import random
import string
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger, InvalidPage


def paginate(request, obj_list, num_per_page=10):
    paginator = Paginator(obj_list, num_per_page)
    
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1
    
    try:
        objects = paginator.page(page)
    except (EmptyPage, InvalidPage):
        objects = paginator.page(paginator.num_pages)
    return objects

def sku_code(size=6, chars=string.ascii_uppercase + string.digits):
    
    return ''.join(random.choice(chars) for _ in range(size))