from django.shortcuts import render,redirect
from .models import Stock
from django.contrib import messages
from .forms import StockForm

# Create your views here.
def home(request):
    import requests
    import json

    if request.method == 'POST':
        ticker=request.POST['ticker']
        api_request = requests.get("https://cloud.iexapis.com/stable/stock/"+ ticker +"/quote?token=pk_40d960e9e11f47419c47ed2a9de813c9")

        try:
            api = json.loads(api_request.content)
        except Exception as e:
            api = "Error..."
        # api-key: pk_40d960e9e11f47419c47ed2a9de813c9

        return render(request,'home.html',{ 'api' : api })
        
    else:
        return render(request,'home.html',{ 'ticker' : "Enter a ticker symbol above..." })


def about(request):
    return render(request,'about.html',{})

def add_stock(request):
    if request.method=='POST':
        form=StockForm(request.POST or None)

        if form.is_valid():
            form.save()
            messages.success(request,("Stock has been added "))
            return redirect('add_stock')



    else:    
        ticker=Stock.objects.all()
        return render(request,'add_stock.html',{ 'ticker':ticker })
