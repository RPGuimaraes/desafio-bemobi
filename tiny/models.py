from tiny.serviceTinyUrl import generate_alias_service
from django.db import models


from django.conf import settings

# Create your models here.
class TinyURL(models.Model):
    original = models.CharField(max_length=255, blank=True)
    alias = models.CharField(max_length=255, blank=True)
    clicks = models.IntegerField(default=0)


    def add_click(self):
        self.clicks+=1
        self.save()
        return self.clicks

    def json(self,time=0):
        return {'alias': (settings.ACTUAL_URL +self.alias), 'url': self.original, "statistic": {'time_taken': "{:.3f}ms".format(time*1000)}}

    def json_ranking(self):
        return {'alias': (self.alias), 'url': self.original, "clicks":self.clicks}

    def generate_new_alias(self):
        generate_alias_service(self).save()
        return self.alias

