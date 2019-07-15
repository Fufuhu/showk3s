from django.urls import path

from app.views.stream_view import StreamView
from app.views.logo_stream_view import LogoStreamView
from app.views.snapshot_view import SnapView
from app.views.index_view import IndexView
from app.views.logo_screen_view import LogoScreenView
from app.views.snapshot_screen_view import SnapshotScreenView

app_name = 'app'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('stream', StreamView.as_view(), name='stream'),
    path('logo', LogoStreamView.as_view(), name='logo'),
    path('snapshot', SnapView.as_view(), name='snapshot'),
    path('logoscreen', LogoScreenView.as_view(), name='logoscreen'),
    path('snapshotscreen', SnapshotScreenView.as_view(), name='snapshotscreen'),
]
