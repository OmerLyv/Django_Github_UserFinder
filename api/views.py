from django.shortcuts import render,redirect
import requests
from django.contrib import messages


base_url = "https://api.github.com/users/"


def index(request):
    
    if request.method == "POST":
        
        githubname = request.POST.get("githubname")
        response_user = requests.get(base_url + githubname)
        response_repos = requests.get(base_url + githubname + "/repos")

        user_info = response_user.json()
        repos = response_repos.json()
        
        if "message" in user_info:
                messages.warning(request,"Böyle bir kullanıcı bulunamadı")
                return redirect("index")
        else:
            return render(request,"index.html",{"profile" :user_info,"repos" : repos})
    else:
        return render(request,"index.html")