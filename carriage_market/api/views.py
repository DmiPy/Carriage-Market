from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def main(request):
#     return render(request, 'index.html')
    return HttpResponse("<h1>Hello!dsfsfds</h1>")