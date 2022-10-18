from django.urls import path

from . import views

urlpatterns = [
    path('', views.pdf, name='pdf'),
    path('pdfview/<str:pdf_type>', views.pdf_view, name='pdfview')
]