from upthor.views import FileUploadView

from django.conf.urls import url

urlpatterns = [
    # for Testing
    url('^thor-upload/', FileUploadView.as_view(), name='thor-file-upload'),
]
