from django.http import HttpResponse
from django.template import Template, Context
from django.shortcuts import render

def categories(request):
    with open("pages/categorias.html") as categoriaHTML:
        template = Template(categoriaHTML.read())
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

def posts(request):
    with open("pages/post.html") as categoriaHTML:
        template = Template(categoriaHTML.read())
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)

def socialmedia(request):
    with open("pages/socialmedia.html") as categoriaHTML:
        template = Template(categoriaHTML.read())
    contexto = Context()
    documento = template.render(contexto)
    return HttpResponse(documento)
