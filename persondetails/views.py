from django.shortcuts import render

# Create your views here.


def person_list(request):
    return render(request, 'persondetails/person_list.html')
