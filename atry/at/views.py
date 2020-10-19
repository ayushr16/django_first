from django.shortcuts import render

# Create your views here.
def index(request):
    my_dict = {'text':'Ayush Ranjan','number':100}
    return render(request,'at/home.html',my_dict)

def detective(request):
    return render(request,'at/detective.html')

def help(request):
    return render(request,'at/help.html')
