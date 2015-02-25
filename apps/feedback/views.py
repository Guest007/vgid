from django.http import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def callback(request):
    # print "WOW!"
    # print request
    return JsonResponse({'status': 'ok'})