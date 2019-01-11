from django.shortcuts import render

# Create your views here.

# This method is going to display the details of the person
def person_list(request):
    return render(request, 'persondetails/person_list.html')
