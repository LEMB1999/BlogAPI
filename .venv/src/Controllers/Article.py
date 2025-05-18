from flask import Blueprint,request
from .. Services import ArticlesDBService
from ..Middleware import ValidateToken, ValidateRequest 

main = Blueprint("article",__name__)

@main.get("/")
@ValidateToken.check_authentication
def getArticles():
    result = ArticlesDBService.getArticles()
    return result

@main.get("/<int:id>")
@ValidateToken.check_authentication
def getArticle(id):
    result = ArticlesDBService.getArticle(id)
    return result 

@main.post("/")
@ValidateToken.check_authentication
@ValidateRequest.validate_json(
       {"title":{"type":str,"required":True,"min-length": 5 },
        "description":{"type":str,"required":True,"min-length":5}})
def createArticle():
    data = request.get_json()
    result = ArticlesDBService.createArticle(data)
    return result

@main.delete("/<int:id>")
@ValidateToken.check_authentication
def deleteArticle(id):
    result = ArticlesDBService.deleteArticle(id)
    return result

@main.put("/<int:id>")
@ValidateToken.check_authentication
@ValidateRequest.validate_json(
       {"title":{"type":str,"required":True,"min-length": 5 },
        "description":{"type":str,"required":True,"min-length":5}})
def updateArticle(id):
    data = request.get_json()
    result = ArticlesDBService.updateArticle(data,id)
    return result

  

