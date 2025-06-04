from flask import Flask

# インスタンス作成
app = Flask(__name__)

# ルートデコレーター
@app.route("/")
def hello_world():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(debug=True)