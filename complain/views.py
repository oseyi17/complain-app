from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, TemplateView
from django.shortcuts import render
from django.views.generic.edit import CreateView, DeleteView
from django.urls import reverse_lazy
from .models import Complain, Bug
from django import forms
from .forms import ComplainForm, BugForm 
from django.db.models import Count


class HomePageView(LoginRequiredMixin, ListView):
    model = Complain
    template_name = 'list.html'
    context_object_name = 'complains'
    paginate_by = 5


class DetailPageView(LoginRequiredMixin, DetailView):
    model = Complain
    template_name = 'detail.html'

class ComplainView(CreateView):
    form_class = ComplainForm
    model = Complain
    template_name = 'complain.html'    

@login_required
def dashboard(request):
    titles = Complain.objects.values('title').annotate(count=Count('title')).order_by('title')
    context = {'titles':titles}
    context_object_name = 'titles'
    return render(request, 'dashboard.html',context)

def thanks(request):
    return render(request, 'thanks.html')

class bug(CreateView):
    form_class = BugForm
    model = Bug
    template_name = 'bug_report.html'
    success_url= reverse_lazy('thanks')


class DeletePageView(DeleteView):
    model = Complain
    template_name = 'delete.html'
    success_url= reverse_lazy('list')

