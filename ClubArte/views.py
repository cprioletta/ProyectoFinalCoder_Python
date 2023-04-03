from django.http import HttpResponse
from django.shortcuts import render
from ClubArte.models import Cine


# Create your views here.
def guardar_cine(request, id_Cine):
    cine = Cine(titulo="Legalmente rubia", director="Lucketic, R.", id_Cine="1001")
    cine.save()
    return HttpResponse("Película agregada con éxito.")

#def cicloPoesia(request):
#    return render(request, "index.html")

#def cursoFotograf(request):
#    return render(request, "index.html")