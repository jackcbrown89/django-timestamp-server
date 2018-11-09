from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import json

def gettimestamp(request):
	ts = datetime.utcnow().isoformat()
	r = json.dumps({ 'timestamp': ts })
	return HttpResponse(r)

# Create your views here.
