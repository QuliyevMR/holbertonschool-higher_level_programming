#!/usr/bin/python3
"""
Bu modul Python-un daxili http.server modulu vasitəsilə
sadə bir API (veb server) qurmağı təmin edir.
"""
import http.server
import socketserver
import json

# Serverin dinləyəcəyi port
PORT = 8000


class SimpleAPIHandler(http.server.BaseHTTPRequestHandler):
    """
    HTTP GET sorğularını idarə edən sinif.
    """

    def do_GET(self):
        """
        GET sorğularını qəbul edir və endpoint-ə görə cavab qaytarır.
        """
        # 1. Ana səhifə (Root endpoint)
        if self.path == '/':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Hello, this is a simple API!")

        # 2. /data endpoint-i (JSON formatında)
        elif self.path == '/data':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            dataset = {"name": "John", "age": 30, "city": "New York"}
            # Lüğəti JSON stringinə, onu da baytlara çeviririk
            self.wfile.write(json.dumps(dataset).encode("utf-8"))

        # 3. /status endpoint-i
        elif self.path == '/status':
            self.send_response(200)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"OK")

        # 4. /info endpoint-i (Gözlənilən nəticə hissəsindəki şərt üçün)
        elif self.path == '/info':
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            info = {
                "version": "1.0",
                "description": "A simple API built with http.server"
            }
            self.wfile.write(json.dumps(info).encode("utf-8"))

        # 5. Tapılmayan hər hansı digər endpoint (404 Error)
        else:
            self.send_response(404)
            self.send_header("Content-type", "text/plain")
            self.end_headers()
            self.wfile.write(b"Endpoint not found")


if __name__ == "__main__":
    # Serveri qeyd olunan portda işə salırıq
    with socketserver.TCPServer(("", PORT), SimpleAPIHandler) as httpd:
        print(f"Serving API on port {PORT}...")
        # Serveri dayandırana qədər (Ctrl+C) işləməyə davam edəcək
        httpd.serve_forever()
