from django.conf.urls import url
from . import views

urlpatterns=[
    url(r'^hello/$',views.hello,name='hello'),
    url(r'^post/(?P<post_id>\d+)/$',views.post,name='post'),
    url(r'^news/(?P<slug>[-\w]+)/$',views.news,name='news'),
    url(r'^$',views.index,name='item_index'),
    url(r'^(?P<item_id>[0-9]+)/edit/$',views.edit,name='item_edit'),
    url(r'^(?P<item_id>[0-9]+)/delete/$',views.delete,name='item_delete'),
    url(r'^(?P<item_id>[0-9]+)/add/wish_list/$',views.add_to_wish_list,name='item_add_wish_list'),
    url(r'^(?P<item_id>[0-9]+)/delete/wish_list/$',views.delete_from_wish_list,name='item_delete_wish_list'),
    url(r'^wish_list/$',views.wish_list_index,name='wish_list_index')
]
