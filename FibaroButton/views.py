from django.shortcuts import render
from django.views import generic
from FibaroButton.models import Buttonlog
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from django.utils.decorators import method_decorator
#from django.views.generic import TemplateView, Formview

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


import requests
TOKEN="5227635927:AAEssMWPxPdAQ6fYj_vHG779j00rBL4UWLc"
chatid= "-674576833"

# Create your views here.
class NicetestListView(generic.ListView):
    model = Buttonlog
    template_name = "FibaroButton/buttonlog_list.html"
    context_object_name = 'button_log_list'

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):
        button = request.POST.get('button')
        value = request.POST.get('value')
        buttonlog= Buttonlog(button=button, value=value)
        buttonlog.save()
        #return HttpResponse(f'Hello, world! You sent {button}')

    #def get_queryset(self):
    #    """Return the last five published questions."""
    #    return Buttonlog.objects.all()



def AddViews(request):
    if request.method == 'POST':
        # Leggi i dati della richiesta POST
        post_data = request.POST
        # Esempio di come accedere ai dati della richiesta POST
        button = post_data.get('button')
        value = post_data.get('value')

        # Restituisci una risposta HTTP con i dati letti dalla richiesta POST
        return HttpResponse(f"Il nome è {button}, il cognome è {value}")
    else:
        return HttpResponse('GET request processed.')




class AddView(APIView):

    template_name = "nicetest/bl.html"

    @method_decorator(csrf_exempt)
    def post(self, request, *args, **kwargs):

        data = request.data
        button = data['button']
        value = data['value']
        buttonlog= Buttonlog(button=button, value=value)
        buttonlog.save()

        str="button {}, value {}".format(button,value)
        url="https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}".format(TOKEN,chatid,str)
        response = requests.get(url)
        return HttpResponse(f'Hello, world! You sent {str}')

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, world2!')


def Nicetestbuttonstatus(request):

    button_1v = Buttonlog.objects.filter(button='button 1').latest('created_at').value
    button_2v = Buttonlog.objects.filter(button='button 2').latest('created_at').value
    button_3v = Buttonlog.objects.filter(button='button 3').latest('created_at').value
    button_4v = Buttonlog.objects.filter(button='button 4').latest('created_at').value
    button_5v = Buttonlog.objects.filter(button='button 5').latest('created_at').value
    button_6v = Buttonlog.objects.filter(button='button 6').latest('created_at').value

    return render(request, 'FibaroButton/button_status.html',
        {'button_1': button_1v, 'button_2': button_2v,
        'button_3': button_3v, 'button_4': button_4v,
        'button_5': button_5v, 'button_6': button_6v}
    )