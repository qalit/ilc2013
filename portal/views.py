# Create your views here.
from models import *
from django.shortcuts import render_to_response
from django.http import Http404
from datetime import datetime

def depan(request):
	Spons_gambar = sponsor_and_partner.objects.all()
	return render_to_response ('index.html', locals())
	
def daftar(request):
	
	return render_to_response ('daftar.html', locals())	

def Jadwal(request):
	JAdwal = jadwal.objects.all()
	return render_to_response ('jadwal.html', locals())		

def Lokasi(request):
	return render_to_response ('lokasi.html', locals())		
	
def gallery(request):
	return render_to_response ('gallery.html', locals())				
	
def Penginapan(request):
	PEnginapan = penginapan.objects.all()
	Penginapan_kelasbawah = penginapan.objects.filter(kelas="bh")
	Penginapan_kelasatas = penginapan.objects.filter(kelas="at")
	Penginapan_kelastengah = penginapan.objects.filter(kelas="tg")
	return render_to_response ('penginapan.html', locals())			
	
def FaQ(request):
	abc = faq.objects.all()
	return render_to_response ('faq.html', locals())		

def Sponsor(request):
	
	SPonsor = sponsor_and_partner.objects.all()
	return render_to_response ('sponsor.html', locals())													

def Hubungi(request):
	if request.method == "POST":
		pass
	return render_to_response ('hubungi.html', locals())														
	
def Informasi(request):
	INformasi = informasi.objects.all()
	return render_to_response ('informasi.html', locals())		
	

def Status(request):
    tail = log(ip=request.META.get('REMOTE_ADDR') + "--"+request.get_host() + "--" +
    	   request.META.get('HTTP_USER_AGENT'), waktu=datetime.now())
    tail.save()
    return render_to_response ('404.html', locals())		
															
