from flask import Flask, render_template, redirect
# from flask_socketio import SocketIO

app = Flask(__name__)


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/cool_video')
def cool_video():
    return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ")


if __name__ == '__main__':
    app.run()
