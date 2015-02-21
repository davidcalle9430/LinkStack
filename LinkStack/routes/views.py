from django.shortcuts import render
from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404
from .models import Route 
from links.models import Link
from django import forms
from django.forms import ModelForm
from django.shortcuts import redirect

def route_view(request, route_name):
    
    if request.method == 'POST':
        route= "/" + route_name
        form = LinkForm(request.POST)
        if form.is_valid():
            temporal_route= Route.objects.get(name=route_name)
            p_link= form.cleaned_data['link']
            p_description = form.cleaned_data['description']
            link= Link.create(p_link,p_description, temporal_route)
            link.save()
            return redirect(route)

    else:
        try:
            route= Route.objects.get(name=route_name)
        except Route.DoesNotExist:
            raise Http404
        links = route.link_set.all()
        creation_form = LinkForm()
        dictionary= {
        'route':route,
        'links':links,
        'form':creation_form,
        }
        return render(request,'route.html',dictionary)

def create_route(request):
    if request.method == 'POST':
        print "post"
        form = RouteForm(request.POST)
        if form.is_valid():
            print "No existe"
            route = Route.create(form.cleaned_data['name'], form.cleaned_data['insertion_password'], form.cleaned_data['deletion_password'], form.cleaned_data['user_email'])
            route.save()
            return redirect("/"+route.name)
        else:
            return HttpResponse('Lo sentimos, este nombre ya ha sido utilizado')
    else:
        form = RouteForm()
        dictionary ={
        'form': form
        }
        return render(request,'home.html',dictionary)

class LinkForm(forms.ModelForm):
    class Meta:
        model = Link
        fields = ['link','description']

class RouteForm(forms.ModelForm):
    class Meta:
        model = Route
        fields = ['name', 'insertion_password','deletion_password','user_email']
    
    





