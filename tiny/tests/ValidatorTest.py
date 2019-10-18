from unittest import TestCase

from django.test import TransactionTestCase

from tiny.models import TinyURL
from tiny.validators import duplicate_alias_validator, url_validator



class ValidatorTest(TransactionTestCase):
    databases = {'default'}

    def test_duplicate_alias_validator(self):
        self.assert_(duplicate_alias_validator(""), True)
        self.assert_(duplicate_alias_validator(None), True)

        with self.assertRaises(Exception) as context:
            duplicate_alias_validator('123?')
        self.assertFalse('This is broken' in str(context.exception))

        with self.assertRaises(Exception) as context:
            tiny = TinyURL(alias="teste",original="oi.com.br")
            tiny.save()
            duplicate_alias_validator(tiny.alias)

        self.assertFalse('This is broken' in str(context.exception))



    def test_url_validator(self):

        with self.assertRaises(Exception) as context:
            url_validator(None)
        self.assertFalse('This is broken' in str(context.exception))

        with self.assertRaises(Exception) as context:
            url_validator("")
        self.assertFalse('This is broken' in str(context.exception))

        with self.assertRaises(Exception) as context:
            url_validator("oicombr")
        self.assertFalse('This is broken' in str(context.exception))