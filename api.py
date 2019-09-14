import time

import responder

api = responder.API(docs_route='/docs', version='0.1', openapi="3.0.2", title="Web Service")


@api.on_event('startup')
def startup():
    print('Hello Before Start. Start or load models.')


@api.on_event('shutdown')
def startup():
    print('Bye After Shutdown. Do some DB Shutdown')


@api.route('/')
def greeting(req, resp):
    resp.text = 'Hello World'


@api.route('/divide/{num1:d}/by/{num2:d}')
async def divide(req, resp, *, num1, num2):
    data = await req.media()
    multiplier = int(data.get('multiplier', 1))

    @api.background.task
    def background_sleep():
        time.sleep(4)
        print('Sleeping done. But Resp would be sent by now !')

    background_sleep()
    resp.media = {'success': True, 'answer': num1 / num2 * multiplier}

if __name__ == '__main__':
    api.run()