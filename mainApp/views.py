from django.http import HttpResponse
from django.shortcuts import render
from sacco.models import Customer, Deposit


# Create your views here.
def test(request):
    #save a customer
    # c1 = Customer(first_name='Saida', last_name='Ali',
    #               email='saida@x.com', dob='2000-11-28', gender='Female', weight=62)
    # c1.save()
    #
    # c2 = Customer(first_name='Jake', last_name='Juma',
    #               email='juma@x.com', dob='1999-11-28', gender='Male', weight=62)
    # c2.save()
    customer_count = Customer.objects.count()
    # fetching one customer
    c1 = Customer.objects.get(id=1) # select * from customers where id=1
    print(c1)
    d1 = Deposit(amount=1000, status=True, customer=c1)
    d1.save()
    deposit_count = Deposit.objects.count()
    return HttpResponse(f"Ok, Done, We have {customer_count} customers and {deposit_count} deposits")

# http://localhost:8000/
# http://localhost:8000/test
# python manage.py runserver 8001

