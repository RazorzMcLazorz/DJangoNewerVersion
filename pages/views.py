from django.shortcuts import render

# Create your views here.
# creates a new page
def home(request):
    return render(request, "home.html", {})

def about(request):
    from pages.namer import namer
    return render(request, "about.html", {"my_stuff": namer})

def contact(request):
    return render(request, "contact.html", {})