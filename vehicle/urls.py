from vehicle import forms
from vehicle.forms import LoginForm
from django.contrib import auth
from django.urls import path
from vehicle import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from .forms import LoginForm, MyPasswordChangeForm, MyPasswordConfirmForm, MyPasswordResetForm,feedbackForm
from django.contrib import admin

urlpatterns = [
   
    path('', views.ProductView.as_view(), name="home"),
    path('product-detail/<int:pk>',views.ProductDetailView.as_view(), name='product-detail'),
    path('customer', views.customer),
    path('orderplaced', views.orderplaced),
    path('carts', views.carts),
    path('product', views.product),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='cart'),
    path('cart/',views.show_cart, name='showcart'),
    path('pluscart/',views.plus_cart),
    path('minuscart/',views.minus_cart),
    path('removecart/',views.remove_cart),
    

    path('buy/', views.buy_now, name='buy-now'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('passwordchange/',auth_views.PasswordChangeView.as_view(template_name='passwordchange.html',form_class=MyPasswordChangeForm, success_url='/passwordchangedone/'),name='passwordchange'),
    path('passwordchangedone/',auth_views.PasswordChangeView.as_view(template_name='passwordchangedone.html'), name='passwordchangedone'),
    
    path('password-reset/',auth_views.PasswordResetView.as_view(template_name='password_reset.html',form_class=MyPasswordResetForm), name='password_reset'),
    path('password-reset/done/',auth_views.PasswordResetDoneView.as_view(template_name='password__reset_done.html'), name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html',form_class=MyPasswordConfirmForm), name='password_reset_confirm'),
    path('password-reset-complete/',auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'), name='password_reset_complete'),

    path('bonnet/', views.bonnet, name='bonnet'),
    path('bonnet/<slug:data>', views.bonnet, name='bonnetdata'),
    path('foglight/', views.foglight, name='foglight'),
    path('foglight/<slug:data>', views.foglight, name='foglightdata'),
    path('bumper/', views.bumper, name='bumper'),
    path('bumper/<slug:data>', views.bumper, name='bumperdata'),
    path('door/', views.door, name='door'),
    path('door/<slug:data>', views.door, name='doordata'),
path('headlight/', views.headlight, name='headlight'),
    path('headlight/<slug:data>', views.headlight, name='headlightdata'),
path('taillight/', views.taillight, name='taillight'),
    path('taillight/<slug:data>', views.taillight, name='taillightdata'),
# path('dryfruit/', views.dryfruit, name='dryfruit'),
#     path('dryfruit/<slug:data>', views.dryfruit, name='dryfruitdata'),
#
# path('candy/', views.candy, name='candy'),
#     path('candy/<slug:data>', views.candy, name='candydata'),
# path('protein/', views.protein, name='protein'),
#     path('protein/<slug:data>', views.protein, name='proteindata'),
# path('chocolate/', views.chocolate, name='chocolate'),
#     path('chocolate/<slug:data>', views.chocolate, name='chocolatedata'),
#
# path('jam/', views.jam, name='jam'),
#     path('jam/<slug:data>', views.jam, name='jamdata'),
# path('pickle/', views.pickle, name='pickle'),
#     path('pickle/<slug:data>', views.pickle, name='pickledata'),
# path('chutney/', views.chutney, name='chutney'),
#     path('chutney/<slug:data>', views.chutney, name='chutneydata'),
# path('peanut/', views.peanut, name='peanut'),
#     path('peanut/<slug:data>', views.peanut, name='peanutdata'),
#
# path('soap/', views.soap, name='soap'),
#     path('soap/<slug:data>', views.soap, name='soapdata'),
# path('oil/', views.oil, name='oil'),
#     path('oil/<slug:data>', views.oil, name='oildata'),
# path('food/', views.food, name='food'),
#     path('food/<slug:data>', views.food, name='fooddata'),





    path('accounts/login/', auth_views.LoginView.as_view(template_name='login.html',authentication_form=LoginForm), name='login' ),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path('customerregistration/',views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('feedbacks/',views.Feedbacks.as_view(), name='feedbacks'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/',views.payment_done, name='paymentdone'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
