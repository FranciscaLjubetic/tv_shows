from django.db import models
from datetime import date, datetime
from django.db import models

# Create your models here.
class Tvshows_manager(models.Manager):
    def basic_validator(self, post_data):
        errors ={}
        #today = date.today()

        if len(post_data['title_input']) < 4:
            errors['title_input'] = 'Title should have at least four characters'
        
        if len(post_data['desc_input']) < 30:
            errors['desc_input'] = 'Description should have at least 10 characters'
        
        if len(post_data['network_input']) =='other':
            errors['network_input'] = 'Please select a network'
        
        try:
            if datetime.strptime(post_data['release_date'],"%Y-%m-%d").date() > datetime.today().date():
                errors['release_date'] = 'The release time should be today or earlier'
            #Show.release_date.strftime('%Y-%m-%d')
        except ValueError:
            errors['release_date'] = 'You should pick a date'
            
            
        return errors
    
class Users_manager(models.Manager):
    
    def basic_validator(self, post_data):
        errors ={}
        #today = date.today()

        if len(post_data['name']) < 4:
            errors["name"] = "Name should have at least 4 characters"
        
        if len(post_data['email']) < 4:
            errors["email"] = "Email should have at least 4 characters"
        
        if len(post_data['password']) < 6:
            errors['password'] = 'Password should have at least 6 characters'
        
        if post_data['password']!= post_data['password_confirm']:
            errors['password'] = 'Passwords do not match'
        
        
        return errors
    '''
    def basic_validator_for_create(self, post_data):
        errors ={}
        #today = date.today()
        if len(post_data['new_network_name']) < 2 & len(post_data['new_network_name']) > 20:
            errors['new_network_name'] = 'IGDAF'

        if len(post_data['title_input']) < 2:
            errors['title_input'] = 'Title should have at least two characters'
        
        if len(post_data['desc_input']) < 10:
            errors['desc_input'] = 'Description should have at least 10 characters'
        
        if len(post_data['network_input']) =='other':
            errors['network_input'] = 'Please select a network'
            
        if datetime.strptime(post_data['release_date'],"%Y-%m-%d").date() > datetime.today().date():
            errors['release_date'] = 'The release time should be today or earlier'
            
        return errors 
        
    '''
    
    

class Network(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __repr__(self):
        return f"<Movie object: {self.title} ({self.id})>"

class Show(models.Model):
    title = models.CharField(max_length=255, unique=True)
    release_date = models.DateField()
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    networks = models.ForeignKey(Network, related_name="curr_shows", on_delete = models.CASCADE)
    objects = Tvshows_manager()

    def __repr__(self):  
        return f"<Movie object: {self.title} ({self.id})>"

class Users(models.Model):
    name = models.CharField(max_length= 255, unique= True)
    email = models.EmailField(max_length = 50, unique= True)
    password  = models.CharField(max_length= 14, unique = True)
    allowed = models.BooleanField(default =True)
    avatar = models.URLField(
        default='https://www.pngkey.com/png/full/331-3315307_our-insert-name-here-meme.png')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    objects = Users_manager()
    
    def __repr__(self) -> str:
        return f'{self.id}: {self.name}' 
