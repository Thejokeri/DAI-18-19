
from django.shortcuts import render, HttpResponse
from .models import restaurantes # Coleccion
from .forms import SearchForm, AddForm, ModifyForm
from bson import ObjectId

# Create your views here.
def Index(request):
    context = {
      'navsearch': True,
      'form_search': SearchForm(),
      'form_add': AddForm()
    }
    return render(request, 'index.html', context)

def ProcesarLista(lista):
    for i in lista:
      i["id"] = i["_id"]
      del i["_id"]

def GetFind(request):
    if request.method == 'POST':
      
      form = SearchForm(request.POST)

      if form.is_valid():
        nombre = request.POST.get('restaurante')
      
        lista = list(restaurantes.find({"name": {'$regex': '^' + nombre}}).limit(10))
       
        if len(lista) != 0:

          ProcesarLista(lista)

          context = {
            'navsearch': True,
            'lista': lista,
            'form_search': SearchForm()
          }

          return render(request, 'find.html', context)
        else:
          context = {
            'navsearch': True,
            'noresult': True,
            'form_search': SearchForm()
          }

          return render(request, 'find.html', context)
      else:
        context = {
          'navsearch': True,
          'noresult': True,
          'form_search': SearchForm()
        }

        return render(request, 'find.html', context)
    else:
        return render(request, 'index.html', {'form_search': SearchForm()})

def GetAdd(request):

  if request.method == 'POST':

    form = AddForm(request.POST)

    if form.is_valid():
      nombre = request.POST.get('nombre')
      positionx = float(request.POST.get('locationx'))
      positiony = float(request.POST.get('locationy'))
      
      restaurantes.insert({"location":{"coordinates":[positionx,positiony],"type":"Point"},"name":nombre})

      context = {
        'navsearch': True,
        'success': True,
        'form_search': SearchForm(),
        'form_add': AddForm()
      }
        
      return render(request, 'add.html', context)
    else:
      context = {
        'navsearch': True,
        'form_search': SearchForm(),
        'form_add': AddForm()
      }

      return render(request, 'add.html', context)
  else:
      context = {
        'navsearch': True,
        'form_search': SearchForm(),
        'form_add': AddForm()
      }

      return render(request, 'add.html', context)

def GetSearch(request):
  if request.method == 'POST':
    get_find(request)
  else:
    return render(request, 'search.html', {'form_search': SearchForm()})

def GetModify(request):
  if request.method == 'POST':
    if request.POST.get('_method') == 'PUT':
      form = ModifyForm(request.POST)
      if form.is_valid():    
        id = ObjectId(request.POST.get('id'))
        nombre = request.POST.get('nombre')
        positionx = float(request.POST.get('locationx'))
        positiony = float(request.POST.get('locationy'))
      
        restaurantes.update({'_id':id}, {"location":{"coordinates":[positionx,positiony],"type":"Point"},"name":nombre})
        
        context = {
          'navsearch': True,
          'form_search': SearchForm(),
          'success': 'True'
        }

        return render(request, 'modify.html', context)
      else:
        context = {
          'navsearch': True,
          'form_search': SearchForm(),
          'nosuccess': 'True'
        }

        return render(request, 'modify.html', context)
    else:
      id = ObjectId(request.POST.get('id'))
        
      lista = list(restaurantes.find({"_id" : id}))
            
      ProcesarLista(lista)
        
      if len(lista) == 1:
        context = {
            'navsearch': True,
            'form_search': SearchForm(),
            'form': True,
            'form_modify': ModifyForm(),
            'lista': lista,
          }

        return render(request, 'modify.html', context)
      else:
        context = {
          'navsearch': True,
          'form_search': SearchForm(),
          'nosuccess': 'True',
        }
            
        return render(request, 'modify.html', context)

def GetDelete(request):
  if request.method == 'POST':
    if request.POST.get('_method') == 'DELETE':
      id = ObjectId(request.POST.get('id'))
          
      restaurantes.remove({"_id" : id},True)

      if len(list(restaurantes.find({"_id" : id}))) == 0:
        context = {
          'navsearch': True,
          'form_search': SearchForm(),
          'success': 'True',
        }
            
        return render(request, 'delete.html', context)
      else:
        context = {
          'navsearch': True,
          'form_search': SearchForm(),
          'nosuccess': 'True',
        }

        return render(request, 'delete.html', context)
    else:
      id = ObjectId(request.POST.get('id'))
      
      lista = list(restaurantes.find({"_id" : id}))
          
      ProcesarLista(lista)
      
      if len(lista) == 1:
        context = {
          'navsearch': True,
          'form_search': SearchForm(),
          'form': True,
          'lista': lista,
        }

        return render(request, 'delete.html', context)
      else:
        context = {
          'navsearch': True,
          'form_search': SearchForm(),
          'nosuccess': 'True',
        }
            
        return render(request, 'delete.html', context)