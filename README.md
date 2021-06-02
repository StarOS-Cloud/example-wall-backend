# Recoard API

## Install

### Enviroument Variable

- **required** MYSQL_HOST 
- **required** MYSQL_PWD

### Docker command

#### Docker build
```shell
docker build -t wall/api:latest .
```

#### Docker run
```shell
docker run -d --name wall-api \
  -e MYSQL_HOST=<HOST> \
  -e MYSQL_PWD=<PWD> \
  -p 5000:5000 \
  wall/api:latest
```
