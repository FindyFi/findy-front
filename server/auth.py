import jwt
import time
import datetime
from .utils import (get_jwt_secret, hash_password)
from .db import (get_db_manager)


async def authenticate(email, password):
    # Check if the user is valid    
    if read_user_credentials(email, password):
        payload = {'user': email, 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)}        
        token = jwt.encode(payload, get_jwt_secret(), algorithm='HS256')
        return{'status': True ,'token': token}
    return {'status': False, 'error': 'Invalid username/password'}


def validate_token(token):
    try:        
        # Decode the token using the secret key
        decoded = jwt.decode(token, get_jwt_secret(), algorithms=['HS256'])        
        # Check if the token has expired
        if 'exp' in decoded and decoded['exp'] < time.time():
            return False
        # If everything checks out, return True
        return True
    except jwt.InvalidTokenError:
        # If there's an error decoding the token, return False
        return False

def validate_request(request):
     # Get the Authorization header from the request
    authorization_header = request.headers.get('Authorization')

    if authorization_header:
        # Split the header value to separate the token from the "Bearer" prefix
        parts = authorization_header.split()

        if len(parts) == 2 and parts[0].lower() == 'bearer':
            jwt_token = parts[1]
            if validate_token(jwt_token):
                # The token is valid, so return the request
                return True
            else:
                # The token is invalid, so return an error
                return False            
            
    # No JWT token found in the header
    return False


def read_user_credentials(email, password):
    try:
        db_manager = get_db_manager()
        # Execute a SELECT query to check if the username and password match
        query = "SELECT COUNT(*) FROM users WHERE email = %s AND password = %s"

        db_manager.execute(query, (email, hash_password(password)))
        result = db_manager.fetchone()        
        # If a row with matching username and password exists, authentication is successful        
        return result[0] > 0
    except (Exception) as error:
        print("Error while reading from the database:", error)
