class ApiException(Exception):
    def __init__(self, status_code, body, headers):
        self.status_code = status_code
        self.body = body
        self.headers = headers

        super(ApiException, self).__init__(str(status_code) + " - " + body)
