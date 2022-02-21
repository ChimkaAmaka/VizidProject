from django.shortcuts import render

from .models import Comment
#from .models import EmailPostForm, CommentForm

def home(request):
    return render(request,'home.html')

def room(request):
    return render(request,'rooms.html')
    
def Comment(request):
    return render(request,'comment.html')


def makepayment(request):
    return render(request,'makepayment.html')

def admin(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')


def about(request):
    return render(request,'about.html')


