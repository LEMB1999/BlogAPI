import mongoengine as me 
class User(me.Document):
    #id = me.IntField(primary_key=True)
    name = me.StringField()
    email = me.EmailField(required=True,unique=True)
    password = me.StringField(required=True)
    def to_dict(self):
      return {
         "email":self.email,
         "name":self.name,
      }