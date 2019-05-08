from .models import Link

"""
Esto se configura en el settings.py para que pueda ser 'inyectado' a cualquier template
"""
def ctx_dict(request):
    ctx = {}
    links = Link.objects.all()
    for link in links:
        ctx[link.key] = link.url
    return ctx