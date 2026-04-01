def handler(request):
    """Vercel Python 云函数标准入口"""
    return {
        "statusCode": 200,
        "headers": {
            "Content-Type": "application/json; charset=utf-8",
            "Access-Control-Allow-Origin": "*"
        },
        "body": '{"message":"✅ 后端连接成功！","version":"Vercel CLI 50+兼容版","data":"来自api/hello"}'
    }
