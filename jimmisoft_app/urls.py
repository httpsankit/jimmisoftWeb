# from django.contrib import admin
# from django.urls import path
# from jimmisoft.views import hello_django
from . import views
from jimmisoft.urls import path

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('debug/app/', views.get_app, name='hello_django'),
    path('get_adharcard/data/', views.fetch_adhar_card_data_views, name='adharcard_data'),
    path('get_pancard/data/', views.fetch_pan_card_data_views, name='pancard_data')
]
