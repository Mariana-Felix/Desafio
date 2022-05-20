from datetime import datetime
import os
from django.http import HttpResponse
from django.shortcuts import render
from django.template import Template, Context
from django.template import loader

def list_family (self):

    miHtml = open ('/Users/marianafelix/Documents/Python/Desafio/challenger/challenger/templates/template.html')
    template = Template (miHtml.read())
    miHtml.close ()

    context_dict = {
        'family':[
            {
        'name': 'pepe','last_name': 'fulano','dni':1234556,'birthday': datetime.now()
        },{
        'name': 'pepe2',
        'last_name': 'fulano',
        'dni':1234556,
        'birthday': datetime.now()
        },{
        'name': 'pep3',
        'last_name': 'fulano',
        'dni':1234556,
        'birthday': datetime.now()
        }]
    }
    my_context = Context (context_dict)
    render = template.render (my_context)
    return HttpResponse (render)