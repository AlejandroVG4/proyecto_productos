from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Productos
from django.views.decorators.csrf import csrf_exempt
import json
from django.template import loader


# Create your views here.

@csrf_exempt
def index(request, id=None):
    if request.method == 'GET':
        # if id:
            
        #     # id_producto es el nombre que está en el modelo
        #     producto = Productos.objects.get(id_producto=id)
            
        #     return JsonResponse(data={"mensaje": "ok",
        #                               "id": producto.id_producto,
        #                               "name": producto.nombre,
        #                               "price": producto.precio,
        #                               "stock": producto.unidades})                 
                             
        # else:
        #     productos = list(Productos.objects.all().values('id_producto', 
        #                                                     'nombre',
        #                                                     'precio',
        #                                                     'unidades'))
            
        #     return JsonResponse(data={"mensaje": "ok", 
        #                               "productos": productos})
        
        lista_productos = Productos.objects.all()
        template = loader.get_template('productos/index.html')
        mensaje = {"lista_productos": lista_productos}
        return HttpResponse(template.render(mensaje, request))
        
        #return HttpResponse(productos)

    #return HttpResponse("Hola estoy en la vista productos")
    
    if request.method == 'POST':
        body = request.body.decode('UTF-8')
        request_body = json.loads(body)
        
        producto = Productos.objects.create(
            id_producto = request_body['id_producto'],
            nombre = request_body['nombre'],
            precio = request_body['precio'],
            unidades = request_body['unidades']
        )
        
        return JsonResponse(data={'message': 'Ok', 
                                  'id': producto.id_producto, 
                                  'name': producto.nombre, 
                                  'price': producto.precio, 
                                  'stock': producto.unidades})
        
        
    if request.method == 'DELETE':
        
        # body = request.body.decode('UTF-8')
        # request_body = json.loads(body)
        # eliminar_elemento = Productos.objects.filter(id_producto=request_body['id_producto'])
        # eliminar_elemento.delete()
        
        Productos.objects.filter(id_producto=id).delete()
        
        return JsonResponse(data={'message': 'Elemento eliminado'})

        # Productos.objects.all().delete()
        
    if request.method == 'PUT':
        
        body = request.body.decode('UTF-8')
        request_body = json.loads(body)
                
        Productos.objects.filter(id_producto=id).update(
            
            nombre = request_body['nombre'],
            precio = request_body['precio'],
            unidades = request_body['unidades']
            
        )
        
        return JsonResponse(data={'message': 'Elemento modificado'})

    if request.method == 'PATCH':
        if id:
            Productos.objects.filter(id_producto=id).update(nombre="Revolcon")
            return JsonResponse(data={"message": "Producto con id = " + str(id) + " actualizado."})
        
    return HttpResponse("Metodo no disponible", status=405)