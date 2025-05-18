from flask import request ,abort
from ..helpers import TokenManager
from functools import wraps

def check_authentication(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        # Middleware logic here
        token = request.headers.get("Authorization",default="")
        token = TokenManager.get_header_value_token(token)        
        isValidate = TokenManager.verify_token(token)    
        if not isValidate:
            abort(401)
        return f(*args, **kwargs)
    return decorated_function
