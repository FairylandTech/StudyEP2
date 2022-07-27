from werkzeug.routing import BaseConverter


class Telephone(BaseConverter):
    regex = r'1[3-9]\d{9}'
    