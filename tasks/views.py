from django.shortcuts import render
from django import forms

# Create your views here.

tasks = ["food", "barbor", "pizza"]

class NewTaskForm(forms.Form):
    task = form.CharField(label="New Task")

def index(request):
    return render(request, 'tasks/index.html', {
        "tasks": tasks
    })

def add(request):
    return render(request, "tasks/add.html", {
        "form": "NewTaskform()"
    })