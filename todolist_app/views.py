from django.http import HttpResponse
from django.shortcuts import render, redirect
from todolist_app.models import Task
from todolist_app.forms import TaskForm
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.contrib import messages
# Create your views here.
@login_required
def todolist(request):

    if request.method == "POST":
        form = TaskForm(request.POST or None)
        if form.is_valid():
            form.save(commit=False).active_user = request.user
            form.save()
            messages.success(request, "New Task Added Successfully!")
        return redirect('todolist')
    else:
        all_tasks = Task.objects.filter(active_user=request.user)  # Fetch all tasks from the database
        paginator = Paginator(all_tasks, 5)  # Show 5 tasks per page
        page_number = request.GET.get('page')
        all_tasks = paginator.get_page(page_number)
        return render(request, 'todolist.html', {'variable_key': "Welcome to todo list", 'all_tasks': all_tasks})

def contact(request):
    return render(request, 'contact.html', {'variable_key': "welcome to contact"})

def index(request):
    return render(request, 'index.html', {'variable_key': "Welcome to TaskMate"})


def about(request):
    return render(request, 'about.html', {'variable_key': "welcome to about"})

@login_required
def delete_task(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.active_user == request.user:
        # Only delete the task if the user is the active user of the task
        task.delete()
        messages.success(request, "Task Deleted!")
    else:
        messages.error(request, "You do not have permission to delete this task.")
    # Redirect to the todolist view after deletion
    return redirect('todolist')

@login_required
def edit_task(request, task_id):
    task = Task.objects.get(id=task_id) 
    if request.method == "POST":
        form = TaskForm(request.POST or None, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, "Saved Changes Successfully!")
        return redirect('todolist')
    else:
        return render(request, 'edit_task.html', {'task': task})

@login_required    
def task_done(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.active_user == request.user:
        # Only mark the task as complete if the user is the active user of the task
        task.completed = True
        task.save()
        messages.success(request, "Congrats! Task Completed!")
    else:
        messages.error(request, "You do not have permission to mark this task as done.") 
    return redirect('todolist')

@login_required
def task_pending(request, task_id):
    task = Task.objects.get(id=task_id)
    if task.active_user == request.user:
        # Only mark the task as incomplete if the user is the active user of the task
        task.completed = False
        task.save()
    else:
        messages.error(request, "You do not have permission to mark this task as pending.")
    return redirect('todolist')