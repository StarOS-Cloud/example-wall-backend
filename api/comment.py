from flask import Blueprint, jsonify, g, request
from .base import API

api = Blueprint('comment', __name__)

@api.route('', methods=["GET"])
@API.handle
def get_all_comments():
    comments = Comment.get_all() 
    return API.result(comments)

@api.route('', methods=["POST"])
@API.handle
def create_comment():
    title = "News:" + request.json.get("title")
    content = request.json.get("content")
    comment = Comment(title, content)
    comment.inserted()
    return API.result()

class Comment(object):
    def __init__(self, title, content):
        self.title = title
        self.content = content
    
    @staticmethod
    def get_all():
        raw_sql = "SELECT * FROM `comment` ORDER BY create_time DESC"
        try:
            cursor = g.db.cursor()
            cursor.execute(raw_sql)
            result = cursor.fetchall()
            def convert(item):
                return {
                    "id": item[0],
                    "title": item[1],
                    "content": item[2],
                    "create_time": item[3] 
                }
            result = [convert(x) for x in result]
            cursor.close()
        except Exception as e:
            cursor.close()
            raise(e)
        return result
    
    def inserted(self):
        raw_sql = "INSERT INTO comment(title, content) VALUES('%s', '%s')" % (self.title, self.content or '')
        try:
            cursor = g.db.cursor()
            result = cursor.execute(raw_sql)
            if result == 0:
                raise API.error(1, "can't create comment")
            g.db.commit()
            cursor.close()
        except Exception as e:
            g.db.rollback()
            cursor.close()
            raise(e)
        return
