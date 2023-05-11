from aiohttp import web
from .utils import (match_path_regex)
from .whitelist import (WHITELIST)
from .auth import (validate_request)

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
            valid_request = validate_request(request)            
            if not valid_request:                
                return web.Response(status=401, text='Unauthorized')
            else:                
                return await handler(request)
        except Exception as e:            
            return web.Response(status=401, text='Unauthorized')        
