from flask import Flask, render_template


menu = {"1", 2, "3"}

app = Flask(__name__)
# если 2  декоратора друг за другом то при написании / или /index вернет на одну и туже страницу
@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html", menu = menu) # title - переменная которая передается в html 
    
@app.route("/about")
def about():
    return render_template("about.html",title = "о сайте", menu = menu ) # 1 menu переменная которая передается в html 2 это переменная на 4 строке

if __name__ == "__main__":
    app.run(debug=True)