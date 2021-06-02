from flask import session, jsonify, g, current_app, request
from functools import wraps

class APIError(Exception):

    def __init__(self, code, msg):
        super().__init__(code, msg)
        self.code = code
        self.msg = msg
    
    def response(self) -> dict:
        msg = self.msg 
        return dict(code=self.code, msg=msg)

class API(object):

    @staticmethod
    def handle(f):
        """
        handle API.error() and return the valid response with this error
        Also handle any Exception and simple return `code:100`
        or return what happened when `app.debug`
        """
        @wraps(f)
        def _handle(*args, **kwargs):
            try: 
                result = f(*args, **kwargs)
            except APIError as e:
                return API.result(code=e.code, msg=e.msg)
            except Exception as e:
                if current_app.debug:
                    return API.result(code=100, msg=str(e))
                else:
                    current_app.logger.error(e)
                    return API.result(code=100, msg="Server Exception")
            else:
                return result
        return _handle

    @staticmethod
    def error(code, msg):
        """`raise` this error, and then the API return response in json with code and msg
            In every API, code should started with `0` which automanticly converted to `20x`
        """
        return APIError(code+200, msg)
    
    @staticmethod
    def result(obj=None, code=0, msg="Success"):
        """create response, automatically wraps `Doc`"""
        r = dict(code=code, msg=msg)
        if obj: 
            r["result"] = obj
        return jsonify(r)

    @staticmethod
    def log(msg):
        current_app.logger.info(msg)

    @staticmethod
    def require(*args):
        """ Quick check and get required value in json """
        values = []
        for arg in args:
            value = request.json.get(arg)
            if not value:
                raise APIError(code=101, msg='Missing value: %s' % arg)
            values.append(value)
        return tuple(values) if len(values) > 1 else values[0]