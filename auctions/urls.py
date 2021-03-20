from django.urls import path

from . import views

urlpatterns = [
    path("category", views.Categories, name="categories"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.CreateListing, name="create"),
    path("", views.AuctionsListView.as_view(), name = "index"),
    path("listing/<int:pk>", views.AuctionsDetailView.as_view(), name = "list-detail"),
    path("watchlist/<int:auctions_id>", views.watchlist_add, name = "watchlist")
]
