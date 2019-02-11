from tornado.web import RequestHandler
from .db_sql_class import BaseHandler



class TestHandler(RequestHandler):
    def get(self):
        self.render(template_name='base.html')
