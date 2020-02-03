from django.shortcuts import render


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
