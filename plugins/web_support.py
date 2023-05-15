from aiohttp import web
import datetime
from helpers import temp

routes = web.RouteTableDef()

@routes.get("/", allow_head=True)
async def root_route_handler(request):
     runtime = datetime.datetime.now()
    t = runtime - temp.START_TIME
    runtime = str(datetime.timedelta(seconds=t.seconds))

    res = {
        "status": "running",
        "bot": temp.BOT_USERNAME,
        "runtime": runtime,
    }
    return web.json_response(res)


async def web_server():
    web_app = web.Application(client_max_size=30000000)
    web_app.add_routes(routes)
    return web_app
