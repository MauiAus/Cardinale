"""cardinale URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from inventory import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.homepage, name='home'),
	path('home', views.homepage, name='home'),
    path('login',views.loginpage, name='login'),
    path('logout', views.logoutuser, name='logout'),
    path('register',views.registerpage, name='register'),

    path('beverages', views.display_beverages, name='display_beverages'),
    path('snacks', views.display_snacks, name='display_snacks'),
    path('cans', views.display_cans, name='display_cans'),

    path('addbeverages', views.add_beverages, name='add_beverages'),
    path('addsnacks', views.add_snacks, name='add_snacks'),
    path('addcans', views.add_cans, name='add_cans'),

    path('beverages/delete/<id>', views.del_beverages, name='del_beverages'),
    path('snacks/delete/<id>', views.del_snacks, name='del_snacks'),
    path('cans/delete/<id>', views.del_cans, name='del_cans'),

    path('beverages/edit/<id>', views.edit_beverages, name='edit_beverages'),
    path('snacks/edit/<id>', views.edit_snacks, name='edit_snacks'),
    path('cans/edit/<id>', views.edit_cans, name='edit_cans'),

    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

"""
    path('login',views.loginpage, name='login'),
    path('logout', views.logoutuser, name='logout'),
    path('register',views.registerpage, name='register'),


    path('add_item', views.additem, name='additem'),
    path('delete/<id>', views.deleteitem, name='deleteitem'),
    path('edit/<id>', views.edititem, name='edititem'),
"""