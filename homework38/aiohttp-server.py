from aiohttp import web

from calculator import calculator


async def result_output(request):
    operation = request.rel_url.query['operation']
    numb1 = request.rel_url.query['numb1']
    numb2 = request.rel_url.query['numb2']
    result = calculator(operation, numb1, numb2)
    output = f"number_1: {operation}, operation: {numb1}, number_2: {numb2} = result {result}"
    return web.Response(text=output)


if __name__ == '__main__':
    app = web.Application()
    app.router.add_route('GET', "/", result_output)

    web.run_app(app,host='localhost', port=8000)
