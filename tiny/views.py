from django.http import HttpResponse
from django.shortcuts import redirect, render

from tiny.models import TinyURL
from django.http import JsonResponse
from django.views.generic.base import TemplateView
from tiny.validators import duplicate_alias_validator, url_validator
import time


def create(request):
    start = time.time()
    if request.method == "POST":
        try:
            url = request.GET.get('url', "")
            alias = request.GET.get('alias', "")
            url = url_validator(url)
            duplicate_alias_validator(alias)

        except Exception as e:
            return JsonResponse({"error": str(e.args[0])},
                                content_type="application/json", status=400)

        tiny = TinyURL(original=url, alias=alias)
        tiny.save()

        if tiny.alias is None or tiny.alias == "":
            tiny.generate_new_alias()

        return JsonResponse(tiny.json(time.time() - start),
                            content_type="application/json", status=200)

    else:
        return JsonResponse({"error": "Method not Allowed"}, content_type="application/json",
                            status=405)


class RetrieveView(TemplateView):

    def get(self, request, *args, **kwargs):

        if not 'alias' in kwargs:
            return JsonResponse({"error": "SHORTENED URL NOT FOUND"},
                                content_type="application/json", status=400)

        tiny = TinyURL.objects.filter(alias=kwargs["alias"]).first()
        if tiny:
            tiny.add_click()
            return redirect(tiny.original)
        else:
            return JsonResponse({"error": "SHORTENED URL NOT FOUND"},
                                content_type="application/json",status=400)
    def post(self, request, *args, **kwargs):
        return JsonResponse({"error": "Method not Allowed"}, content_type="application/json",
                            status=405)

def ranking(request):
    try:
        rank =  [tiny.json_ranking() for tiny in TinyURL.objects.order_by("-clicks").filter(clicks__gt=0)[:10]]
        return JsonResponse({"ranking":rank}, content_type="application/json",status=200)
    except Exception as e:
        return JsonResponse({"error": str(e.args[0])},
                                content_type="application/json", status=500)

