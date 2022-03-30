from django.shortcuts import render

# Create your views here.
info=[
    {'Fname': 'Hrishikesh', 'Mname':'P', 'Lname':'Pani', 'Role':'Teacher', 'Department': 'comps', 'Pno': '234', 'Email': 'Whatever'},
    {'Fname': 'Hrishikesh', 'Mname':'P', 'Lname':'Pani', 'Role':'Teacher', 'Department': 'comps', 'Pno': '234', 'Email': 'Whatever'},
    {'Fname': 'Hrishikesh', 'Mname':'P', 'Lname':'Pani', 'Role':'Teacher', 'Department': 'comps', 'Pno': '234', 'Email': 'Whatever'},
    {'Fname': 'Hrishikesh', 'Mname':'P', 'Lname':'Pani', 'Role':'Teacher', 'Department': 'comps', 'Pno': '234', 'Email': 'Whatever'},
    {'Fname': 'Hrishikesh', 'Mname':'P', 'Lname':'Pani', 'Role':'Teacher', 'Department': 'comps', 'Pno': '234', 'Email': 'Whatever'},
    {'Fname': 'Hrishikesh', 'Mname':'P', 'Lname':'Pani', 'Role':'Teacher', 'Department': 'comps', 'Pno': '234', 'Email': 'Whatever'},
    {'Fname': 'Hrishikesh', 'Mname':'P', 'Lname':'Pani', 'Role':'Teacher', 'Department': 'comps', 'Pno': '234', 'Email': 'Whatever'},
    {'Fname': 'Hrishikesh', 'Mname':'P', 'Lname':'Pani', 'Role':'Teacher', 'Department': 'comps', 'Pno': '234', 'Email': 'Whatever'},
    {'Fname': 'Hrishikesh', 'Mname':'P', 'Lname':'Pani', 'Role':'Teacher', 'Department': 'comps', 'Pno': '234', 'Email': 'Whatever'},
    
]

def Adminpage(request):
    return render(request, 'admin.html', {'info': info})