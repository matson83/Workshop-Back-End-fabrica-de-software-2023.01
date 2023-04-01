from django.contrib import admin

from app.models import Cliente
from app.models import Produto
# Register your models here.
admin.site.register(Cliente)
admin.site.register(Produto)