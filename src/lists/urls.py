"""
URL configuration for superlists project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.urls import path
from lists import views


urlpatterns = [
    path("new", views.new_list, name="new_list"),
    # URLs without a trailing slash are "action" URLs which modify the database.
    path("<int:list_id>/", views.view_list, name="view_list"),
    # We adjust the regular expression for our URL to include a capture group, <int:list_id>, which will match any
    # numerical characters, up to the following /, The captured id will get passed to the view as an argument.
    # path("<int:list_id>/add_item", views.add_item, name="add_item"),
]
#  cp superlists/urls.py lists/
