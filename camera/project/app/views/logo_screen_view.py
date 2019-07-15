from django.views.generic import View
from django.shortcuts import render

class LogoScreenView(View):
    def get(self, request):
        return render(request, 'logo.html', {})