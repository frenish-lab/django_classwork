from django.shortcuts import render
from django.http import HttpResponse 

users = [
        {"id":1,"name":"deep","email":"deep@gmail.com","phone":123456789},
        {"id":2,"name":"dev","email":"dev@gmail.com","phone":123456789},
        {"id":3,"name":"raj","email":"raj@gmail.com","phone":123456789}
    ]
# Create your views here.

def Welcome(request):
    if request.method == "GET":
        print(request.method)
        return render(request,"index.html")
        # return HttpResponse("not found...!")
    return HttpResponse("not found...!")
    
    
def form(request):
    if request.method == "GET":
        print(request.method)
        return render(request,"table.html",{"users":users})
        # return HttpResponse("not found...!")
    if request.method == "POST":
        name = request.POST.get("username")
        email = request.POST.get("useremail")
        phone = request.POST.get("userphone")
        
        user =  {"id":1,"name":name,"email":email,"phone":phone}
        print(user)
        print("_"*20)
        users.append(user)
        for i in users:
            print(i)
        print("_"*20)
        return render(request,"table.html",{"users":users})
    return HttpResponse("table not found...!")
    
    