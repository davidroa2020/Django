from cgitb import html
from re import template
from urllib import request
#from http.client import HTTPResponse
#from xml.dom.minidom import Document
from django.http import HttpResponse
from datetime import *
from django.template import Template, Context

def saludo(request):

    doc_externo = open("C:/Users/david/OneDrive/PYTHON/Django/proyecto_1/Inicio.html")
    plt=Template(doc_externo.read())
    doc_externo.close() 
    ctx=Context()
    documento =plt.render(ctx)
    return HttpResponse(documento)


def despedida(request):
    
    doc_externo = open("C:/Users/david/OneDrive/PYTHON/Django/proyecto_1/Inicio.html")
    plt=Template(doc_externo.read())
    doc_externo.close() 
    ctx=Context()
    documento =plt.render(ctx)
    return HttpResponse(documento)

def fechadame(request):
    fecha_actual= datetime.now()
    html_ = """<html>
                    <body>
                        <h1>
                            hola %s
                        </h1>
                        </body>
                    </html>
                    """ % fecha_actual
    
    return HttpResponse(html_)

def calculaEdad(request, agno):

    edadActual = 24
    periodo = agno - 2022
    edadFutura= edadActual + periodo
    html_ = """<html>
                <body>
                    <h2>
                        en el año %s tendrás %s
                    </h2>
                    </body>
                </html>
                """ % (agno, edadFutura)
    return HttpResponse(html_)

def calculaEdad2(request, edadActual, agno):

    #edadActual = 24
    periodo = agno - 2022
    edadFutura= edadActual + periodo
    html_ = """<html>
                <body>
                    <h2>
                        en el año %s tendrás %s
                    </h2>
                    </body>
                </html>
                """ % (agno, edadFutura)
    return HttpResponse(html_)