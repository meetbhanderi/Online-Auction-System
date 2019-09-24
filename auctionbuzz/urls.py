from django.urls import path
from django.conf.urls import url
from auctionbuzz import views
from django.conf.urls import url, include
from django.contrib import admin
import auctionbuzz.views
from .classviews import BidderListView, ProductDelete, UserCreateView
from .classviews import ProductDetailView, AddProductView, ProductView
from django.contrib.auth.decorators import login_required
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth.views import logout_then_login
urlpatterns = [
     url(r'^$', auctionbuzz.views.home, name="home"),
     url('^login/',views.login,name="login"),
     url('^registration/',views.registration,name="registration"),
     url('^announce/',views.announce,name="announce"),
     url(r'^viewproduct/', login_required(ProductView.as_view()), name="view_product"),
     url(r'^addproduct/', login_required(AddProductView.as_view()), name="add_product"),
     url(r'^productdetails/(?P<pk>[0-9]+)', login_required(ProductDetailView.as_view()), name="product_detail"),
     url(r'^save_bid/', login_required(auctionbuzz.views.save_bid), name="save_bid"),
     url(r'^register_user/', UserCreateView.as_view(), name="register"),
     url(r'^deleteproduct/(?P<pk>[0-9]+)', login_required(ProductDelete.as_view()), name="delete_product"),
     url(r'^bidderlist/(?P<pk>[0-9]+)', login_required(BidderListView.as_view()), name="bidder_list"),
     url(r'^logout/', views.logout, name='logout')
]


