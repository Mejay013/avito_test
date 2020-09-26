from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
import pyshorteners
from django.core.validators import URLValidator


def index(request):
    try: 
        if request.method == "POST":
            val = URLValidator()
            warning_list = list()
            old_link = request.POST['old_link']
            test = val(old_link)
            if old_link and test != 'invalid':
                s = pyshorteners.Shortener()
                new_link = s.tinyurl.short(old_link)
                context = {
                    'old_link': old_link,
                    'new_link' : new_link
                }
                return render(request, 'shortening_link/index.html',context)
    except:
        warning_list.append('Проверьте корректность введенной ссылки')
        return render(request, 'shortening_link/index.html',{'warning_list': warning_list})
    return render(request, 'shortening_link/index.html')