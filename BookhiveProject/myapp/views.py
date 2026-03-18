from django.shortcuts import render, redirect
from django.contrib import messages
from .models import UserRegistrationModel


# ---------------- REGISTER ----------------
def UserRegister(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        loginid = request.POST.get('loginid')
        password = request.POST.get('password')
        mobile = request.POST.get('mobile')
        email = request.POST.get('email')
        locality = request.POST.get('locality')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')

        if UserRegistrationModel.objects.filter(loginid=loginid).exists():
            messages.error(request, 'Login ID already exists')
            return render(request, 'UserRegistrations.html')

        UserRegistrationModel.objects.create(
            name=name,
            loginid=loginid,
            password=password,
            mobile=mobile,
            email=email,
            locality=locality,
            address=address,
            city=city,
            state=state
        )

        messages.success(request, 'Account created successfully. Please login.')
        return redirect('UserLogin')

    return render(request, 'UserRegistrations.html')