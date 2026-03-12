from itertools import product

from django.contrib import admin
from .models import *
# from .models import reg, Product
admin.site.register(reg)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(CartItem)