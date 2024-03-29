from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django .template import loader
from company.models import *
from django.views import generic
# Create your views here.

def home(request):

    context={
        'company': Company.objects.all(),
        'app': Application.objects.all()
    }
    template = loader.get_template('Company\home.html')
    return HttpResponse(template.render(context,request))
    #return render(request, template, context)

def detail(request, c_id):
    obj = get_object_or_404(Company, pk = c_id)
    app = Company.objects.get(pk=c_id)
    template = loader.get_template('Company\\app_detail.html')
    context = {
        'app_list': app.application_set.all(),
        'p_id': c_id
    }
    #return render(request, template, context)
    return HttpResponse(template.render(context, request))

def app_detail(request,a_id):
    obj = Application.objects.get(pk= a_id)
    template = loader.get_template('Company\details.html')
    context={
        'obj': obj
    }
    return HttpResponse(template.render(context, request))

#to add company
def AddCompany(request):
    return render(request, "Company/add_company.html")

#store data to database
def AddCompanySub(request):
    print("Company data is submitted successfully")
    c_name = request.POST["c_name"]
    c_link = request.POST["c_link"]
    company_info = Company(c_name = c_name, c_link = c_link)
    company_info.save()

    return render(request, "Company/add_company.html")

#add application
def AddApplication(request, p_id):
    context = {
        'name': Company.objects.get(pk = p_id),
        'company':Company.objects.all()
    }
    return render(request, "Company/add_application.html", context)

#store data in db
def AddApplicationSub(request):
    print("Application submitted successfully")
    w = request.POST["c_name"]
    x = Company.objects.get(c_name = w)
    print(w)
    profile_name = request.POST["profile_name"]
    date = request.POST["date"]
    link = request.POST["link"]
    desc = request.POST["desc"]
    feedback = request.POST["feedback"]
    resume = request.POST["resume"]
    app_info = Application(c_name = x, profile_name = profile_name, date = date, link = link, desc = desc, feedback = feedback, resume = resume)
    app_info.save()
    context = {
        'company': Company.objects.all()
    }
    return render(request, "Company/add_application.html", context)






