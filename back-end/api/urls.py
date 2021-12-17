from django.urls import path, include
from api.serializers import MyObtainTokenPairView
from api.views import ExportDocx, RegisterView, ScheduleDetail, ScheduleList, SheetDetail, SheetList, TitlesDetail, \
    TitlesList, ValuesDetail, ValuesList, NotWorkingDayList, NotWorkingDayDetail, NotWorkTypeList, NotWorkTypeDetail

urlpatterns = [
    path('sheets/', SheetList.as_view(), name='sheet-view'),
    path('sheets/<int:pk>/', SheetDetail.as_view(), name='sheet-detail'),
    path('schedules/', ScheduleList.as_view(), name='schedule-list'),
    path('schedules/<int:pk>/', ScheduleDetail.as_view(), name='schedule-detail'),
    path('notworkingdays/', NotWorkingDayList.as_view(), name='not-working-day-list'),
    path('notworkingdays/<int:pk>/', NotWorkingDayDetail.as_view(), name='not-working-day-detail'),
    path('notworkingtypes/', NotWorkTypeList.as_view(), name='not-working-day-list'),
    path('notworkingtypes/<int:pk>/', NotWorkTypeDetail.as_view(), name='not-working-day-detail'),
    path('titles/', TitlesList.as_view(), name='titles-list'),
    path('titles/<int:pk>/', TitlesDetail.as_view(), name='titles-detail'),
    path('values/', ValuesList.as_view(), name='values-list'),
    path('values/<int:pk>/', ValuesDetail.as_view(), name='values-detail'),

    path('exportdocx/<int:pk>/', ExportDocx.as_view(), name='doc'),
    path('login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('register/', RegisterView.as_view(), name='auth_register'),
]
