from django.contrib import admin
from .models import *

admin.site.register(IDCard)
admin.site.register(Balance)
admin.site.register(Income)
admin.site.register(Outgo)
admin.site.register(Loan)
admin.site.register(Subscriptions)

# Register your models here.