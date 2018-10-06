import requests


class MainClass(object):
    def make_call(self):
        return RequestClass.post_request()

class RequestClass(object):
    @staticmethod
    def post_request():
        body = {'title': 'foo', 'body': 'bar', 'userId': 1}
        response = requests.post('https://jsonplaceholder.typicode.com/posts', json=body)
        return response.json()


if __name__ == '__main__':
    mc = MainClass()
    print(mc.make_call())