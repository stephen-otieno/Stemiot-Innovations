from django.shortcuts import render
from stemiotApp.models import Client

# Create your views here.

def index(request):
    return render(request, 'index.html')


def client_details(request):
    if request.method == "POST":
        client_name = request.POST.get('client_name')
        client_email = request.POST.get('client_email')
        client_phone = request.POST.get('client_phone')
        client_message = request.POST.get('client_message')

        client =Client (
            client_name = client_name,
            client_email = client_email,
            client_phone = client_phone,
            client_message = client_message,


        )
        client.save()
    return render(request, template_name="index.html")
