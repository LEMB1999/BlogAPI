from flask import Blueprint ,request
from ..helpers import TokenManager
from ..Services import UserDBService
from ..helpers import ValidateAuthentication
from ..Middleware.ValidateRequest import validate_json

main = Blueprint("auth",__name__)


@main.post("/register")
@validate_json({"name":{"type": str,"required":True, "min-length": 3 },
                "email":{"type":str,"required":True , "min-length": 3 },
                "password":{"type":str,"required":True, "min-length":8}})
def register():    
    data = request.get_json()
    #result = UserDBService.createUser(data)
    return "test" #result

@main.post("/login")
@validate_json(
       {"email":{"type":str,"required":True,"min-length": 3 },
           "password":{"type":str,"required":True,"min-length":8}})           
def authentication():
    user_login_info =  request.get_json()
    user, isValid = ValidateAuthentication.validateCredentials(user_login_info)
    
    if not isValid:
        return {"message":"Invalid Credentials","status":400}
    
    token = TokenManager.get_token(user)
    return {"data":token,"status":200}
    

