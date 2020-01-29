from django.shortcuts import render


# Create your views here.
def home(request):
    # api-key: pk_40d960e9e11f47419c47ed2a9de813c9
    return render(request,'home.html',{})

def about(request):
    return render(request,'about.html',{})
