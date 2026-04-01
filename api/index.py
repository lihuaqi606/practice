from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello():
    return jsonify({
        "message": "你好！来自Python后端",
        "status": "运行成功",
        "info": "部署在Vercel"
    })
