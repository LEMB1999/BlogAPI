from ..Models.User import User
import bcrypt

def validateCredentials(user_info):
    user = User.objects(email=user_info["email"]).first()
    
    if user == None:
        return None,False
     
    if bcrypt.checkpw(user_info["password"].encode(),user["password"].encode()):
        return user.to_dict() , True
    else:
        return None, False
