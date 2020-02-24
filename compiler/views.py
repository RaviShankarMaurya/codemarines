from django.shortcuts import render
from django.http import HttpResponse
from .models import Questions
import os
# Create your views here.


temp=Questions.objects.all()
buttons=temp
ques=temp[0]


def home(request):
      return render(request,"index.html",{"buttons":buttons,"Questions":ques})

def index2(request):
    q=int(request.GET['q'])

    ques=temp[q-1]
    return render(request,"index2.html",{"buttons":buttons,"Questions":ques})
def compile(request):
    q=int(request.GET['q'])
    ques=temp[q-1]

    code=request.GET['codebox']
    code=str(code)
    codefile=open("templetes/code.py","w+")
    codefile.write(code)
    codefile.close()
    os.system("python templetes/code.py > templetes/result.txt 2>templetes/error.txt")
    file=open("templetes/result.txt")
    result=""
    error=""
    errorfile=open("templetes/error.txt")
    for i in errorfile.readlines():
        error+=i
    errorfile.seek(0)

    if len(error)<2:
        for i in file.readlines():
            result=result+i
        return render(request,"compile.html",{"buttons":buttons,"Questions":ques,'res':result,'pcode':code})
        file.close()
    else:
        errorfile.seek(0)
        for i in errorfile.readlines():
            error+=i
        
    return render(request,"compile.html",{"buttons":buttons,"Questions":ques,'res':error,'pcode':code})
code=""