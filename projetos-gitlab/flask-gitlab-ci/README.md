# Flask Gitlab-CI

Modelo para uso do CI/CD do Gitlab em uma aplicação Python+Flask, com execução de testes unitários utilizando PyUnit.

Para a execução da pipeline o Gitlab Runner foi [configurado em uma instância AWS EC2](https://docs.gitlab.com/runner/install/linux-repository.html), com Ubuntu.

## Executando os testes unitários localmente

```
$ python -m unittest -v tests/appTest.py

test_http_code (tests.appTest.AppTest.test_http_code) ... ok
test_print_hello_world (tests.appTest.AppTest.test_print_hello_world) ... ok

----------------------------------------------------------------------
Ran 2 tests in 0.019s

OK
```