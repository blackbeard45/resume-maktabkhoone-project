from django.shortcuts import render

# Create your views here.
def home_1_view(request):
    return render(request, 'resume/home-1.html')

def contact_view(request):
    return render(request, 'resume/contact.html')
