from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
import pyshorteners



def index(request):
    if request.method == "POST":
        old_link = request.POST['old_link']
        if old_link:

            s = pyshorteners.Shortener()
            new_link = s.tinyurl.short(old_link)
            context = {
                'old_link': old_link,
                'new_link' : new_link
            }
            return render(request, 'shortening_link/index.html',context)
    return render(request, 'shortening_link/index.html')