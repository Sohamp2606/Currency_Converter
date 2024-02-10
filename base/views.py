from django.shortcuts import render,redirect
from forex_python.converter import CurrencyRates


# Create your views here.
def home(request):
    converted_amt=None
    if request.method == 'POST':
        source_currency = request.POST.get('source_currency')
        target_currency = request.POST.get('target_currency')    
        amount = float(request.POST.get('amount'))
        
        c = CurrencyRates()
        exchange_rate = c.get_rate(source_currency,target_currency)
        converted_amt = round(amount*exchange_rate,2)
        print(c,exchange_rate,converted_amt)
        
    return render(request,'home.html',{'converted_amt':converted_amt})