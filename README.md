# User Manager
This library provides an interface for basic user managing which includes
create, authenticate and user permssions

# Install
```bash
pip install user_manager
```

# Using it
First, you need to create an implementation of the interface. A mongo
implementation is provided (using mongoengine)

# Actions
## Create an user
```python
from user_manager.mongoengine import MongoUserManager
um = MongoUserManager()
user = um.create(username="pepe", password="lolazo")

```

## Check authentication an user
```python
from user_manager.mongoengine import MongoUserManager
um = MongoUserManager()
if um.authenticate(username="pepe", password="lolazo"):
   print("Authenticated")


```

## Grant and revoke permissions
```python
from user_manager.user_manager import Permission
from user_manager.mongoengine import MongoUserManager
um = MongoUserManager()
um.grant(role="admin", resource="products", permission=Permission.CREATE)
um.revoke(role="admin", resource="products", permission=Permission.EDIT)
```

Check UserManager class to get more available methods

# Extending the user manager
You can customize the user manager to fit your requirements

```python
from user_manager.mongoengine import MongoUserManager
from user_manager.mongoengine import User
from mongoengine import connect, StringField
connect('mydb')

# My custom user manager, in this case I just modify the "notify" method
class MyUserManager(MongoUserManager):
    def notify(self, event):
        print("New event", event)

# My custom user class
class MyUser(User):
    other_field = StringField(required=True)
    
um = MyUserManager(user_model=My)
um.create(username="pepe", password="lolazo", other_field="This is an example")

```

Check the mongo implementation to get more details on how to customize the user manager
