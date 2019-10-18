from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.utils.translation import gettext_lazy as _


def duplicate_alias_validator(alias):
    from tiny.models import TinyURL

    if alias is None or alias == "":
        return True

    if not alias.isalpha():
        raise ValidationError(
            _('Custom alias can only have letters!'),
            params={'alias': alias},
        )


    if len(TinyURL.objects.filter(alias=alias))>0:
        raise ValidationError(
            _('Duplicated Custom Alias: {}'.format(alias)),
            params={'alias': alias},
        )

def url_validator(url):
    if url is None or url == "":
        raise ValidationError("Url param cannot be empty")

    try:
        if '://' not in url:
            #adding http to url
            url = 'http://' + url


        validator = URLValidator(schemes=('http', 'https', 'ftp', 'ftps', 'rtsp', 'rtmp'))
        validator(url)

        return url
    except Exception as e:

        raise ValidationError("Url is not valid")