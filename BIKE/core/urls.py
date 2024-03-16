from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.home,name='home'),

    path('contact',views.contact,name='contact'),

    path('instagram',views.instagram,name='instagram'),

    path('facebook',views.facebook,name='facebook'),

    path('dashboard',views.dashboard,name='dashboard'),

    
    
    path('registration/',views.registration,name='registration'),

    path('login/',views.log_in,name='login'),

    path('profile/',views.profile,name='profile'),

    path('logout/',views.log_out, name="logout"),

    path('changepassword/',views.changepassword, name="changepassword"),

    
    
    path('address/',views.address,name='address'),
    path('delete_address/<int:id>',views.delete_address,name='deleteaddress'),

    
    path('sport_categories/',views.SportCategoriesView.as_view(),name='sportbikecategories'),
    path('electric_categories/',views.ElectricCategoriesView.as_view(),name='electricbikecategories'),
    path('scoty_categories/',views.ScotyCategoriesView.as_view(),name='elctericscotycategory'),

    
    path('sportbike_details/<int:id>/',views.SportbikeDetailView.as_view(),name='sportbikedetails'),
    path('electricbike_details/<int:id>/',views.ElectricbikeDetailView.as_view(),name='electricbikedetails'),
    path('electricscoty_details/<int:id>/',views.ElectricscotyDetailView.as_view(),name='electricscotydetails'),




    path('royal_bike/',views.RoyalCategoriesView.as_view(),name='royalbike'),
    path('shine_bike/',views.ShineCategoriesView.as_view(),name='shinebike'),
    path('unicorn_bike/',views.UnicornCategoriesView.as_view(),name='unicornbike'),
    path('activa_bike/',views.ActivaCategoriesView.as_view(),name='activabike'),
    path('avenger_bike/',views.AvengerCategoriesView.as_view(),name='avengerbike'),
    path('dio_bike/',views.DioCategoriesView.as_view(),name='diobike'),


    path('viewcart/',views.view_cart, name="viewcart"),

    path('add_to_cart/<int:id>/',views.add_to_cart, name="addtocart"),

    path('add_quantity/<int:id>/', views.add_quantity, name='add_quantity'),

    path('delete_quantity/<int:id>/', views.delete_quantity, name='deletequantity'),

    path('delete_cart/<int:id>',views.delete_cart, name="deletecart"),

    
    
    path('checkout/',views.checkout,name='checkout'),

    path('payment/',views.payment,name='payment'),
    
    path('payment_success/<int:selected_address_id>/',views.payment_success,name='paymentsuccess'),

    path('payment_failed/',views.payment_failed,name='paymentfailed'),

    path('order/',views.order,name='order'),

    path('buynow/<int:id>',views.buynow,name='buynow'),

    path('buynow_payment/<int:id>',views.buynow_payment,name='buynowpayment'),

    path('buynow_payment_success/<int:selected_address_id>/<int:id>',views.buynow_payment_success,name='buynowpaymentsuccess'),
    

]
    
     
    

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)