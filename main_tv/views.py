from django.shortcuts import render, redirect, HttpResponse
from main_tv.models import Show, Network
from django.contrib import messages

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



def editshow(request, num):
    if request.method== 'GET':
        edit_show = Show.objects.get(id= num)
        # yo no tuve ese problema, pero en caso de que me de jugo la fecha hago lo siguiente:
        time_str=edit_show.release_date.strftime('%Y-%m-%d')
        Networks= Network.objects.all()
        
        context = {
            'edit_show': edit_show,
            'time_str':time_str,
            'network': Networks
        }
        return render(request,'shows_edit.html',  context)
    else:
        # en este caso hay que rescatarla de la DB
        edit_show = Show.objects.get(id= num)
        network_id= int(request.POST['network_input'])
        network = Network.objects.get(id=network_id)
    # -------
        showTitle = request.POST['title_input']
        showDate = request.POST['release_date_input']
        showDesc = request.POST['desc_input']
        new_show = Show.objects.update_or_create(title = showTitle, release_date = showDate, description = showDesc, networks = network)
        #new_show.network.add(network)
        return redirect('/shows')


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

