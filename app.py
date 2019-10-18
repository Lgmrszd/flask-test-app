from flask import Flask, render_template, redirect
# from flask_socketio import SocketIO

app = Flask(__name__)


@app.route('/')
def index():
    with open("static/site-default", "r") as f:
        config_file = f.read()
    return render_template("index.html", title="Main page", config_file=config_file)


@app.route('/cool_video')
def cool_video():
    return render_template("cool_video.html", title="Cool video!!!")


@app.route('/about')
def about():
    return render_template("about.html", title="About this site")


if __name__ == '__main__':
    app.run()
