from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render,get_object_or_404,redirect
from django.urls import reverse
from commerce import settings
import datetime
from django.contrib import messages
from django.utils import timezone
from django.views import generic
from django.views.generic import ListView
from.forms import CreateForm

from .models import User,Auctions,Bids,Comment,Watchlist


def Categories(request):
    return render(request, "auctions/categories.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def CreateListing(request):
    submitted = False
   
    if request.method == "POST":
        form = CreateForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = CreateForm()
        if 'submitted' in request.GET:
            submitted = True
    return render(request,"auctions/CreateListing.html",context={'form':form,'submitted':submitted})




# This is the index page
class AuctionsListView(generic.ListView):
    model = Auctions
    #paginate_by = 5
    context_object_name = 'active_list'   
    queryset = Auctions.objects.all()
    template_name = "auctions/index.html"
    

class AuctionsDetailView(generic.DetailView):
    model = Auctions


def watchlist_add(request, auctions_id):
    pass


from django.views.generic.edit import CreateView
from django.urls import reverse_lazy

from .models import Bids

class BidsCreate(CreateView):
    model = Bids
    fields = ['user_id', 'auctions_id', 'value']
    initial = {'date_of_death': '11/06/2020'}


"""
class User(AbstractUser):
    pass

class Product(models.Model):
    title=models.CharField(max_length=50)
    desc=models.TextField()
    initial_amt=models.IntegerField()
    image=models.ImageField(upload_to='product')
    category=models.CharField(max_length = 20, choices =CHOICES)
    def __str__(self):
        return f"Item ID: {self.id} | Title: {self.title}"

class Watchlist(models.Model):
   user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
   item = models.ManyToManyField(Product)
   def __str__(self):
       return f"{self.user}'s WatchList"
Here the products and watchlist are linked by many to many field since a product can be present in multiple user's watchlists and a user can have multiple items in the watchlist.

views.py

adding the product in the watchlist

def watchlist_add(request, product_id):
    item_to_save = get_object_or_404(Product, pk=product_id)
    # Check if the item already exists in that user watchlist
    if Watchlist.objects.filter(user=request.user, item=item_id).exists():
        messages.add_message(request, messages.ERROR, "You already have it in your watchlist.")
        return HttpResponseRedirect(reverse("auctions:index"))
    # Get the user watchlist or create it if it doesn't exists
    user_list, created = Watchlist.objects.get_or_create(user=request.user)
    # Add the item through the ManyToManyField (Watchlist => item)
    user_list.item.add(item_to_save)
    messages.add_message(request, messages.SUCCESS, "Successfully added to your watchlist")
    return render(request, "auctions/watchlist.html")
The button can be added like this:

<a href="{% url 'watchlist' auctions.id %}" role="button" class="btn btn-outline-success btn-lg">Add to Watchlist</a>







if request.POST['title'] and request.POST['body'] and request.POST['price']:

             auction = Auctions()
             auction.title = request.POST['title']
             auction.body = request.POST['body']
             auction.Price = request.POST['price']
             
             auction.pub_date = timezone.datetime.now()
             auction.save()
             return redirect('index')
         else:
            return render(request, 'auctions/CreateListing.html',{'error':'All the field must be filled'})
    else:
        return render(request,"auctions/CreateListing.html")



watchlist
    item_to_save = get_object_or_404(Auctions, pk=auctions_id)
    # Check if the item already exists in that user watchlist
    if Watchlist.objects.filter(user=request.user, item=auctions_id).exists():
        messages.add_message(request, messages.ERROR, "You already have it in your watchlist.")
        return HttpResponseRedirect(reverse("index"))
    # Get the user watchlist or create it if it doesn't exists
    user_list, created = Watchlist.objects.get_or_create(user=request.user)
    # Add the item through the ManyToManyField (Watchlist => item)
    user_list.item.add(item_to_save)
    messages.add_message(request, messages.SUCCESS, "Successfully added to your watchlist")
    return render(request, "auctions/watchlist.html")



"""