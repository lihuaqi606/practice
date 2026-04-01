def handler(request):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json; charset=utf-8"
        },
        "body": '{"message":"你好！后端连接成功","status":"ok","author":"你的名字"}'
    }
