from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from .models import Order, Customer


class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone', 'email', 'profile_pic']


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        # if we want specific fields
        # fileds = ['customer', 'product']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
