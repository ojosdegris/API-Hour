import hashlib
import asyncio
import aiorest


def about(request):
    return {'app_name': request.server.config['name']}


def secret(request):
    return {'hashed_secret': hashlib.sha512(request.server.config['secret'].encode('utf-8')).hexdigest()}


class App(aiorest.RESTServer):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.config = {'name': 'aiorest', 'secret': 'sducvvhdivhvidvd'}


def main():
    loop = asyncio.get_event_loop()

    server = App(hostname='127.0.0.1', loop=loop)
    server.add_url('GET', '/about', about)
    server.add_url('GET', '/secret', secret)

    srv = loop.run_until_complete(loop.create_server(
        server.make_handler, '127.0.0.1', 8080))

    loop.run_forever()


if __name__ == '__main__':
    main()
