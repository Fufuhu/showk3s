from django.urls import path

from app.views.stream_view import StreamView
from app.views.logo_stream_view import LogoStreamView


urlpatterns = [
    path('stream', StreamView.as_view(), name='stream'),
    path('logo', LogoStreamView.as_view(), name='logo'),

]
