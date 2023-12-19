from django.shortcuts import render,redirect
from . models import Todotable
from django.urls import reverse_lazy
from . forms import TodoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView

class Tasklv(ListView):
    model = Todotable
    template_name = 'home.html'
    context_object_name = 'task'

class Taskdv(DetailView):
     model = Todotable
     template_name = 'detail.html'
     context_object_name = 'task'

class Taskuv(UpdateView):
    model = Todotable
    template_name = 'update.html'
    context_object_name = 'task'
    fields = ('name','priority','date')

    def get_success_url(self):
        return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class TaskDelV(DeleteView):
    model = Todotable
    template_name = 'delete.html'
    success_url = reverse_lazy('tasklv')

# Create your views here.
def homepage(request):
    task = Todotable.objects.all()
    if request.method =="POST":
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        todo = Todotable(name=name,priority=priority,date=date)
        todo.save()
        
    return render(request,'home.html',{'task':task})

def done(request,taskid):
    task = Todotable.objects.get(id=taskid)
    if request.method =="POST":
        task.delete()
        return redirect('/')
    return render(request,'done.html')

def edit(request,form_id):
    task = Todotable.objects.get(id=form_id)
    form = TodoForm(request.POST or None, instance = task)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'task':task})