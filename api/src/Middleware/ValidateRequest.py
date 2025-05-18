from functools import wraps
from flask import request, abort

def validate_json(json_structure):
       def _ (f) :
          @wraps(f)
          def decorated_function(*args, **kwargs):
             #logic to validate input   
             data =  request.get_json()
             for property, value in json_structure.items():
                 if value.get("required") and data.get(property) == None:
                    abort(400)
                 
                 if data.get(property) != None:
                    
                    if not isinstance(data.get(property), value["type"]) :  
                        abort(400)

                    if value.get("min-length") != None and isinstance(data.get(property), str ) and  len (data.get(property))  < value.get("min-length"):
                        abort(400)
                     
             return f(*args,**kwargs)
          return decorated_function
       return _
       
""" def validate_request_header(header):
    def _ (f):
        @wraps(f)
        def decorated_function(*args,**kwargs):
            
            header_value = request.headers.get(header["name"])
            if header_value == None:
                abort(400)
            elif header_value != header["value"].lower():
                abort(400)

            return f(*args,**kwargs)
        return decorated_function
    return _ """