from django.shortcuts import render
from django.http import HttpResponse
from django.http import FileResponse, Http404


# Create your views here.
def pdf(request):
    return render(request, "home.html")

def pdf_view(request, pdf_type):

    if pdf_type == "compute":
        try:
            return FileResponse(open('pdfserverapp/pdfs/seaplane.pdf', 'rb'), content_type='application/pdf')
        except FileNotFoundError:
            raise Http404()

    if pdf_type == "coordination":
        return HttpResponse("Coordination")
    else: raise Http404()
    
