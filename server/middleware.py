import jwt
from aiohttp import web
from .utils import (get_jwt_secret, match_path_regex)
from .whitelist import (WHITELIST)

@web.middleware
async def jwt_middleware(request, handler):    
    result = await match_path_regex(WHITELIST, request.path)
    if result is True:
        return await handler(request)
    else:     
        token = request.headers.get('Authorization', None)    
        if not token:
            return web.Response(status=401, text='Unauthorized')
        try:
            payload = jwt.decode(token, get_jwt_secret(), algorithms=['HS256'])
            request.user = payload['user']
        except jwt.InvalidTokenError:
            return web.Response(status=401, text='Unauthorized')
        return await handler(request)
