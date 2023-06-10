from django.urls import path,include
from . import views
urlpatterns = [
path('',views.sch1,name='sch1'),
path('shomark',views.shomark,name='shomark'),
path('adds',views.adds,name='adds'),
path('addrow',views.addrow,name='addrow'),
path('chrow',views.chrow,name='chrow'),
path('addstud',views.addstud,name='addstud'),
path('shost',views.shost,name='shost'),
path('shost2',views.shost2,name='shost2'),
path('shost3',views.shost3,name='shost3'),
path('update1',views.update1,name='update1'),
path('shost5',views.shost5,name='shost5'),
path('shost6',views.shost6,name='shost6'),
path('login1',views.login1,name='login1'),
path('logout1',views.logout1,name='logout1'),
path('setting1',views.setting1,name='setting1'),
path('setting2',views.setting2,name='setting2'),
path('setting3',views.setting3,name='setting3'),
path('renrow',views.renrow,name='renrow'),
path('shoprod_helf',views.shoprod_helf,name='shoprod_helf'),
path('shoprod_helf2',views.shoprod_helf2,name='shoprod_helf2'),
]
