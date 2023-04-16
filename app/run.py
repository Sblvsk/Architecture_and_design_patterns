from wsgiref.simple_server import make_server

from sblvsk_framework.main import Framework
from urls import routes, fronts


application = Framework(routes, fronts)

with make_server('', 8002, application) as httpd:
    print("Serving on port 8002...")
    httpd.serve_forever()
