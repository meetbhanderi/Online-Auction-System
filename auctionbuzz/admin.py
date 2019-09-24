from django.contrib import admin
from .models import *
#admin.site.register(user_info)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'category', 'minimum_price', 'bid_end_date')
admin.site.register(Product, ProductAdmin)



class SellerAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'product_id')
admin.site.register(Seller, SellerAdmin)


class BidderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user_name', 'product_id', 'bid_amount')
admin.site.register(Bidder, BidderAdmin)