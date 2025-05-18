import mongoengine as me 
class Article(me.Document):
    #id = me.IntField(primary_key=True)
    title = me.StringField()
    description = me.StringField()

    def to_dict(self):
        return {
            "id":self.id,
            "title":self.title,
            "description":self.description
        }