from django.views.generic import View
from django.shortcuts import render

class IndexView(View):
    def get(self, request):
        return render(request, 'index.html', {})