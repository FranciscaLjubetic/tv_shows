import bcrypt
from django.shortcuts import render, redirect, HttpResponse
from main_tv.models import Show, Network, Users
from django.contrib import messages
from django.db import IntegrityError
from .decorators import *

def index(request):
    context = {
        'saludo': 'Hola'
    }
    return render(request, 'index.html', context)

@login_protect
def shows(request):
    Shows= Show.objects.all()
    networks = Network.objects.all()

    context = {
        'Shows': Shows,
        'Networks': networks,
    }
    return render(request,'shows.html', context)

@login_protect
def addshow(request):
    Shows= Show.objects.all()
    networks = Network.objects.all()

    context = {
        'Shows': Shows,
        'Networks': networks,
    }
    return render(request, 'shows_new.html', context)

@login_protect
def create(request):
    errors = Show.objects.basic_validator(request.POST)
    network = None
    if request.POST['network_input'] == 'other':
        # en este caso hay que crearla
        new_network_name = request.POST['newNetwork']
        network = Network.objects.create(title = new_network_name)
    else:
        
        # en este caso hay que rescatarla de la DB
        network_id = request.POST['network_input']
        network = Network.objects.get(id=network_id)
    # Ahora estamos 100% seguros que SI existe 'network'
    showTitle = request.POST['title_input']
    showDate = request.POST['release_date']
    showDesc = request.POST['desc_input']
    
    if len(errors)> 0: #si el suscriptor lleno mal esta cuestion
        for key, error_message in errors.items():
            messages.error(request, error_message)
        return redirect(f'/shows/new')
    
    new_show = Show.objects.create(title = showTitle, release_date = showDate, description = showDesc, networks = network)
    messages.success(request, 'Show successfully created')

    return redirect('/shows')
    


@login_protect
def editshow(request, num):
    edit_show = Show.objects.get(id= int(num))
    Networks = Network.objects.all()
    
    if request.method== 'GET':
        # yo no tuve ese problema, pero en caso de que me de jugo la fecha hago lo siguiente:
        #time_str=edit_show.release_date.strftime('%Y-%m-%d')
        context = {
            'edit_show': edit_show,
            #'time_str':time_str,
            'Networks': Networks
        }
        return render(request,'shows_edit.html',  context)
    
    else:
        errors = Show.objects.basic_validator(request.POST)
        network_id= int(request.POST['network_input'])
        network = Network.objects.get(id=network_id)
        showTitle = request.POST['title_input']
        showDate = request.POST['release_date']
        showDesc = request.POST['desc_input']
        
        
        if len(errors)> 0: #si el suscriptor lleno mal esta cuestion
            for key, error_message in errors.items():
                messages.error(request, error_message)
            return redirect(f'/shows/{num}/edit')
        
        edit_show.title = showTitle
        edit_show.release_date =  showDate
        edit_show.description = showDesc
        edit_show.networks = network
        #aqui no hago create, porque lo que necesito es sobreescribir algo que ya existe
        
        try:
            edit_show.save()
            messages.success(request, 'Show successfully updated')
                
        except IntegrityError:
            messages.error('This shows already exists')
            #new_show.network.add(network)
            return redirect(f'/shows/{num}/edit')
        
        return redirect('/shows')

@login_protect
def tvshow(request, num):
    this_show = Show.objects.get(id= num)
    context = {
        
        'this_show': this_show,
    }
    
    return render(request, 'tv_show.html', context)

@login_protect
def delete(request, num):
    show_id= Show.objects.get(id= num)
    show_id.delete()
    return redirect('/shows')
    

def second(request, name):
    return HttpResponse('Hola ' + name)

def register(request):
    if request.method == 'GET':
        context = {
            'users': Users.objects.all(),
        }
        return render(request, 'register.html')
    
    else:
        name= request.POST['name']
        email =request.POST['email']
        password =request.POST['password']
        password_confirm=request.POST['password_confirm']
        
        
    errors = Users.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for llave, error_message in errors.items():
            messages.error(request, error_message)
        return redirect('/register')
        #avatar =request.POST['avatar']
    '''
    if password != password_confirm:
        messages.errorr(request, 'Passwords don??t match. Try again')
        return redirect('/register') ahora la validacion la hago en el validador
    '''
        
    user = Users.objects.create(
        name = name,
        email= email,
        password = bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()
    )
    request.session['user']={
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'avatar': user.avatar
    }
    messages.success(request, 'User successfully created')
    return redirect('/shows')

def logout(request):
    del request.session['user'] 
    return redirect('/register')

def login(request):
    email = request.POST['email']
    password = request.POST['password']
    try:
        user = Users.objects.get(email=email)
    except Users.DoesNotExist:
        messages.error(request, 'User does not exist')
        return redirect('/register')
    
    # si llegamos ac??, estamos seguros que al  menos el usuario SI existe
    if  not bcrypt.checkpw(password.encode(), user.password.encode()): 
        messages.error(request, 'User or Password are wrong')
        return redirect('/register')
    
    # si llegamos hasta ac??, estamos seguros que es el usuario y la contrase??a est?? correcta
    request.session['user'] = {
        'id': user.id,
        'name': user.name,
        'email': user.email,
        'avatar': user.avatar
    }
    messages.success(request, f'Hello, {user.name}')
    return redirect('/shows')
        
    
    