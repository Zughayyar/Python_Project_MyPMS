from django.db import models
import bcrypt, re # type: ignore
from datetime import date

###########################################
####### Validation Classes (Managers) #####
###########################################
class UserManager(models.Manager):
    def basic_validator(self, data):
        errors = {}
        if len(data['username']) < 8:
            errors['first_name'] = "First Name should be at least 8 characters!"
        if len(data['name']) < 8:
            errors['last_name'] = "First Name should be at least 8 characters!"
        if len(data['password']) < 8:
            errors['password_len'] = "Password should be at least 8 characters!"
        if data['re_password'] != data['password'] and len(data['password']) >= 8:
            errors['password_match'] = "Password not match!"
        return errors

class ClientManager(models.Manager):
    def basic_validator(self, data):
        errors = {}
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(data['company_name']) < 3:
            errors['company_name'] = "First Name should be at least 3 characters!"
        if len(data['contact_name']) < 3:
            errors['contact_name'] = "First Name should be at least 3 characters!"
        if len(data['phone_number']) < 10:
            errors['phone_number'] = "First Name should be at least 10 numbers!"
        if not EMAIL_REGEX.match(data['email']):
            errors['email'] = "E-mail address should be valid!"
        return errors

class ProjectManager(models.Manager):
    def basic_validator(self, data):
        errors = {}
        if len(data['name']) < 3:
            errors['name'] = "First Name should be at least 3 characters!"
        if len(data['location']) < 3:
            errors['location'] = "First Name should be at least 3 characters!"
        if len(data['main_contractor']) < 3:
            errors['main_contractor'] = "First Name should be at least 3 characters!"
        return errors

###########################
###### Table Classes ######
###########################
class Department(models.Model):
    name = models.CharField(max_length=255)
    desc = models.TextField( default="No desription added!")
    
class User(models.Model):
    username = models.CharField(max_length=255, default="null")
    name = models.CharField(max_length=255, default="null")
    password = models.CharField(max_length=255, default="null")
    department = models.ForeignKey(Department, on_delete=models.DO_NOTHING, related_name="users", default="null")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

class Client(models.Model):
    company_name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ClientManager()

class Project(models.Model):
    name = models.CharField(max_length=255)
    client = models.ForeignKey(Client,on_delete=models.DO_NOTHING,related_name="projects")
    location = models.CharField(max_length=255)
    main_contractor = models.CharField(max_length=255)
    manager = models.ForeignKey(User,on_delete=models.DO_NOTHING,related_name="projects")
    deadline = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

#################################
###### Methods (Functions) ######
#################################
def create_user(data):
    password =data['password']
    hashed_pwd = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    User.objects.create(
        username = data['username'],
        name = data['name'],
        password = hashed_pwd,
        department = data['department']
    )

def get_user_by_username(username):
    return User.objects.filter(username=username)

def is_user_exist(data):
    users = get_user_by_username(username = data['username'])
    if len(users) == 0:
        return False
    else:
        return True

def is_password_match(entered_email, entered_password):
    user = User.objects.filter(email = entered_email)
    password = user[0].password
    return bcrypt.checkpw(entered_password.encode() , password.encode())

def check_login(data):
    entered_username = data['username']
    entered_password = data['password']
    return is_password_match(entered_username,entered_password)









    

