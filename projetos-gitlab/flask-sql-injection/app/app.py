import os
from flask import Flask, render_template, request
from sqlalchemy.sql import text
from sqlalchemy import create_engine
from markupsafe import Markup 

#db_connect = create_engine('mysql://root:my-password@db/my_database')
db_connect = create_engine('sqlite:///mydb.db', echo=True)

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = db_connect

@app.route("/")
def home():
    return render_template('home.html')

@app.route("/login", methods=["POST", "GET"])
def login():
    
    if request.method == 'POST':
        # Recuperar parâmetros passados via formuláruo
        username_from_form = request.form.get('username')
        password_from_form = request.form.get('password')
        
        if not (username_from_form and password_from_form):
            return 'Informe um usuário e senha!', 400
        
        conn = db_connect.connect()

        sql_Query_Not_Injection = text("SELECT * FROM users WHERE username=:username AND password=:password")
        result = conn.execute(sql_Query_Not_Injection, parameters=dict(username = username_from_form
                                                                       , password = password_from_form))
        
        #sql_Query_Injection_False_Negative = text("SELECT * FROM users WHERE username = '" + username_from_form + "'"
         #                                       " AND password = " + password_from_form)                                         
        #result = conn.execute(sql_Query_Injection_False_Negative)

        content = "<table>"
        content = content + str("<tr>")
        content = content + str("<th>id</th>")
        content = content + str("<th>username</th>")
        content = content + str("<th>password</th>")
        content = content + str("</tr>")

        for column in result:
            content = content + str("<tr>")
            content = content + str("<td>"+str(column[0])+"</td>")
            content = content + str("<td>"+str(column[1])+"</td>")
            content = content + str("<td>"+str(column[2])+"</td>")
            content = content + str("</tr>")            

        content = content + str("</table>")
        result = Markup(content)

        return render_template('index.html', result=result)

    if request.method == 'GET':
        # Recuperar parâmetros passados via URL após "?"
        id = request.args.get('id')
        username_from_url = request.args.get('username')
        password_from_url = request.args.get('password')
        
        conn = db_connect.connect()

        sql_Query_Not_Injection = text("SELECT * FROM users WHERE id=:user_id")
        result = conn.execute(sql_Query_Not_Injection, parameters=dict(user_id = id))
        
        #sql_Query_Injection_False_Negative = text("SELECT * FROM users WHERE username = '" + username_from_url + "'"
        #                                        " AND password = " + password_from_url)                                         
        #result = conn.execute(sql_Query_Injection_False_Negative)

        # deprecated in SQLAlchemy >=2.0
        #sql_Query_Injection = "SELECT * FROM users WHERE id={}".format(id)
        #result = conn.execute(sql_Query_Injection)

        content = "<table>"
        content = content + str("<tr>")
        content = content + str("<th>id</th>")
        content = content + str("<th>username</th>")
        content = content + str("<th>password</th>")
        content = content + str("</tr>")

        for column in result:
            content = content + str("<tr>")
            content = content + str("<td>"+str(column[0])+"</td>")
            content = content + str("<td>"+str(column[1])+"</td>")
            content = content + str("<td>"+str(column[2])+"</td>")
            content = content + str("</tr>")            

        content = content + str("</table>")
        result = Markup(content)

        return render_template('index.html', result=result)
    
if __name__ == "__main__":
    app.run()