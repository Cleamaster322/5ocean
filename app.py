from flask import Flask, render_template, url_for, request, flash, session , redirect,abort
import sqlite3
import os


menu = [{"name":"Установка","url": "install-flask"},
        {"name":"Первое приложение","url": "first-app"},
        {"name":"обратная связь","url": "contact"}]

app = Flask(__name__)

app.config['SECRET_KEY'] = "dasfdsfhgskdjfsdkjlgfsdlkfhd"

# если 2  декоратора друг за другом то при написании / или /index вернет на одну и туже страницу
@app.route("/index")
def index():
    print(url_for("index"))
    # title - переменная которая передается в html 
    return render_template("index.html", menu = menu)
    
@app.route("/about")
def about():
    print( url_for("about"))
    # 1 menu переменная которая передается в html 2 это переменная на 4 строке
    return render_template("about.html",title = "о сайте", menu = menu )
     
# <> - То что напишет пользователь. path: - Весь оставшийся путь даже если есть/. int - цифры 
#  Если в url 2 раза <> <> Тогда 2 переменные идут на вход
# Синтаксис <type:a> Сначала тип а потом название переменной
#  В def username - переменная от строки посика(url). 
@app.route("/profile/<username>")
def profile(username):
    if "userLogged" not in session or session["userLogged"] != username:
        abort(401)
    print( url_for("profile",username = username))
    return f"Пользователь: {username}"

# Метод пост значит что мы разрешаем принимать значение на сервер которые отправил сервер
@app.route("/contact",methods = ["POST", "GET"])
def contact():
    if request.method == "POST":
        # Выведется весь список с формы
        print(request.form)
        # Выведется только значение username
        print(request.form["username"])
        if len(request.form["username"]) > 2:
            # category Для css чтобы по ним обратится и изменить их
            flash("Сообщение отправлено",category="success")
        else:
            flash("Мало символов", category="error")
    return render_template('contact.html',title = "Обратная связь", menu =menu)

# Страница при ошибки 404, 404-в конце -> В консоле выйдет 404 а не 200
@app.errorhandler(404)
def pageNotFound(error):
    return render_template('page404.html',title = "Страница не найдена", menu =menu),404

@app.route("/login", methods = ["POST", "GET"])
def login():
    if 'userLogged' in session:
        return redirect(url_for('profile', username=session['userLogged']))
    # Авторизация
    elif request.method == 'POST'and request.form["username"] == "selfedu" and request.form['psw'] =='123':
        session["userLogged"] = request.form["username"]
        return redirect(url_for('profile', username=session['userLogged']))
    
    return render_template('login.html',title = "Логин", menu = menu)

if __name__ == "__main__":
    app.run(debug=True)