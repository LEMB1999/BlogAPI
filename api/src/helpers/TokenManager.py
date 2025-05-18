import jwt
from cryptography.hazmat.primitives import serialization
from dotenv import load_dotenv
import os 
from flask  import abort

#read environmet variables
load_dotenv()  

file_path_private_key = os.path.join(os.path.dirname(__file__), "..", "..", "cert", "private_key")
file_path_public_key = os.path.join(os.path.dirname(__file__), "..", "..", "cert", "public_key.pub")

#read the private key
private_key = open(file_path_private_key,"r").read()
private_key = serialization.load_ssh_private_key(private_key.encode(),password=os.environ.get("PASSPHRASE").encode())

public_key = open(file_path_public_key,"r").read()


def get_token(user_info):
    return jwt.encode(user_info,private_key,algorithm="RS256")

def verify_token(token):
    try:
        jwt.decode(token,public_key,algorithms="RS256")
        return True
    except:
      return False
    
def get_header_value_token(token):
    if token.strip() == "":
        return abort(401)    
    token = token.strip().split(" ")
    if len(token) != 2:
        return abort(401)
    if token[0].lower() != "bearer":
        return abort(401)
    return token[1]
