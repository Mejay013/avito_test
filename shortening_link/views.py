from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
import pyshorteners
import urllib
import requests
from django.core.validators import URLValidator



def index(request):
    try: 
        if request.method == "POST": 
            
            warning_list = list() # список для ошибок
            old_link = request.POST['old_link']
            custom_link = request.POST['custom_link']

            val = URLValidator() 
            test = val(old_link) # проверяем валидность ссылки

            if custom_link and test != 'invalid':
                result = custom_link_send(old_link,custom_link)

                if result['new_url'] != None: #если удалось создать новую ссылку - отправляем её
                    return render(request, 'shortening_link/index.html',{'new_link': result['new_url']})
                    
                else:
                    warning_list.append(result['error']) #иначе отпраыляем код ошибки
                    return render(request, 'shortening_link/index.html',{'warning_list': warning_list})

            if old_link and test != 'invalid': # Если ссылки валидна и не пустая
                s = pyshorteners.Shortener()  
                new_link = s.tinyurl.short(old_link) # используем pyshorteners для создания короткой ссылки
                return render(request, 'shortening_link/index.html',{'new_link' : new_link}) # отправляем ссылку шаблону

    except :
        warning_list.append('Проверьте корректность введенной ссылки')
        return render(request, 'shortening_link/index.html',{'warning_list': warning_list}) # отправляем список ошибок шаблону

    return render(request, 'shortening_link/index.html')



def custom_link_send(old_link,custom_link):
    problem_dict = { 400 : 'URL domain banned',
                     422 : 'Некорректный URL или кол-во допустимых сокращений превышено'} 
    URL = "http://tinyurl.com/api-create.php"
    answer_dict = {'new_url': None , 'error':None}

    url = URL + "?" + urllib.parse.urlencode({"url": old_link , "alias": custom_link })
    res = requests.get(url)
    if res.status_code == 200:
        answer_dict['new_url'] = res.text
    elif res.status_code in problem_dict:
        answer_dict['error'] = problem_dict[res.status_code]
    return answer_dict
    
