from flask import Flask, jsonify

app = Flask(__name__)

# 后端API接口
@app.route('/api/hello')
def hello():
    return jsonify({
        "message": "你好！来自Python后端",
        "status": "运行成功",
        "author": "你的名字"
    })

# 前端页面路由
@app.route('/')
def home():
    return app.send_static_file('index.html')

if __name__ == '__main__':
    app.run(debug=True)
