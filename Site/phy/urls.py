from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from .views import *


urlpatterns = [
    path('', PhyMain.as_view(), name='phy_main'),
    # path('mechanics/', mechanics, name='mechanics'),
    path('mechanics/', Mechanics.as_view(), name='mechanics'),
    path('statics/', Statics.as_view(), name='statics'),
    path('<slug:formula_slug>/', template_formula, name='template_formula'),
    path("category/<slug:cat_slug>", CategoryPhysics.as_view(), name='category_physics')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
