
from ..Models.User import User
import bcrypt

def getUser(email):
    user = User.objects(email=email).first()
    return {"data":user.to_dict(), "status":200}

def createUser(user):
    #hash the password
    user["password"] = bcrypt.hashpw(user["password"].encode(), bcrypt.gensalt()).decode()
    current_user = User.objects(email=user["email"]).first()
    if current_user != None:
        return {"message":"The email is currently used" ,"status":400}
    user = User(**user).save()
    return {"data":user.to_dict(), "message":"user created" ,"status":201}

def updateUser(user,id):
    user = User.objects(id=id)
    user.update(**user)
    return {"data":user.to_dict(), "message":"user updated" ,"status":200}
    
