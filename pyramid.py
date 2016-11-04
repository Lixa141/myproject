from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response


def index(request):
    return Response("""<a href="index.html">THIS LINK FOR INDEX!!!</a> <br> <a href="http://localhost:8000/index.html">FANTASTIK LINK</a>""")
def about(request):
    return Response("""<a href="about/aboutme.html">this is sad link</a> <br> <a href="http://localhost:8000/about/aboutme.html">please don't press it</a>""")

if __name__ == '__main__':
    configurator=Configurator()
    configurator.add_route('index', '/index.html')
    configurator.add_view(Index, route_name='index')
    configurator.add_route("aboutme",'/about/aboutme.html')
    configurator.add_view(AboutMe,route_name='aboutme')
    app=configurator.make_wsgi_app()
    server = make_server('0.0.0.0', 8000, app)
    server.serve_forever()
