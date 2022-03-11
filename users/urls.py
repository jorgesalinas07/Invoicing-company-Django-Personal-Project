#Django
from django.urls import path

#Local
from . import views

app_name = 'users'

urlpatterns = [
    path(
        route='',
        view=views.login_view,
        name = "login"
    ),
    path(
        route='logout/',
        view=views.LogoutView.as_view(),
        name = "logout"
    ),
    path(
        route='signup/',
        view=views.SignupView.as_view(),
        name = "signup"
    ),
    path(
        route='profile/<int:pk>/',
        view=views.ClientDetailView.as_view(),
        name = "detail"
    ),
    path(
        route='update/<str:pk>/',
        view=views.UpdateProfileView.as_view(),
        name = "update"
    ),
        path(
        route='menu/<int:client_id>',
        view=views.menu,
        name = "menu"
    ),
    path(
        route='delete/<int:pk>',
        view=views.DeleteClientView.as_view(),
        name = 'delete'
    ),
    path(
        route='download/',
        view = views.downloadfile,
        name = 'download'
    ),
    path(
        route='import/',
        view = views.importfile,
        name = 'import'
    )
]