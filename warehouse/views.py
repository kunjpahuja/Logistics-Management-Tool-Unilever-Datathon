from django.shortcuts import render
from .models import Plant, Operation, Consolidated_Data
from django.views.generic import TemplateView, View
from .forms import BudgetForm
from django.http import HttpResponseRedirect

# Create your views here.

def testPage(request):
    return render(request, 'warehouse/index.html')

def update_budget(request):

    if request.method == "POST":
        # print("POSTTTTTT")
        myBudgetForm = BudgetForm(request.POST)

        if myBudgetForm.is_valid:
            # print("VALID")
            myBudgetForm.process
            month = myBudgetForm.cleaned_data['month']
            Plnt = myBudgetForm.cleaned_data['Plant']
            Oper = myBudgetForm.cleaned_data['Operation']
            value = myBudgetForm.cleaned_data['value']

            print(str(Plnt))

    # elif request.method == "GET":
    # else:
    all_plants = Plant.objects.all()
    all_operations = Operation.objects.all()
    # form_class = BudgetForm

    print(request.method)

    context = {
        'all_plants' : all_plants,
        'all_operations' : all_operations
    }

    return render(request, 'warehouse/form2.html', context)

# def get(request):
    #     all_plants = Plant.objects.all()
    #     all_operations = Operation.objects.all()
    #
    #     context = {
    #         'all_plants' : all_plants,
    #         'all_operations' : all_operations
    #     }
    #
    #     return render(request, 'warehouse/form2.html', context)
    #
    # def post(self, request):
    #     pass
    #     # form = self.form_class(request.POST)
    #     #
    #     # if form.is_valid:
    #



# def update_budgetDB(request):
#    username = "didNotWork"
#
#    print(request.method)
#
#    # if request.method == "POST":
#    #    #Get the posted form
#    #    # myBudgetForm = BudgetForm(request.POST)
#    #    print("Post Request Successful")
#    #
#    #    # if BudgetForm.is_valid():
#    #    #    # username = MyLoginForm.cleaned_data['username']
#    #    #    return HttpResponseRedirect('')
#    #    #    print("Post Request")
#    # else:
#    #     print("Post Request Unsuccessful")
#    #     # myBudgetForm = BudgetForm
#
#    return render(request, 'warehouse/testIt.html', {"username" : username})

def login(request):
    return render(request, 'warehouse/login.html')

def emptyDash(request):
    return render(request, 'warehouse/dashboard/index.html')

def wareUpload(request):
    return render(request, 'warehouse/upload/upload.html')

def fullTable(request):
    all_cd = Consolidated_Data.objects.all()

    for cd in all_cd:
        cd.value = cd.value/cd.plant.conversion

    context = {
        'all_cd' : all_cd
    }

    return render(request, 'warehouse/operations/operations.html', context)


def ruTable(request):
    all_cd = Consolidated_Data.objects.filter(plant__coutryCode = "RU")

    for cd in all_cd:
        cd.value = cd.value/cd.plant.conversion

    context = {
        'all_cd' : all_cd
    }

    return render(request, 'warehouse/operations/operations.html', context)

def uaTable(request):
    all_cd = Consolidated_Data.objects.filter(plant__coutryCode = "UA")

    for cd in all_cd:
        cd.value = cd.value/cd.plant.conversion

    context = {
        'all_cd' : all_cd
    }

    return render(request, 'warehouse/operations/operations.html', context)
