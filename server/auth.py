import jwt
from aiohttp import web
from .utils import (get_jwt_secret)

async def login(request):
    data = await request.json()
    username = data.get('username')
    password = data.get('password')
    # Check if the user is valid
    if username == 'admin' and password == 'admin':
        payload = {'user': username}
        token = jwt.encode(payload, get_jwt_secret(), algorithm='HS256')
        return web.json_response({'token': token})
    return web.Response(status=401, text='Unauthorized')



