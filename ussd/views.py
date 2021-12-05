from django.http.response import HttpResponse
from django.shortcuts import render
import africastalking
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def  Murakaza(request):
    return render(request, 'index.html')

#  python3 -m pip install africastalking
AfricasUsername='mucyoadonis@gmail.com'
api_key ='d70ce442317ba09027e1572c8e3a9c6c427a21a963f2b25727ac5cfee3890746'
africastalking.initialize(AfricasUsername,api_key)

@csrf_exempt
def ussdApp(request):

    if request.method == 'POST':

        session_id = request.POST.get("sessionId")
        service_code = request.POST.get("serviceCode")
        phone_number =request.POST.get("phoneNumber")
        text = request.POST['text']
        level = text.split('*')
        category = text[:3]
        response =""
        #  main menu for our application
        if text == '':
            response =  "CON Murakaza neza kuri Mushtech \n"
            response += "1. Ikinyarwanda \n"
            response += "2. English\n"
        elif text == '1':

            response = "CON Amakuru ukeneye yose ku gihumyo \n"
            response += "1. igihumyo ni iki? \n"
            response += "2. Amoko y'ibihumyo bihingwa mu Rwanda \n"
            response += "3. Akamaro K'ibihumyo \n"

        elif text == '1*1':
            product="Menya igihumyo icyo aricyo"
            response = "CON Igihumyo ni igihingwa cyihariye; ntikigira indabo cyangwa imbuto.Kigizwe n’ibice bitatu by ingenzi: Umurundugushyu, Umuringa n’ingofero.  Umurundugushu wacyo ntugira imizi, amashami n’amababi. Ibi bisimburwa n’umuringa ndetse n’ingofero. Uyu murundugushu niwo ufata ku mugina aho giteye ukavomamo intungamubiri. "+str(product)+"\n"
        elif category =='1*1' and int(len(level)) == 3 and str(level[2]) in  str(level):
            response = "END Murakoze gusura Mushtech \n"


        elif text == '1*2':
            respone ="CON Dore amoko y'ibihumyo bihingwa mu Rwanda"
            response += "1. Pleurote ( Soma Pulerote) \n"
            response += "2. Ganoderma ( soma Ganoderima) \n"
        
        
        # elif category =='1*2' and int(len(level)) == 3 and str(level[2]) in  str(level):
        #     response = "CON Uwo mubufatanyije \n"
        # elif category =='1*2' and int(len(level)) == 4 and str(level[3]) in  str(level):
        #     response = "CON Shyiramo nimero y'irangamuntu yuwo mufatanyije \n"
        # elif category =='1*2' and int(len(level)) == 5 and str(level[4]) in  str(level):
        #     response = "END Murakoze kwiyandikisha kuri Ida farm \n"
         
        #  ======================== INGENGABIHE==================
        elif text == '2':
            response = "CON Hitamo igihe \n "
            response += "1. Rimwe mukwezi \n"
            response += "2. Kabiri Mukwezi \n"
            response += "3. Buri gihe"
        elif text == '2*1':
            response ="END Murakoze , tuzajya tubagezaho amakuru ku iteganyagihe rimwe mukwezi"
        elif text == '2*2':
            response ="END Murakoze , tuzajya tubagezaho amakuru ku iteganyagihe kabiri mukwezi"
        elif text == '2*3':
            response ="END Murakoze , tuzajya tubagezaho amakuru ku iteganyagihe Buri munsi"

        else:
            response = "END Ukanze ibitaribyo, ongera mukanya"
        return HttpResponse(response)
    else:
        return HttpResponse('we are on ussd app')