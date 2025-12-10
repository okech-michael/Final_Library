from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def sign(request):
    return render(request, 'sign.html')

def dashboard(request):
    return render(request, 'dashboard.html')

def payment(request):
    return render(request, 'payment.html')

def reset_password(request):
    return render(request, 'reset_password.html')

def recommendations(request):
    return render(request, 'recommendations.html')

def cart_view(request):
    return render(request, 'cart.html')

def view_all(request):
    return render(request, 'viewall.html')

def cart_view(request):
    return render(request, 'cart.html')

def user_profile(request):
    return render(request, 'userprofile.html')

def about(request):
    return render(request, 'about.html')

def science(request):
    return render(request, 'science.html')

def fiction(request):
    return render(request, 'fiction.html')

def history(request):
    return render(request, 'history.html')

def about(request):
    return render(request, 'about.html')

def help(request):
    return render(request, 'help.html')

def terms(request):
    return render(request, 'terms.html')

def contact(request):
    return render(request, 'contact.html')

def notifications(request):
    return render(request, 'notifications.html')

def logout(request):
    return render(request, 'logout.html')

def search(request):
    return render(request, 'search.html')

def favorites(request):
    return render(request, 'favorites.html')

def technology(request):
    return render(request, 'technology.html')

def view_all(request):
    return render(request, 'viewall.html')

def cart_view(request):
    return render(request, 'cart.html')

def science(request):
    return render(request, 'science.html')
 
 
def history(request):
    return render(request, 'history.html')

def technology(request):
    return render(request, 'technology.html')

def viewall(request):
    return render(request, 'viewall.html')



from django.shortcuts import render
from .models import Book, Subscription, UserProfile, Cart   

def dashboard(request):
    books = Book.objects.all()   # Fetch ALL books from database
    return render(request, 'dashboard.html', {'books': books})

def reset_password(request):
    subscriptions = Subscription.objects.filter(user=request.user)
    return render(request, 'reset_password.html', {'subscriptions': subscriptions})

def user_profile(request):
    user_profile = UserProfile.objects.get(user=request.user)
    return render(request, 'userprofile.html', {'user_profile': user_profile})

def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    return render(request, 'cart.html', {'cart_items': cart_items})



from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login as auth_login
from django.contrib import messages

def sign(request):
    if request.method == 'POST':
        # FIXED: Changed .get[] to .get()
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        confirm_password = request.POST.get('confirm_password', '')
        email = request.POST.get('email', '')
        
        # Validate all fields are filled
        if not all([username, password, email]):
            messages.error(request, 'All fields are required')
            return render(request, 'sign.html')
        
        # Validate passwords match
        if password != confirm_password:
            messages.error(request, 'Passwords do not match')
            return render(request, 'sign.html')
        
        # Check if user already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, 'Username already exists')
            return render(request, 'sign.html')
        
        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, 'Email already exists')
            return render(request, 'sign.html')
        
        try:
            # Create new user (create_user automatically saves, no need for .save())
            user = User.objects.create_user(username=username, password=password, email=email)
            
            # Automatically log the user in after sign up
            auth_login(request, user)  # Use auth_login instead of login
            messages.success(request, f'Welcome {username}! Your account has been created.')
            return redirect('dashboard')
        except Exception as e:
            messages.error(request, f'Error creating account: {str(e)}')
            return render(request, 'sign.html')
    
    return render(request, 'sign.html')


# FIXED: Renamed function to avoid conflict with Django's login function
def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        
        # Validate fields
        if not username or not password:
            messages.error(request, 'Both username and password are required')
            return render(request, 'login.html')
        
        user = authenticate(request, username=username, password=password)
        if user is not None:
            auth_login(request, user)  # Use auth_login instead of login
            messages.success(request, f'Welcome back, {username}!')
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password')
            return render(request, 'login.html')
    
    return render(request, 'login.html')


        
        



# Create your views here.
