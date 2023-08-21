from django.urls import path

from .views import *

urlpatterns = [
    path('user/<int:tg_id>', UserGetView.as_view()),
    path('user/create', UserCreateView.as_view()),
    path('user/update/<int:tg_id>', UserUpdateView.as_view()),
    path('bonus', BonusView.as_view()),
    path('prods', ProductListView.as_view()),
    path('prods/<int:id>', ProductGetView.as_view()),
    path('news', NewsListView.as_view()),
    path('news/<int:id>', NewsGetView.as_view()),
]
