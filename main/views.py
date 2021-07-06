from django.http import HttpResponse

def home(request):
    return HttpResponse("""
    <html>
    <a href="./about">biz xaqimizda</a>
    """)
    print(request.GET)
    
def biz_xaqimizda(request):
    return HttpResponse("Saytimizga xush kelibsiz ...")
def contact(request):
    return HttpResponse("bizni shu raqamlar orqali topasizlar")
