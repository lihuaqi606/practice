from http.server import BaseHTTPRequestHandler
import json

class handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json; charset=utf-8')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        
        response = {
            "message": "✅ 后端连接成功！",
            "version": "Vercel Standard Class 版",
            "data": "来自api/hello"
        }
        
        self.wfile.write(json.dumps(response).encode('utf-8'))
        return
