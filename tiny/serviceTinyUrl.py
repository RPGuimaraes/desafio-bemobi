chars = 'SW1n9ckUYKCBR2H5qMONDuvdypG6ZbolLfVX4JF0xh8ezsar7gPwjtTIiQmE3A'
mapping = range(52)[::-1]


def encode(n):
    result = 0
    for i, b in enumerate(mapping):
        b1 = 1 << i
        b2 = 1 << mapping[i]
        if n & b1:
            result |= b2
    return result


def enbase(x):
    x = int(x)
    n = len(chars)
    if x < n:
        return chars[x]
    return enbase(x / n) + chars[x % n]


def generate_alias_service(tiny):
    from tiny.models import TinyURL
    tiny.alias = None

    if tiny.id is None:
        tiny.save()

    alias = enbase(encode(tiny.id))

    while TinyURL.objects.filter(alias=alias).first() is not None:
        tiny.id = None
        tiny.save()
        alias = enbase(encode(tiny.id))

    tiny.alias = alias

    return tiny



