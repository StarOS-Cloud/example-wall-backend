FROM python:3.8-alpine
WORKDIR /root/wall/api
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY ./ ./
RUN mkdir log
EXPOSE 5000
ENTRYPOINT ["gunicorn", "-c", "gunicorn.py", "main:app"]
