from django.shortcuts import render,redirect,get_object_or_404
from . forms import RegistrationForm,AuthenticateForm,ChangePasswordForm,UserProfileForm,AdminProfileForm,CustomerForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash
from django.views import View
from . models import Customer,Bike,Order,Cart

#====================================================== 

from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from django.urls import reverse

# ==================================================================================================================

# Create your views here.
def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request, 'contact.html')

def instagram(request):
    return render(request,'instagram.html')

def facebook(request):
    return render(request,'facebook.html')

def dashboard(request):
    return render(request,'dashboard.html')




# ============================================================================================================================

def registration(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            mf = RegistrationForm(request.POST)
            if mf.is_valid():
                mf.save()
                return redirect('registration')    
        else:
            mf  = RegistrationForm()
        return render(request,'registration.html',{'mf':mf})
    else:
        return redirect('profile')
    

# ============================================================================================================================
    
def log_in(request):
    if not request.user.is_authenticated: 
        if request.method == 'POST':        
            mf = AuthenticationForm(request,request.POST)
            if mf.is_valid():
                name = mf.cleaned_data['username']
                pas = mf.cleaned_data['password']
                user =authenticate(username=name, password=pas)
                if user is not None:
                    login(request, user)
                    return redirect('/')
        else:
            mf = AuthenticationForm()
        return render(request,'login.html',{'mf':mf})
    else:
        return redirect('profile')
    
# =====================================================================================================
def profile(request):
    if request.user.is_authenticated:  
        if request.method == 'POST':
            if request.user.is_superuser == True:
                mf = AdminProfileForm(request.POST,instance=request.user)
            else:
                mf = UserProfileForm(request.POST,instance=request.user)
            if mf.is_valid():
                mf.save()
        else:
            if request.user.is_superuser == True:
                mf = AdminProfileForm(instance=request.user)
            else:
                mf = UserProfileForm(instance=request.user)
        return render(request,'profile.html',{'name':request.user,'mf':mf})
    else:                                                
        return redirect('login')
    

def log_out(request):
    logout(request)
    return redirect('home')


def changepassword(request):                                                      
    if request.user.is_authenticated:                              
        if request.method == 'POST':                               
            mf =ChangePasswordForm(request.user,request.POST)
            if mf.is_valid():
                mf.save()
                update_session_auth_hash(request,mf.user)
                return redirect('profile')
        else:
            mf = ChangePasswordForm(request.user)
        return render(request,'changepassword.html',{'mf':mf})
    else:
        return redirect('login')


# ============================================Bikescategories======================================================================


class SportCategoriesView(View):
    def get(self,request):
        sportbike_category = Bike.objects.filter(category='SPORT_BIKE')  
        return render(request,'sportbike_categories.html',{'sportbike_category':sportbike_category})
    

    
class ElectricCategoriesView(View):
    def get(self,request):
        electricbike_category=Bike.objects.filter(category='ELECTRIC_BIKE')
        return render(request,'electricbike_category.html',{'electricbike_category':electricbike_category})
    

class ScotyCategoriesView(View):
    def get(self,request):
        electricscoty_category=Bike.objects.filter(category='ELECTRIC_SCOTY')
        return render(request,'electriscoty_category.html',{'electricscoty_category':electricscoty_category})

    
# ================================================BikeDetails===============================================================
    

 
    
class SportbikeDetailView(View):
    def get(self,request,id):      
        bike = Bike.objects.get(pk=id)

        
        if Bike.discounted_price !=0:    
            percentage = int(((bike.selling_price-bike.discounted_price)/bike.selling_price)*100)
        else:
            percentage = 0
        
            
        return render(request,'sportbike_details.html',{'bike':bike,'percentage':percentage})
    


class ElectricbikeDetailView(View):
    def get(self,request,id):      
        bike = Bike.objects.get(pk=id)

        
        if Bike.discounted_price !=0:    
            percentage = int(((bike.selling_price-bike.discounted_price)/bike.selling_price)*100)
        else:
            percentage = 0
        
            
        return render(request,'electricbike_details.html',{'bike':bike,'percentage':percentage})
    

class ElectricscotyDetailView(View):
    def get(self,request,id):      
        bike = Bike.objects.get(pk=id)

        
        if Bike.discounted_price !=0:    
            percentage = int(((bike.selling_price-bike.discounted_price)/bike.selling_price)*100)
        else:
            percentage = 0
        
            
        return render(request,'electricscoty_details.html',{'bike':bike,'percentage':percentage})
    

# =================================================BikeCategories====================================================================
    


class RoyalCategoriesView(View):
    def get(self,request):
        royal_category = Bike.objects.filter(category='ROYAL_BIKE')  
        return render(request,'royal.html',{'royal_category':royal_category})
    

class ShineCategoriesView(View):
    def get(self,request):
        shine_category = Bike.objects.filter(category='SHINE_BIKE')  
        return render(request,'shine.html',{'shine_category':shine_category})
    
class UnicornCategoriesView(View):
    def get(self,request):
        unicorn_category = Bike.objects.filter(category='UNICORN_BIKE')  
        return render(request,'unicorn.html',{'unicorn_category':unicorn_category})
    
class ActivaCategoriesView(View):
    def get(self,request):
        activa_category = Bike.objects.filter(category='ACTIVA_BIKE')  
        return render(request,'activa.html',{'activa_category':activa_category})
    
class AvengerCategoriesView(View):
    def get(self,request):
        avenger_category = Bike.objects.filter(category='AVENGER_BIKE')  
        return render(request,'avenger.html',{'avenger_category':avenger_category})
    
class DioCategoriesView(View):
    def get(self,request):
        dio_category = Bike.objects.filter(category='DIO_BIKE')  
        return render(request,'dio.html',{'dio_category':dio_category})

# ======================================================Addd_To_Cart===============================================================

def add_to_cart(request, id):     
    if request.user.is_authenticated:
        product = Bike.objects.get(pk=id)
        user=request.user                
        Cart(user=user,product=product).save()  
        return redirect('sportbikedetails', id)      
    else:
        return redirect('login')               

def view_cart(request):
    cart_items = Cart.objects.filter(user=request.user)     
    total =0
    delhivery_charge =2000
    for item in cart_items:
        item.product.price_and_quantity_total = item.product.discounted_price * item.quantity
        total += item.product.price_and_quantity_total
    final_price= delhivery_charge + total
    return render(request, 'view_cart.html', {'cart_items': cart_items,'total':total,'final_price':final_price})

def add_quantity(request, id):
    product = get_object_or_404(Cart, pk=id)   
    product.quantity += 1                        
    product.save()
    return redirect('viewcart')

def delete_quantity(request, id):
    product = get_object_or_404(Cart, pk=id)
    if product.quantity > 1:
        product.quantity -= 1
        product.save() 
    return redirect('viewcart')

def delete_cart(request,id):
    if request.method == 'POST':
        de = Cart.objects.get(pk=id)
        de.delete()
    return redirect('viewcart')



# =================address===================================================================

def address(request):
    if request.method == 'POST':
            print(request.user)
            mf =CustomerForm(request.POST)
            print('mf',mf)
            if mf.is_valid():
                user=request.user                
                name= mf.cleaned_data['name']
                address= mf.cleaned_data['address']
                city= mf.cleaned_data['city']
                state= mf.cleaned_data['state']
                pincode= mf.cleaned_data['pincode']
                print(state)
                print(city)
                print(name)
                Customer(user=user,name=name,address=address,city=city,state=state,pincode=pincode).save()
                return redirect('address')           
    else:
        mf =CustomerForm()
        address = Customer.objects.filter(user=request.user)
    return render(request,'address.html',{'mf':mf,'address':address})


def delete_address(request,id):
    if request.method == 'POST':
        de = Customer.objects.get(pk=id)
        de.delete()
    return redirect('address')




def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)      
    total =0
    delhivery_charge =2000
    for item in cart_items:
        item.product.price_and_quantity_total = item.product.discounted_price * item.quantity
        total += item.product.price_and_quantity_total
    final_price= delhivery_charge + total
    
    address = Customer.objects.filter(user=request.user)

    return render(request, 'checkout.html', {'cart_items': cart_items,'total':total,'final_price':final_price,'address':address})

#===================================== Payment ============================================

def payment(request):

    if request.method == 'POST':
        selected_address_id = request.POST.get('selected_address')

    host = request.get_host()   
    cart_items = Cart.objects.filter(user=request.user)      
    total =0
    delhivery_charge =2000
    for item in cart_items:
        item.product.price_and_quantity_total = item.product.discounted_price * item.quantity
        total += item.product.price_and_quantity_total
    final_price= delhivery_charge + total
    
    address = Customer.objects.filter(user=request.user)

#=============================== Paypal Code ===============================================
    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': final_price,
        'item_name': 'bike',
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('paymentsuccess', args=[selected_address_id])}",
        'cancel_url': f"http://{host}{reverse('paymentfailed')}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

#==========================================================================================================
    return render(request, 'payment.html', {'cart_items': cart_items,'total':total,'final_price':final_price,'address':address,'paypal':paypal_payment})

#===================================== Payment Success ============================================

def payment_success(request,selected_address_id):
    print('payment sucess',selected_address_id)   
                                                 
    user =request.user
    customer_data = Customer.objects.get(pk=selected_address_id,)
    cart = Cart.objects.filter(user=user)
    for c in cart:
        Order(user=user,customer=customer_data,bike=c.product,quantity=c.quantity).save()
        c.delete()
    return render(request,'payment_success.html')


#===================================== Payment Failed ============================================


def payment_failed(request):
    return render(request,'payment_failed.html')

#===================================== Order ====================================================

def order(request):
    ord=Order.objects.filter(user=request.user)
    return render(request,'order.html',{'ord':ord})


# ===============================================================================================


def buynow(request,id):
    bike = Bike.objects.get(pk=id)     
    delhivery_charge =2000
    final_price= delhivery_charge + bike.discounted_price
    
    address = Customer.objects.filter(user=request.user)

    return render(request, 'buynow.html', {'final_price':final_price,'address':address,'bike':bike})


def buynow_payment(request,id):

    if request.method == 'POST':
        selected_address_id = request.POST.get('buynow_selected_address')

    bike = Bike.objects.get(pk=id)     
    delivery_charge =2000
    final_price= delivery_charge + bike.discounted_price
    
    address = Customer.objects.filter(user=request.user)
    #================= Paypal Code ======================================

    host = request.get_host()   

    paypal_checkout = {
        'business': settings.PAYPAL_RECEIVER_EMAIL,
        'amount': final_price,
        'item_name': 'bike',
        'invoice': uuid.uuid4(),
        'currency_code': 'USD',
        'notify_url': f"http://{host}{reverse('paypal-ipn')}",
        'return_url': f"http://{host}{reverse('buynowpaymentsuccess', args=[selected_address_id,id])}",
        'cancel_url': f"http://{host}{reverse('paymentfailed')}",
    }

    paypal_payment = PayPalPaymentsForm(initial=paypal_checkout)

    #========================================================================

    return render(request, 'payment.html', {'final_price':final_price,'address':address,'bike':bike,'paypal':paypal_payment})

def buynow_payment_success(request,selected_address_id,id):
    print('payment sucess',selected_address_id)   
                                                  
    user =request.user
    customer_data = Customer.objects.get(pk=selected_address_id,)
    
    bike = Bike.objects.get(pk=id)
    Order(user=user,customer=customer_data,bike=bike,quantity=1).save()
   
    return render(request,'buynow_payment_success.html')








