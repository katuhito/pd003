from django.urls import path
from .import views

app_name = 'diary'

urlpatterns = [
    path('', views.IndexView.as_view(), name="index"),
    #リクエストされたURLが「blog-detail/レコードのid/」の場合はBlogDetailを実行
    #path(詳細ページのURL, viewsモジュールのBlogDetailを実行,URLパターンの名前を'blog-detail'にする)
    path('blog-detail/<int:pk>/', views.BlogDetail.as_view(), name='blog_detail'),
]