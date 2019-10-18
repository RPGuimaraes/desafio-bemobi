from unittest import TestCase

from django.test import TransactionTestCase

from tiny.models import TinyURL
from tinyUrl import settings


class TinyURLTest(TransactionTestCase):
    databases = {'default'}
    def test_click(self):

        tiny = TinyURL(original="google.com.br",alias="test")

        self.assertEqual(tiny.add_click(), 1)
        self.assertEqual(tiny.add_click(), 2)
        self.assertEqual(tiny.add_click(), 3)
        self.assertEqual(tiny.add_click(), 4)



    def test_json(self):
        tiny = TinyURL(original="google.com.br", alias="test")
        self.assertEqual(tiny.json(0), {'alias': (settings.ACTUAL_URL + tiny.alias), 'url': tiny.original, "statistic": {'time_taken': "{:.3f}ms".format(0)}})
        self.assertEqual(tiny.json(0.12346), {'alias': (settings.ACTUAL_URL + tiny.alias), 'url': tiny.original, "statistic": {'time_taken': "{:.3f}ms".format(0.12346*1000)}})

    def test_json_ranking(self):
        tiny = TinyURL(original="google.com.br", alias="test",clicks=10)
        self.assertEqual(tiny.json_ranking(),{'alias': (tiny.alias), 'url': tiny.original, "clicks": tiny.clicks})

        tiny.original="oi.com.br"
        tiny.click=20
        tiny.alias="oi"

        self.assertEqual(tiny.json_ranking(), {'alias': (tiny.alias), 'url': tiny.original, "clicks": tiny.clicks})



    def test_generate_new_alias(self):
        tiny = TinyURL(original="google.com.br",alias="test")
        self.assertEqual(tiny.generate_new_alias(), tiny.alias)
        self.assertEqual(tiny.generate_new_alias(), tiny.alias)
        self.assertEqual(tiny.generate_new_alias(), tiny.alias)




