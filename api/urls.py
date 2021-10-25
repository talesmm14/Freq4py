from django.urls import path
from api.views import Sheet_Detail_View, Sheet_View, ExportDocx

urlpatterns = [
    path('api/sheet/', Sheet_View.as_view(), name='sheet-view'),
    path('api/sheet/<int:pk>/', Sheet_Detail_View.as_view(), name='sheet-detail'),
    path('teste/<int:pk>/', ExportDocx.as_view(), name='doc')
]
