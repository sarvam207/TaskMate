from django.urls import path
from todolist_app import views

urlpatterns = [
    path('todo/', views.todolist, name='todolist'),                 # Home page for the task list
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # Route to delete a task
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'), # Route to edit a task
    path('mark_complete/<int:task_id>/', views.task_pending, name='task_pending'),  # Route to mark a task as complete
    path('mark_incomplete/<int:task_id>/', views.task_done, name='task_done'),  # Route to mark a task as incomplete
    path('contact/submit/', views.contact_form_submit, name='contact_submit'),

    # Add more paths as needed for additional views
]
