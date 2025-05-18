from ..Models.Article import Article

def getArticles():
    return {"data": Article.objects(), "status":200} 

def getArticle(id):
    article = Article.objects(id=id).first()
    return {"data":article.to_dict(), "status":200}

def createArticle(article):
    article = Article(title=article["title"],description=article["description"]).save()
    return {"data":article.to_dict(), "message":"article created", "status":201}

def deleteArticle(id):    
    article = Article.objects(id=id).first()    
    article.delete()
    return {"data":article.to_dict(), "message":"article deleted", "status":200} 

def updateArticle(data,id):
    article = Article.objects(id=id).first()
    article.update(**data)
    return {"data":article.to_dict(),"message":"article updated","status":200}