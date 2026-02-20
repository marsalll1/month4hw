from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from main.views import IndexView  # <-- импортируем CBV

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', IndexView.as_view(), name='index'),  # <-- используем .as_view()
    path('', include('myShop.urls')),   
    path('books/', include('book.urls')), 
    path('', include('resume.urls')),
    path('captcha/', include('captcha.urls')),
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)