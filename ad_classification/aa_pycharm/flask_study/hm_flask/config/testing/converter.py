from werkzeug.routing import BaseConverter


class TelConverter(BaseConverter):
    regex = r'1[3-9]\d{9}'


