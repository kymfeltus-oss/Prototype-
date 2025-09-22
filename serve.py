import http.server, socketserver, webbrowser
PORT = 5500
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(('', PORT), Handler) as httpd:
    url = f'http://localhost:{PORT}/index.html#dashboard'
    print(f'Serving prototype at {url}')
    try: webbrowser.open(url)
    except Exception as e: print('Could not open browser automatically:', e)
    httpd.serve_forever()
