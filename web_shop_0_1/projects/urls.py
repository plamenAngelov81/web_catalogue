from django.urls import path, include

from web_shop_0_1.projects.views import show_projects, ProjectDetailsView

urlpatterns = [
    path('projects/', include([
        path('', show_projects, name='projects'),
        path('details/<int:pk>', ProjectDetailsView.as_view(), name='project details'),
    ]))
]
