
from django.shortcuts import render
from django.http import HttpResponse
from .models import Topic,Webpage,AccessRecord
# Create your views here.

# def index(request):
#     return HttpResponse('Hello World!')

# def index(request):
#     my_dict = {'insert_me':"This message is brought to you by first app views.py"}
#     return render(request, 'first_app/index.html', context=my_dict)



def index(request):
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {"access_records":webpages_list}
    return render(request,'first_app/index.html',date_dict)