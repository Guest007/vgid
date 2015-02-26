from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def callback(request):
    # print "WOW!"
    # print request.POST
    return JsonResponse({'status': 'ok'})


@csrf_exempt
def excurs(request):
    # print "WOW!"
    # print request.POST
    return JsonResponse({'status': 'ok'})


@csrf_exempt
def feedback(request):
    # print "WOW!"
    # print request.POST
    return JsonResponse({'status': 'ok'})

