from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic
from django.shortcuts import redirect
from django.views.generic import ListView
from django.contrib.auth.models import User
from users.models import Profile
import operator

import json, functools

from shop.models import Food
from shop.models import Post
from shop.models import Quantity

from .forms import PostForm
from .forms import LocationForm

def checkout(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        cart = json.loads(request.POST['cart'])
        # create a form instance and populate it with data from the request:
        form = PostForm(request.POST)
        temp = form.save(commit=False)
        temp.status = "active"
        temp.customer = request.user
        temp.cost = functools.reduce(lambda sum, item : float(sum) + float(item['item_price']), cart, 0)
        temp.numitems = len(cart)
        temp.save()
        for item in cart:
            item_ref = Food.objects.get(id=item['id'])
            food_link = Quantity.objects.get_or_create(post=temp, food=item_ref)
            food_link[0].quantity_food += 1
            food_link[0].save()
        # check whether it's valid:
        #if temp.is_valid():
            # process the data in form.cleaned_data as required
        temp.save()
            # redirect to a new URL:
        return HttpResponseRedirect(reverse('allposts'))

    # if a GET (or any other method) we'll create a blank form
    else:
        post_form = PostForm()
        return render(request, 'shop/checkout.html', {'post_form': post_form})

def editpost(request, postid):
    if request.method == 'POST':
        post_form = PostForm(request.POST, instance=Post.objects.get(id=postid))
        if post_form.is_valid():
            post_form.save()
            #messages.success(request, _('Your profile was successfully updated!'))
            return redirect('allposts')
        else:
            #messages.error(request, _('Please correct the error below.'))
            pass
    else:
        post_form = PostForm(instance=Post.objects.get(id=postid))
    return render(request, 'shop/edit_post.html', {
        'post' : post_form
        })

def shop(request):
    shop_items = Food.objects.all()
    query = request.GET.get('search')
    if query:
        shop_items = Food.objects.filter(item_name__icontains=query)
    return render(request, 'shop/shop.html', {'Food_Items': shop_items})

def allposts(request):
    form = LocationForm()
    all_posts = Post.objects.all()
    full = True
    return render(request, 'shop/allposts.html', {'object_list': all_posts, 'form': form, 'full':full})

def claimpost(request, postid):
    post=Post.objects.get(id=postid)
    post.shopper=request.user
    post.status="claimed"
    post.save()
    return render(request, 'shop/allposts.html', {'object_list': Post.objects.all()})

def get_Post(request):
    all_posts = Post.objects.all() #Fallback
    if request.method == 'POST': #If it's post
        loc = request.POST.get('location_choice') #Grab my stuff from the form so I can use it
        sort = request.POST.get('sorter')
        r = True #Used for reversing the code. I know it's bad but it'll do
        if(sort == 'old'):
            sort = 'dateposted'
            r = False
        if loc != 'ALL': #If the location from the form isn't specified, we want all of the posts
            all_posts = Post.objects.filter(general_location=loc) #But if it is specified, we need to filter
        ordered = sorted(all_posts, key=operator.attrgetter(sort)) #Sort them based on the sorter.
        if(sort == 'bounty' or r): #sort goes least to most, but we want most to least on bounties
            ordered = reversed(ordered)
        form = LocationForm(request.POST)
        if form.is_valid():
            return render(request, 'shop/allposts.html', {'object_list': ordered, 'form': form})
    else:
        form = LocationForm()

    if len(all_posts) == 0:
        return render(request, 'shop/allposts.html', {'form': form})
    else:
        return render(request, 'shop/allposts.html', {'object_list': all_posts, 'form': form})


