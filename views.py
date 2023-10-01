from django.shortcuts import render
from django.http.response import HttpResponse,JsonResponse
from.models import *
import random
def login(request):
 a="ankita"
 print(a)
 return render (request, "login.html")

def signup(request):
 return render(request,"signup.html")
        
def home(request):
 return render(request,"home.html")

def getstulogin1(request):
    try:
          question_objs=list(Question.objects.all())
          data = []
          random.shuffle(list(question_objs))
          for question_obj in question_objs:
               data.append({
                 "category": question_obj.category.category_name,
                 "question": question_obj.question,
                 "marks":    question_obj.marks,
                 "answers":   question_obj.get_answers()
                })
          payload={'status':True, 'data':data}
          return  JsonResponse(payload)
             
          

    except Exception as e:
        print(e)  
    return HttpResponse("something went wrong") 