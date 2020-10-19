from django.conf.urls import url,include
from at import views

#Template Tagging

app_name = 'at'

urlpatterns = [
url(r'^help',views.help,name = 'help'),
url(r'^detective',views.detective,name='detective'),
]
