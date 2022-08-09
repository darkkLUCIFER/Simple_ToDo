from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import NewTodoForm, UpdateTodoForm
from .models import ToDo


def home(request):
    todo = ToDo.objects.all()
    return render(request, 'home/home.html', {'todo': todo})


def todo_detail(request, pk):
    detail = ToDo.objects.get(id=pk)
    return render(request, 'home/detail.html', {'detail': detail})


def todo_delete(request, pk):
    ToDo.objects.get(id=pk).delete()
    messages.success(request, 'تسک موردنظر شما با موفقیت حذف شد.', extra_tags='success')
    return redirect('home:home')


def todo_create(request):
    if request.method == "POST":
        form = NewTodoForm(data=request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            title = cd['title']
            body = cd['body']
            created = cd['created']
            ToDo.objects.create(title=title, body=body, created=created)
            messages.success(request, 'تسک جدید با موفقیت ایجاد شد.', extra_tags='success')
            return redirect('home:home')
    else:
        form = NewTodoForm()
    return render(request, 'home/new_todo.html', {'form': form})


def update_todo(request, pk):
    todo = ToDo.objects.get(id=pk)
    if request.method == "POST":
        form = UpdateTodoForm(data=request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, 'تسک مورد نظر شما با موفقیت تغییر یافت.', extra_tags='success')
            return redirect('home:detail', pk)
    else:
        form = UpdateTodoForm(instance=todo)
    return render(request, 'home/update_todo.html', {'form': form})
