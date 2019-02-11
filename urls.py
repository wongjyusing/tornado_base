from views import index
from tornado.web import url
urlpatterns = [
    url(r'/', index.TestHandler, name='home'),
    # url(r'/detail/(?P<slug>[\w-]+)', index.DetailHandler,name='detail'),
    # url(r'/tags/(?P<slug>[\w-]+)', index.AllTagHandler,name='tags'),
]
