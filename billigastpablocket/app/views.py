from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse
from datetime import datetime, timedelta

def index(request):
	
	dic = []  
	return render(request, 'index.html', {'dic': dic}) 

def getSearch(request):
	searchTerm = request.POST.get('search')
	items = []
	last_month = datetime.today() - timedelta(days=30)
	terms = searchTerm.split(" ")
	if len(terms) == 1:
		objects = Listing.objects.filter(name__icontains=searchTerm).filter(downloaded_at__gte=last_month)
	elif len(terms) == 2:
		objects = Listing.objects.filter(name__icontains=terms[0]).filter(name__icontains=terms[1]).filter(downloaded_at__gte=last_month)
	elif len(terms) == 3:
		objects = Listing.objects.filter(name__icontains=terms[0]).filter(name__icontains=terms[1]).filter(name__icontains=terms[2]).filter(downloaded_at__gte=last_month)
	elif len(terms) == 4:
		objects = Listing.objects.filter(name__icontains=terms[0]).filter(name__icontains=terms[1]).filter(name__icontains=terms[2]).filter(name__icontains=terms[3]).filter(downloaded_at__gte=last_month)
	elif len(terms) == 5:
		objects = Listing.objects.filter(name__icontains=terms[0]).filter(name__icontains=terms[1]).filter(name__icontains=terms[2]).filter(name__icontains=terms[3]).filter(name__icontains=terms[4]).filter(downloaded_at__gte=last_month)
	elif len(terms) == 6:
		objects = Listing.objects.filter(name__icontains=terms[0]).filter(name__icontains=terms[1]).filter(name__icontains=terms[2]).filter(name__icontains=terms[3]).filter(name__icontains=terms[4]).filter(name__icontains=terms[5]).filter(downloaded_at__gte=last_month)
	elif len(terms) == 7:
		objects = Listing.objects.filter(name__icontains=terms[0]).filter(name__icontains=terms[1]).filter(name__icontains=terms[2]).filter(name__icontains=terms[3]).filter(name__icontains=terms[4]).filter(name__icontains=terms[5]).filter(name__icontains=terms[6]).filter(downloaded_at__gte=last_month)
	elif len(terms) == 8:
		objects = Listing.objects.filter(name__icontains=terms[0]).filter(name__icontains=terms[1]).filter(name__icontains=terms[2]).filter(name__icontains=terms[3]).filter(name__icontains=terms[4]).filter(name__icontains=terms[5]).filter(name__icontains=terms[6]).filter(name__icontains=terms[7]).filter(downloaded_at__gte=last_month)
	elif len(terms) == 9:
		objects = Listing.objects.filter(name__icontains=terms[0]).filter(name__icontains=terms[1]).filter(name__icontains=terms[2]).filter(name__icontains=terms[3]).filter(name__icontains=terms[4]).filter(name__icontains=terms[5]).filter(name__icontains=terms[6]).filter(name__icontains=terms[7]).filter(name__icontains=terms[8]).filter(downloaded_at__gte=last_month)
	else:
		objects = Listing.objects.filter(name__icontains=searchTerm).filter(downloaded_at__gte=last_month)

	if objects.count() == 0:
		response = '{"errorResult" : "no-result"}'
		bytes = JsonResponse(response, safe=False)
		return HttpResponse(bytes, content_type='application/json')

	for obj in objects:
		items.append(obj.price)
	medv = median(items)
	minv = min(float(s) for s in items)
	maxv = max(float(s) for s in items)

	response = '{"search":"'+searchTerm+'", "med":"'+str(medv)+'", "min":"'+str(minv)+'", "max":"'+str(maxv)+'"}'
	bytes = JsonResponse(response, safe=False)
	return HttpResponse(bytes, content_type='application/json')

def median(lst):
    sortedLst = sorted(lst)
    lstLen = len(lst)
    index = (lstLen - 1) // 2

    if (lstLen % 2):
        return sortedLst[index]
    else:
        return (sortedLst[index] + sortedLst[index + 1])/2.0

