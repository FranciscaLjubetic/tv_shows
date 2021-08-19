from django.shortcuts import render, redirect, HttpResponse
from main_tv.models import Show, Network

def index(request):
    context = {
        'saludo': 'Hola'
    }
    return render(request, 'index.html', context)


def shows(request):
    Shows= Show.objects.all()
    networks = Network.objects.all()

    context = {
        'Shows': Shows,
        'Networks': networks,
    }
    return render(request, 'shows.html', context)


def addshow(request):
    Shows= Show.objects.all()
    networks = Network.objects.all()

    context = {
        'Shows': Shows,
        'Networks': networks,
    }
    return render(request, 'shows_new.html', context)


def create(request):
    if request.POST['network_input'] == 'other':
        # en este caso hay que crearla
        new_network_name = request.POST['newNetwork']
        network = Network.objects.create(name = new_network_name)
    else:
        # en este caso hay que rescatarla de la DB
        network_id = request.POST['network_input']
        network = Network.objects.get(id=network_id)
    # -------

    showTitle = request.POST['title_input']
    showDate = request.POST['release_date_input']
    showDesc = request.POST['desc_input']
    new_show = Show.objects.create(title = showTitle, release_date = showDate, description = showDesc, networks = network)
    #new_show.network.add(network)
    return redirect(request.META.get('HTTP_REFERER'))



def editshow(request):
    Shows= Show.objects.all()
    networks = Network.objects.all()

    context = {
        'Shows': Shows,
        'Networks': networks,
    }
    if request.POST['network_input'] == 'other':
        # en este caso hay que crearla
        new_network_name = request.POST['newNetwork']
        network = Network.objects.create(name = new_network_name)
    else:
        # en este caso hay que rescatarla de la DB
        network_id = request.POST['network_input']
        network = Network.objects.get(id=network_id)
    # -------

    showTitle = request.POST['title_input']
    showDate = request.POST['release_date_input']
    showDesc = request.POST['desc_input']
    new_show = Show.objects.create(title = showTitle, release_date = showDate, description = showDesc, networks = network)
    #new_show.network.add(network)
    return redirect(request.META.get('HTTP_REFERER'))


def tvshow(request, num):
    this_show = Show.objects.get(id= num)
    context = {
        
        'this_show': this_show,
    }
    
    return render(request, 'tv_show.html', context)


def delete(request, num):
    show_id= Show.objects.get(id= num)
    show_id.delete()
    return redirect('/shows')
    

def second(request, name):
    return HttpResponse('Hola ' + name)

