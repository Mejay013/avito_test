from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
import pyshorteners
from django.core.validators import URLValidator


def index(request):
    try: 
        if request.method == "POST": 
            val = URLValidator() 
            warning_list = list() # список для ошибок
            old_link = request.POST['old_link'] 
            test = val(old_link) # проверяем валидность ссылки
            if old_link and test != 'invalid': # Если ссылки валидна и не пустая
                s = pyshorteners.Shortener()  
                new_link = s.tinyurl.short(old_link) # используем pyshorteners для создания короткой ссылки
                context = {
                    'new_link' : new_link
                }
                return render(request, 'shortening_link/index.html',context) # отправляем ссылку шаблону
    except:
        warning_list.append('Проверьте корректность введенной ссылки')
        return render(request, 'shortening_link/index.html',{'warning_list': warning_list}) # отправляем список ошибок шаблону
    return render(request, 'shortening_link/index.html')