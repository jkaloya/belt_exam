from django.shortcuts import render, HttpResponse, redirect
from .models import User, Item
from django.contrib import messages

def index(request):
    return render(request, 'beltexamapp/index.html')

def validation(request):
    if request.method == "POST":
        user = User.Usermgr.filter(user_name = request.POST['user_name'])
        if user:
            messages.add_message(request, messages.INFO, 'User already exists, please login!')
            return redirect('/')
        else:
            result = User.Usermgr.register(request.POST['first_name'], request.POST['last_name'], request.POST['user_name'], request.POST['password'], request.POST['confirm_password'])
            if result[0] == True:
                request.session['user_id'] = result[1].id
                request.session['status'] = 'registered'
                return redirect('/welcome')
            else:
                error_msg = result[1]
                for i in range(len(error_msg)):
                    messages.add_message(request, messages.ERROR, error_msg[i])
                return redirect('/')
    else:
        return redirect('/')

def login(request):
    if request.method == "POST":
        user = User.Usermgr.filter(user_name = request.POST['user_name'])
        if not user:
            messages.add_message(request, messages.INFO, 'User does not exist, please Register!')
            return redirect('/')
        else:
            result = User.Usermgr.login(request.POST['user_name'], request.POST['password'])
            i = User.Usermgr.filter(user_name = request.POST['user_name'])
            if result[0] == True:
                request.session['user_id'] = i[0].id
                request.session['status'] = 'log'
                return redirect('/welcome')
            else:
                error_msg = result[1]
                for i in range(len(error_msg)):
                    messages.add_message(request, messages.ERROR, error_msg[i])
                return redirect('/')
    return redirect('/')

def welcome(request):
    user =  User.Usermgr.filter(id=request.session['user_id'])
    if user:
        items = Item.objects.filter(user=user)
        print items
        context = {'user': user[0], 'items': items}
        return render(request,'beltexamapp/welcome.html', context)


def add(request):
    return render(request, 'beltexamapp/add.html')

def add_item(request):
    return redirect ('/add')

def create(request):
    item = request.POST['item']
    if len(item) <3:
        messages.add_message(request, messages.INFO, 'Item/Product must be greater than 3 characters!')
        return redirect('/add')
    else:
        user =  User.Usermgr.filter(id=request.session['user_id'])
        item = Item.objects.filter(item=request.POST['item'])
        if item:
            item = item[0]
            return redirect('/welcome')
        else:
            item = Item.objects.create(item=request.POST['item'])
            print "hello"
            return redirect('/welcome')

def home(request):
    return redirect ('/welcome')

def logout(request):
    request.session.pop('user_id')
    return redirect ('/')
