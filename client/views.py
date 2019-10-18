from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView


class MainView(TemplateView):
    def get(self, request, *args, **kwargs):
        return render(request, 'index.html', )

    def post(self, request, *args, **kwargs):
        return JsonResponse({"error": "Method not Allowed"}, content_type="application/json",
                            status=405)