from django.urls import path, include
from api.serializers import MyObtainTokenPairView
from api.views import Sheet_Detail_View, Sheet_View, ExportDocx, RegisterView

urlpatterns = [
    path('sheet/', Sheet_View.as_view(), name='sheet-view'),
    path('sheet/<int:pk>/', Sheet_Detail_View.as_view(), name='sheet-detail'),
    path('exportdocx/<int:pk>/', ExportDocx.as_view(), name='doc'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name='auth_register'),
]
