from django.db import models
import bcrypt, re # type: ignore

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

class User(models.Model):
    username = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()

def create_user(data):
    password =data['password']
    hashed_pwd = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    User.objects.create(
        username = data['username'],
        name = data['name'],
        password = hashed_pwd
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

class Client(models.Model):
    company_name = models.CharField(max_length=255)
    contact_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = ClientManager()