def handler(request):
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json; charset=utf-8",
            "Access-Control-Allow-Origin": "*"
        },
        "body": '{"message":"✅ 后端连接成功！","status":"ok","version":"Vercel 50+ 兼容版"}'
    }
