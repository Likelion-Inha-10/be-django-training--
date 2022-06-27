from django.shortcuts import render, redirect
from .models import board
from board.models import board
from .forms import addPostForm
# Create your views here.

def index(request):
    board_list = board.objects.all().order_by('-id')
    context = {'board_list':board_list}
    return render(request, 'board/index.html', context)

def addPost(request):
    if request.method == 'POST':
        form = addPostForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('board:index')
    else:
        form = addPostForm()
    context = {'form':form,}
    return render(request, 'board/addPost_form.html', context)