
from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView
from .models import restaurants, platos # Coleccion
from django.http import JsonResponse
from .forms import SearchForm, AddFormRestaurant, ModifyFormRestaurant, AddFormPlate, ModifyFormPlate
import json
from django.core import serializers

class Home(TemplateView):
    template_name = 'home.html'

def Index(request):
    context = {
        'navsearch': True,
        'form_search': SearchForm(),
        'form_add': AddFormRestaurant()
    }
    return render(request, 'index.html', context)

################################# Funciones relacionadas con los restaurantes #################################

def DictRestaurantes(lista):
    dict = {}
    n = 10
    tam = int(len(lista) / n)

    for i in range(1,tam):
        dict[i] = lista[i:i + n]

    return dict

def reclama_datos(request):
    global d

    if d:
        datos = json.dumps(d)

    return JsonResponse(datos,safe=False)

def FindRestaurant(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            nombre = request.POST.get('restaurante')
            nombre = nombre.capitalize()
            lista = list(restaurants.objects(name__startswith=nombre))
        
            if len(lista) != 0:
                global d
                
                for i in range(0,len(lista)):
                    lista[i] = lista[i].to_json()

                d = DictRestaurantes(lista)
                keys = list(d.keys())[:4]

                context = {
                    'navsearch': True,
                    'd': keys,
                    'form_search': SearchForm()
                }

                return render(request, './restaurante/find.html', context)
            else:
                context = {
                    'navsearch': True,
                    'noresult': True,
                    'form_search': SearchForm()
                }

                return render(request, './restaurante/find.html', context)
        else:
            context = {
                'navsearch': True,
                'noresult': True,
                'form_search': SearchForm()
            }

            return render(request, './restaurante/find.html', context)
    else:
        valor = var
        keys = list(d.keys())[valor:valor+4]

        context = {
            'navsearch': True,
            'lista': d[valor],
            'd': keys,
            'form_search': SearchForm()
        }

        return render(request, './restaurante/find.html', context)

def AddRestaurant(request):
    if request.method == 'POST':
        form = AddFormRestaurant(request.POST)
        if form.is_valid():
            nombre = request.POST.get('nombre')
            positionx = float(request.POST.get('locationx'))
            positiony = float(request.POST.get('locationy'))
            
            restaurante = restaurants(name=nombre, location=[positionx,positiony])
            restaurante.save()

            context = {
                'navsearch': True,
                'success': 'True',
                'form_search': SearchForm(),
            }
                
            return render(request, './restaurante/add.html', context)
        else:
            context = {
                'navsearch': True,
                'form_search': SearchForm(),
                'nosuccess': 'True',
                'form_add': AddFormRestaurant(),
            }

            return render(request, './restaurante/add.html', context)
    else:
        context = {
            'navsearch': True,
            'form_search': SearchForm(),
            'form_add': AddFormRestaurant()
        }

        return render(request, './restaurante/add.html', context)

def SearchRestaurant(request):
    if request.method == 'POST':
        get_find(request)
    else:
        return render(request, './restaurante/search.html', {'form_search': SearchForm()})

def ModifyRestaurant(request):
    if request.method == 'POST':
        if request.POST.get('_method') == 'PUT':
            form = ModifyFormRestaurant(request.POST)
            if form.is_valid():    
                id = request.POST.get('id')
                nombre = request.POST.get('nombre')
                positionx = float(request.POST.get('locationx'))
                positiony = float(request.POST.get('locationy'))

                restaurante = restaurants.objects(pk=id)[0]
                restaurante.name = nombre
                restaurante.location = [positionx,positiony]
                restaurante.save()

                context = {
                    'navsearch': True,
                    'form_search': SearchForm(),
                    'success': 'True'
                }

                return render(request, './restaurante/modify.html', context)
            else:
                id = request.POST.get('id')
                name = request.POST.get('nombre')

                context = {
                    'navsearch': True,
                    'form_search': SearchForm(),
                    'nosuccess': 'True',
                    'form': True,
                    'form_modify': ModifyFormRestaurant(initial={'nombre': name}),
                    'id': id,
                }

                return render(request, './restaurante/modify.html', context)
        else:
            id = request.POST.get('id')
            name = request.POST.get('nombre')
                
            context = {
                'navsearch': True,
                'form_search': SearchForm(),
                'form': True,
                'form_modify': ModifyFormRestaurant(initial={'nombre': name}),
                'id': id,
            }

            return render(request, './restaurante/modify.html', context)

def DeleteRestaurant(request):
    if request.method == 'POST':
        if request.POST.get('_method') == 'DELETE':
            id = request.POST.get('id')
                
            restaurante = restaurants.objects(pk=id)[0]
            plato = platos.objects(restaurante=id)
            for i in plato:
                plato.delete()
            restaurante.delete()
            restaurante.save()

            context = {
                'navsearch': True,
                'form_search': SearchForm(),
                'success': 'True',
            }
                
            return render(request, './restaurante/delete.html', context)
        else:
            id = request.POST.get('id')
            name = request.POST.get('nombre')
                
            context = {
                'navsearch': True,
                'form_search': SearchForm(),
                'form': True,
                'name': name,
                'id': id,
            }

            return render(request, './restaurante/delete.html', context)
      

###################################################################################################

def ListPlate(request):
    if request.method == 'POST':
        id = request.POST.get('id')

        nombre = restaurants.objects(pk=id)[0].name
        listaplatos = list(platos.objects(restaurante=id))

        if len(listaplatos) != 0:
            context = {
                'navsearch': True,
                'form_search': SearchForm(),
                'lista': listaplatos,
                'id': id,
                'name': nombre,
            }
            return render(request, './plato/list.html', context)
        else:
            context = {
                'navsearch': True,
                'form_search': SearchForm(),
                'noresult': True,
                'id': id,
                'name': nombre,
            }
            return render(request, './plato/list.html', context)
    else:
        return render(request, 'index.html')

def AddPlate(request):
    if request.method == 'POST':
        form = AddFormPlate(request.POST)
        if form.is_valid():
            restaurante = request.POST.get('id')
            nombre = request.POST.get('nombre')
            tipoCocina = request.POST.get('tipocomida')
            alergeno = request.POST.getlist('alergenos')
            precio = float(request.POST.get('precio'))

            plato = platos(restaurante=restaurante, nombre=nombre, tipoCocina=tipoCocina, alergenos=alergeno, precio=precio)
            plato.save()
            
            context = {
                'navsearch': True,
                'success': 'True',
                'form_search': SearchForm(),
            }

            return render(request, './plato/add.html', context)
        else:
            id = request.POST.get('id')
            nombre = request.POST.get('nombrerestaurante')

            context = {
                'navsearch': True,
                'form_search': SearchForm(),
                'namerestaurante': nombre,
                'id': id,
                'nosuccess': 'True',
                'form_add': AddFormPlate(),
            }
            
            return render(request, './plato/add.html', context)
    else:
        id = request.GET.get('id')
        nombre = request.GET.get('nombrerestaurante')
        
        context = {
            'navsearch': True,
            'namerestaurante': nombre,
            'id': id,
            'form_search': SearchForm(),
            'form_add': AddFormPlate()
        }
        
        return render(request, './plato/add.html', context)

def ModifyPlate(request):
    if request.method == 'POST':
        if request.POST.get('_method') == 'PUT':
            form = ModifyFormPlate(request.POST)
            if form.is_valid():
                idplato = request.POST.get('idplato')
                nombre = request.POST.get('nombre')
                tipoCocina = request.POST.get('tipocomida')
                alergeno = request.POST.getlist('alergenos')
                precio = float(request.POST.get('precio'))

                plato = platos.objects(pk=idplato)[0]
                plato.nombre = nombre
                plato.tipoCocina = tipoCocina
                plato.alergenos = alergeno
                plato.precio = precio
                plato.save()

                context = {
                    'navsearch': True,
                    'form_search': SearchForm(),
                    'success': 'True'
                }
                
                return render(request, './plato/modify.html', context)
            else:
                idplato = request.POST.get('idplato')
                idrestaurante = request.POST.get('idrestaurante')
                nombre = request.POST.get('nombre')
                tipococina = request.POST.get('tipococina')

                context = {
                    'navsearch': True,
                    'form_search': SearchForm(),
                    'nosuccess': 'True',
                    'form': True,
                    'form_modify': ModifyFormPlate(initial={'nombre': nombre, 'tipocomida': tipococina}),
                    'idplato': idplato,
                    'idrestaurante': idrestaurante,
                }

                return render(request, './plato/modify.html', context)
        else:
            idplato = request.POST.get('idplato')
            idrestaurante = request.POST.get('idrestaurante')
            nombre = request.POST.get('nombreplato')
            tipococina = request.POST.get('tipococina')

            context = {
                'navsearch': True,
                'form_search': SearchForm(),
                'form': True,
                'form_modify': ModifyFormPlate(initial={'nombre': nombre, 'tipocomida': tipococina}),
                'idplato': idplato,
                'idrestaurante': idrestaurante,
            }

            return render(request, './plato/modify.html', context)

def DeletePlate(request):
    if request.method == 'POST':
        if request.POST.get('_method') == 'DELETE':
            id = request.POST.get('id')

            plato = platos.objects(pk=id)[0]
            plato.delete()
            plato.save()

            context = {
                'navsearch': True,
                'form_search': SearchForm(),
                'success': 'True',
            }
                
            return render(request, './plato/delete.html', context)
        else:
            id = request.POST.get('idplato')
            name = request.POST.get('nombre')
                
            context = {
                'navsearch': True,
                'form_search': SearchForm(),
                'form': True,
                'name': name,
                'id': id,
            }

            return render(request, './plato/delete.html', context)