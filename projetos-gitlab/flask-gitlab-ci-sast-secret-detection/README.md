# Flask Gitlab-CI-SAST

Modelo para uso do CI/CD do Gitlab em uma aplicação Python+Flask+uWSGI, realizando a execução dos seguintes stages:

1. Testes Unitários com PyUnit;
3. SAST com Semgrep;

Para a execução da pipeline o Gitlab Runner foi [configurado em uma instância AWS EC2](https://docs.gitlab.com/runner/install/linux-repository.html), com Ubuntu.

## Deploy local, com Docker

```
$ docker build --tag your-user/my-flask-gitlab-ci-sast .
```

## Testando

```
$ docker run -d -p 5000:5000 your-user/my-flask-gitlab-ci-sast
```
Saída esperada:
```
id-contêiner
$ curl localhost:5000/health-check

<h1>Hello World!</h1>
```

## Executando testes unitários

```
$ python -m unittest -v tests/appTest.py
```
Saída esperada:
```
test_http_code_health_check (tests.appTest.AppTest.test_http_code_health_check) ... ok
test_http_code_hello_error (tests.appTest.AppTest.test_http_code_hello_error) ... ok
test_print_health_check (tests.appTest.AppTest.test_print_health_check) ... ok
test_print_hello_error (tests.appTest.AppTest.test_print_hello_error) ... ok
test_print_hello_success (tests.appTest.AppTest.test_print_hello_success) ... ok

----------------------------------------------------------------------
Ran 5 tests in 0.010s

OK
```