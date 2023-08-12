from django.shortcuts import render, redirect
from .forms import SignUpForm, LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, FormView, CreateView
from .models import Vehicle




def index(request):
    return render(request, 'index.html')


def register(request):
    msg = None
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            msg = 'user created'
            return redirect('login_view')
        else:
            msg = 'form is not valid'
    else:
        form = SignUpForm()
    return render(request,'register.html', {'form': form, 'msg': msg})


def login_view(request):
    form = LoginForm(request.POST or None)
    msg = None
    if request.method == 'POST':
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None and user.is_superadmin:
                login(request, user)
                return redirect('superadminpage')
            elif user is not None and user.is_customer:
                login(request, user)
                return redirect('customer')
            elif user is not None and user.is_admin:
                login(request, user)
                return redirect('admin')
            else:
                msg= 'invalid credentials'
        else:
            msg = 'error validating form'
    return render(request, 'login.html', {'form': form, 'msg': msg})




def admin(request):
    return render(request,'superadmin.html')


def customer(request):
    return render(request,'customer.html')


def employee(request):
    return render(request,'admin.html')



class VehicleList(ListView):
    model = Vehicle
    context_object_name = 'vehicles'
    template_name = 'listview.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        context['vehicle'] = context['vehicle'].filter(user=self.request.user)
        context['count'] = context['vehicle'].filter(completed=False).count()

        return context

class VehicleCreate(LoginRequiredMixin, CreateView):
        model = Vehicle
        fields = '__all__'
        success_url = reverse_lazy('vehicle')
        template_name = 'vehiclecreate.html'

        def form_valid(self, form):
            form.instance.user = self.request.user
            return super(VehicleCreate, self).form_valid(form)





class VehicleUpdate(LoginRequiredMixin, UpdateView):
    model = Vehicle
    fields = '__all__'
    success_url = reverse_lazy('vehicle')
    template_name = 'vehiclecreate.html'
