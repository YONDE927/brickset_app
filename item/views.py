from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.template.response import TemplateResponse
from django.contrib.auth.decorators import login_required
from .models import Item
# Create your views here.
def hello(request):
    context={
        'headers':{
            'scheme':request.scheme,
            'path':request.path,
            'method':request.method,
            'content_length':request.META['CONTENT_LENGTH'],
            'http_accept':request.META['HTTP_ACCEPT'],
            'http_accept_language':request.META['HTTP_ACCEPT_LANGUAGE'],
            'user_agent':request.META['HTTP_USER_AGENT'],
            'remote_addr':request.META['REMOTE_ADDR'],
        }
    }
    return TemplateResponse(request,'item/header.html',context)

def post(request,post_id):
    return HttpResponse('post_idは = {0}です。'.format(post_id))

def news(request,slug):
    return HttpResponse('slugは = {}です。'.format(slug))

@login_required
def edit(request,item_id):
    item=get_objiect_or_404(Item,id=item_id)
    if request.method is 'POST':
        form=ItemForm(request.POST,instance=item)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('item_index'))
    else:
        form=ItemForm(instance=item)
    context={"form":form,"item":item}
    TemplateResponse(request,'item/edit.html',context=context)

@login_required
@require_POST
def delete(request,item_id):
    item=get_objiect_or_404(Item,id=item_id)
    item.delete()
    return HttpResponse(reverse('item_index'))

@login_required
def index(request):
    context={'items':Item.objects.all()}
    return TemplateResponse(request,'item/list.html',context=context)

@login_required
@require_POST
def add_to_wish_list(request,item_id):
    item = get_object_or_404(item, id=item_id)
    wish_list, created=WishList.object.get_or_create(user=request.user)
    wish_list.items.add(item)
    return HttpResponseRedirecti(reverse('wish_list_index'))

@login_required
@require_POST
def delete_form_wish_list(request, item_id):
    item = get_object_or_404(item,id=item_id)
    wish_list, created= WishList.objects.get_or_create(user=request.user)
    wish_list.items.remove(item)
    return HttpResponseRedirect(reverse('wish_list_index'))

@login_required
def wish_list_index(request):
    wish_list, created = WishList.objects.get_or_create(user=request.user)
    context={'items': wish_list.items.all()}
    return TemplateResponse(request, 'wish_list/list.html', context=context)
