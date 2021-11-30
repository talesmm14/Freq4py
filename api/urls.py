from django.urls import path, include
from api.serializers import MyObtainTokenPairView
from api.views import ExportDocx, RegisterView, Schedule_Detail, Schedule_List, Sheet_Detail, Sheet_List, Titles_Detail, Titles_List, Values_Detail, Values_List


urlpatterns = [
    path('sheets/', Sheet_List.as_view(), name='sheet-view'),
    path('sheets/<int:pk>/', Sheet_Detail.as_view(), name='sheet-detail'),
    path('schedule/', Schedule_List.as_view(), name='schedule-list'),
    path('schedule/<int:pk>/', Schedule_Detail.as_view(), name='schedule-detail'),
    path('titles/', Titles_List.as_view(), name='titles-list'),
    path('titles/<int:pk>/', Titles_Detail.as_view(), name='titles-detail'),
    path('values/', Values_List.as_view(), name='values-list'),
    path('values/<int:pk>/', Values_Detail.as_view(), name='values-detail'),

    path('exportdocx/<int:pk>/', ExportDocx.as_view(), name='doc'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name='auth_register'),
]
