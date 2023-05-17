# Flask Gitlab-CI-AWS-ECS

Modelo para uso do CI/CD do Gitlab em uma aplicação Python+Flask+uWSGI, realizando a execução dos seguintes stages:

1. Build da imagem Docker no Gitlab Registry;
2. Deploy no AWS ECS.

Para a execução da pipeline o Gitlab Runner foi [configurado em uma instância AWS EC2](https://docs.gitlab.com/runner/install/linux-repository.html), com Ubuntu.

## Variáveis Configuradas no Gitlab

* AWS_ACCESS_KEY_ID
* AWS_SECRET_ACCESS_KEY
* AWS_SESSION_TOKEN
* AWS_DEFAULT_REGION
* CI_AWS_ECS_CLUSTER
* CI_AWS_ECS_SERVICE
* CI_AWS_ECS_TASK_DEFINITION

## Deploy local, com Docker

```
$ docker build --tag seu-usuário/my-flask-app-ecs .
```

## Testando

```
$ docker run -d -p 5000:5000 seu-usuário/my-flask-app-ecs
```
Saída esperada:
```
id-contêiner
$ curl localhost:5000

<h1>Hello From ECS!</h1>
```

## Executando testes unitários

```
$ python -m unittest -v tests/appTest.py
```
Saída esperada:
```
test_http_code (tests.appTest.AppTest.test_http_code) ... ok
test_print_hello_world (tests.appTest.AppTest.test_print_hello_world) ... ok
----------------------------------------------------------------------------

Ran 2 tests in 0.013s
OK
```
Baseado no projeto [Docker-Flask-uWSGI](https://github.com/cirolini/Docker-Flask-uWSGI/)