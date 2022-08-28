#CUSTOM CREATED
from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # return HttpResponse('<h1>Home page!</h1>')
    # params = {'name':'abc', 'age': 25}
    # return render(request, 'index.html', params)
    return render(request, 'index.html')

def analyze(request):
    txt = request.POST.get('text', 'default')
    # action = request.GET.get('action', 'off')
    removepunc = request.POST.get('removepunc', 'off')
    uppercase = request.POST.get('uppercase', 'off')
    lowercase = request.POST.get('lowercase', 'off')
    removenewline = request.POST.get('newline-remover', 'off')
    removespace = request.POST.get('space-remover', 'off')
    countchar = request.POST.get('count-char', 'off')   
    purpose = ""

    if removepunc != 'on' and  uppercase != 'on' and lowercase != 'on' and removenewline != 'on' and removespace != 'on' and countchar != 'on':
        analyzed = txt
        purpose = "Please Select Operations"
        params = {'purpose' : purpose, 'analyzed_text' : analyzed}


    if removepunc == 'on':
        analyzed = ""
        punctuations = '''!()-+[]{};:'"\,<>./?@#$%^&*_~'''     
        purpose = "Remove Punctuation"  
        for char in txt:
            if char not in punctuations:
                analyzed = analyzed + char
        txt = analyzed
    
    if uppercase == 'on':
        analyzed = ""
        purpose = "Convert To Uppercase"    
        analyzed = txt.upper()
        txt = analyzed

    if lowercase == 'on':
        analyzed = ""
        purpose = "Convert To Lowercase"    
        analyzed = txt.lower()
    
    if removenewline == 'on':
        analyzed = ""
        purpose = "Remove New Line"
        for char in txt:
            if char != "\n" and char != "\r":
               analyzed = analyzed + char
        txt = analyzed
    
    if removespace == 'on':
        analyzed = ""
        purpose = "Remove Extra Remove"
        for index, char in enumerate(txt):
            if not(txt[index] == " " and txt[index + 1] == " "):
                analyzed = analyzed + char
        txt = analyzed
    
    if countchar == 'on':
        # analyzed = ""
        purpose = "Count Character"
        countchars = "No. Of Characters : " + str(len(txt))
        params = {'purpose' : purpose, 'analyzed_text' : analyzed, 'total_chars' : countchars}
    else:        
        params = {'purpose' : purpose, 'analyzed_text' : analyzed}

    return render(request, 'analyze.html', params)