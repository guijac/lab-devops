# Flask Docker

Modelo para uso de uma aplicação Python + Flask, utilizando Docker.

## Build da imagem Docker

```
$ docker build --tag seu-usuário/my-flask-app-docker .
[+] Building 69.7s (4/9)
=> [1/5] FROM docker.io/library/python@sha256:d3
.
.
.
$ docker images
REPOSITORY TAG IMAGE ID CREATED SIZE
my-flask-app-docker latest 40f8ac1a4476 About a minute ago 941MB

```

## Testando

```
$ docker run -d -p 5000:5000 seu-usuário/my-flask-app-docker
id-contêiner
$ curl localhost:5000
<h1>Hello World!</h1>

```
## Finalizando

```
$ docker stop id-contêiner

```