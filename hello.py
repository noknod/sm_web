def app(environ, start_response):
    data = '\n'.join(param for param in environ['QUERY_STRING'].split('&'))
    status_code = '200 OK'
    headers = [('Content-Type', 'text/plain') 
              #, ('Content-Length', str(len(data)))
              ]
    start_response(status_code, headers)
    return iter([data])
