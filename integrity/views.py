# Create your views here.
from django.http.response import HttpResponse
from django.shortcuts import render
import requests
import hashlib
from base64 import b64encode
import json


def home(request):
    return render(request, 'home.html', {})


def get_hash(request):
    url = request.GET.get('download_url')
    methods = request.GET.getlist('methods')
    response = requests.get(url)
    if response.ok:
        data = response.content
        out = []
        for method in methods:
            try:
                hash = b64encode(hashlib.new(method, data).digest())
            except Exception as e:
                print e
                continue
            out.append('-'.join([method, hash]))

        return HttpResponse(status=200, content=' '.join(out))
    return HttpResponse(status=400, content='Bad')

