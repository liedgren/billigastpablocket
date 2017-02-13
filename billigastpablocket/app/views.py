from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse

def index(request):
	
	dic = []  
	return render(request, 'index.html', {'dic': dic}) 

def getSearch(request):
	searchTerm = request.POST.get('search')
	items = []
	objects = Listing.objects.filter(name__contains=searchTerm)
	if objects.count() == 0:
		response = '{"error": "no-result"}'
		bytes = JsonResponse(response, safe=False)
		return HttpResponse(bytes, content_type='application/json')

	for obj in objects:
		items.append(obj.price)
	answer = median(items)
	response = '{"search":"'+searchTerm+'", "answer":"'+str(answer)+'"}'
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

