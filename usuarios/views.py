from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Usuarios
from django.views.decorators.csrf import csrf_exempt
import json
from django.template import loader
from django.core.exceptions import ObjectDoesNotExist

# Create your views here.

def users_list(request):
    if request.method == "GET":
        lista_usuarios = Usuarios.objects.all()
        template = loader.get_template('usuarios/index.html')
        mensaje = {"lista_usuarios": lista_usuarios}
        return HttpResponse(template.render(mensaje, request))
    
    return HttpResponse("Method not allowed", status=405)

def user_detail(request, username):
    if request.method == "GET":
        try:
            usuario = Usuarios.objects.get(username=username)
            return JsonResponse(data={"nombre": usuario.username,
                                    "email": usuario.email,
                                    "direccion": usuario.direccion,
                                    "pais": usuario.pais})
            
        except Usuarios.DoesNotExist:
            return JsonResponse(data={"error": "Usuario no encontrado"}, status=404)
        
    return HttpResponse("Method not allowed", status=405)
    

@csrf_exempt
def create_user(request):
    if request.method == "POST":
        # Getting data
        decoded_body = request.body.decode('UTF-8')
        body = json.loads(decoded_body)

        # Data validation
        errors = []
        if body['username'] == "":
            errors.append({'username': 'username cannot be empty'})

        if any(caracter.isdigit() for caracter in body['pais']):  # TODO: Validate country format
            errors.append({'pais': 'El pais no puede tener numeros'})

        if "@" not in body['email']:  # TODO: Validate email format
            errors.append({'email': 'Incorrect email format'})

        if len(errors) > 0:
            return JsonResponse({'errors': errors}, status=400)

        # Saving data in DB:
        user = Usuarios.objects.create(
            username=body['username'],
            password=body['password'],
            email=body['email'],
            direccion=body['direccion'],
            pais=body['pais']
        )

        return JsonResponse(data={'message': 'Created user', 'id': user.id, 'username': user.username})

    return HttpResponse("Method not allowed", status=405)

@csrf_exempt
def update_user(request, username):
    if request.method == "PUT":
        body = request.body.decode('UTF-8')
        request_body = json.loads(body)
        
        new_username = request_body.get('username', '').strip()
        email = request_body.get('email', '').strip()
        pais = request_body.get('pais', '').strip()
        
        if new_username == "":
            return JsonResponse(data={'error': 'El campo no puede estar vacio'}, status=400)
        
        if '@' not in email:
            return JsonResponse(data={'error': 'El campo debe tener un "@"'}, status=400)
        
        if any(caracter.isdigit() for caracter in pais):
            return JsonResponse(data={'error': 'El pais no puede contener numeros'}, status=400)
        
        usuario = Usuarios.objects.filter(username=username)
        
        if not usuario.exists():
            return JsonResponse(data={'error': "Usuario no encontrado"}, status=404)
        
        usuario.update(
            username = new_username,
            password = request_body['password'],
            email = email,
            direccion = request_body['direccion'],
            pais = pais
        )
        
        return JsonResponse(data={'message': 'Elemento modificado'})
        
    return HttpResponse("Method not allowed", status=405)

@csrf_exempt
def update_user_details(request, username):
    if request.method == "PATCH":
        body = request.body.decode('UTF-8')
        request_body = json.loads(body)
        
        new_username = request_body.get('username', '').strip()
        
        if new_username == "":
            return JsonResponse(data={'error': 'El nuevo nombre no puede estar vacio'}, status=400)
        
        usuario = Usuarios.objects.filter(username=username)
        
        if not usuario.exists():
            return JsonResponse(data={'error': "Usuario no encontrado"}, status=404)
        
        usuario.update(username=new_username)
        
        return JsonResponse(data={"message": "Usuario de nombre = " + username + " actualizado."})
    
    return HttpResponse("Method not allowed", status=405)

@csrf_exempt
def delete_user(request, username):
    if request.method == "DELETE":
        usuario = Usuarios.objects.filter(username=username)
        if not usuario.exists():
             return JsonResponse(data={'error': "Usuario no encontrado"}, status=404)

        usuario.delete()
        return JsonResponse(data={"message": "Usuario eliminado"})
    
    return HttpResponse("Method not allowed", status=405)