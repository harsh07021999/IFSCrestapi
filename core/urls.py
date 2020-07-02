from django.urls import include,re_path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import DetailView, ListView

urlpatterns = {
    re_path(r'^ifsc/(?P<ifsc>[A-Za-z]{4}\w{7})$', DetailView.as_view()),
    re_path(r'^branches/(?P<city>.*)/(?P<bank>.*)$', ListView.as_view())
}

urlpatterns = format_suffix_patterns(urlpatterns)