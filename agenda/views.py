from django.shortcuts import render
from django.urls import reverse_lazy

# Create your views here.
from .models import Agenda
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .forms import AgendaForm
from django.contrib.auth.forms import UserCreationForm


class AgendaListView(ListView):       
    context_object_name = 'contactos'
    template_name = 'agenda/home.html'
    paginate_by = 10

    def get_queryset(self):
        return Agenda.objects.filter(creador= self.request.user.id)


class AgendaCreateView(CreateView): 
    form_class = AgendaForm
    template_name = 'agenda/create.html'
    success_url = reverse_lazy('home')

class AgendaUpdateView(UpdateView):
    model = Agenda
    form_class = AgendaForm
    template_name = 'agenda/update.html'
    success_url = reverse_lazy('home')

class AgendaDeleteView(DeleteView):
    model = Agenda
    template_name = 'agenda/delete.html'
    success_url = reverse_lazy('home')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('home')
    template_name = 'registration/signup.html'