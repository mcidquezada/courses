from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import Course

# INDEX
def index(request):
    context = {
        'courses' : Course.objects.all()
    }

    if request.method == 'GET':
        return render(request, 'index.html', context)
    
    if request.method == 'POST':
        print(request.POST)
        errors= Course.objects.validator(request.POST)

        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect ("/")
        
        else:
            Course.objects.create(
                name = request.POST['name'],
                desc = request.POST['desc']
                )
            return redirect ("/")
    

def delete(request,id):
    context = {
        'course' : Course.objects.get(id=id)
    }
    Course.objects.get(id=id).delete()
    return redirect ("/")