from django.shortcuts import render
from .forms import Musician
# Create your views here.


def home(request): 
    # to remove id_ pref auto_id = True
    # label_suffix  = ''
    # initial = {key:value} default in form

    # orderring form field
    # fm.order_field(field_order=['last_name','first_name'])
    fm = Musician(auto_id=True ) 
    

    return render(request,'modelapp/home.html',{'form': fm})