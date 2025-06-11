from http.server import SimpleHTTPRequestHandler, HTTPServer
import socketserver
import os
import webbrowser

class CustomHandler(SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            # Read the README.md content
            with open('README.md', 'r') as f:
                readme_content = f.read()
            
            # Read the index.html template
            with open('index.html', 'r') as f:
                html_content = f.read()
            
            # Insert the README content into the HTML
            final_html = html_content.replace('<!-- README_CONTENT -->', 
                                           f'<pre>{readme_content}</pre>')
            
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(final_html.encode('utf-8'))
        else:
            super().do_GET()

def run(server_class=HTTPServer, handler_class=CustomHandler, port=8000):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    webbrowser.open(f'http://localhost:{port}')
    httpd.serve_forever()

if __name__ == '__main__':
    run()
