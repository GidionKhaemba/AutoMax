from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Listing
from.forms import ListingForm
from users.forms import LocationForm
from django.contrib import messages
from .filters import ListingFilter


@login_required
def home_view(request):
    listings=Listing.objects.all()
    listing_filter=ListingFilter(request.GET, queryset=listings)
    context={"listings":listings, 'listing_filter':listing_filter}
    return render(request, 'views/home.html', context)


def main_view(request):
    introduce = "AutoMax"
    return render(request, "views\main.html", {"introduce":introduce})

@login_required
def list_view(request):
    if request.method=="POST":
        try:
            listing_form=ListingForm(request.POST, request.FILES)
            location_form=LocationForm(request.POST)
            if listing_form.is_valid() and location_form.is_valid():
                listing=listing_form.save(commit=False)
                listing_location=location_form.save()
                listing.seller=request.user.profile
                listing.location=listing_location
                listing.save()  
                messages.info(request, f"{listing.model} listing posted succesfully")   
                return redirect('home')               
            
            
        except Exception as e:
            print(e)
            messages.error(request, 'an error occured during posting the listing')
        
    elif request.method=="GET":
        listing_form=ListingForm()
        location_form=LocationForm()
        context={'listing_form':listing_form, 'location_form':location_form}
        return render(request, "views/list.html", context)

@login_required
def listing_view(request, id):
    try:
        listing=Listing.objects.get(id=id)
        if listing is None:
            raise Exception  
    except Exception as e:      
    
        messages.error(request, f'invalid uuid {id} was provided for listing')    
        return redirect('home')    
    context={"listing":listing}
    return render(request, 'views/listing.html', context)

@login_required
def edit_view(request, id):
    try:
        listing = Listing.objects.get(id=id)
        if listing is None:
            raise Exception
        
        if request.method == "POST":
            listing_form = ListingForm(request.POST, request.FILES, instance=listing)   
            location_form = LocationForm(request.POST, instance=listing.location)   
            
            if listing_form.is_valid() and location_form.is_valid():
                listing_form.save() 
                location_form.save()
                messages.info(request, f'Listing updated successfully')
                return redirect('edit', id=id)
            else:
                messages.error(request, 'An error occurred while trying to edit the listing')
                return redirect('edit', id=id)
        else:
            listing_form = ListingForm(instance=listing)   
            location_form = LocationForm(instance=listing.location)  

        # Define context here after initializing the forms
        context = {
            "listing_form": listing_form,
            "location_form": location_form                 
        }
                 
    except Exception as e:
        messages.error(request, 'Error occurred during updating')         
        return redirect('edit', id=id)  # Handle the exception with a redirect
    
    return render(request, 'views/edit.html', context)



