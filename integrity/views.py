# Create your views here.
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.http.response import HttpResponse
from django.shortcuts import render
import requests
import hashlib
from base64 import b64encode
import json
import re


def home(request):
    return render(request, 'home.html', {})


def get_hash(request):
    url = request.GET.get('download_url')
    methods = request.GET.getlist('methods')
    js_regex = re.compile(r'.js((?P<gets>[\?]+)(?(gets)[\%\-\#\?\=\& \w]+))?$')
    css_regex = re.compile(r'.css((?P<gets>[\?]+)(?(gets)[\%\-\#\?\=\& \w]+))?$')
    try:
        URLValidator()(url)
    except ValidationError as e:
        return HttpResponse(status=400, content=json.dumps(e.messages))

    ftype = 'error'
    if js_regex.search(url):
        ftype = 'js'
    elif css_regex.search(url):
        ftype = 'css'

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
        out_dict = dict(
            hashes=' '.join(out),
            ftype=ftype
        )
        return HttpResponse(status=200, content=json.dumps(out_dict))
    return HttpResponse(status=400, content='Bad')

