# 这是 Vercel 标准 Python 服务端函数，不是普通 Flask
def handler(request):
    return {
        "message": "你好！后端连接成功",
        "status": "ok",
        "author": "你的名字"
    }
