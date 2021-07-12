from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView
from .models import BlogPost


class IndexView(ListView):
    """トップページのビュー
    投稿記事を一覧表示するのでListViewを継承する

    Attributes:
    template_name: レンダリングするテンプレート
    context_object_name: object_listキーの別名を設定
    queryset: データベースのクエリ
    """
    #index.htmlをレンダリングする
    template_name = "index.html"
    #object_listキーの別名を設定
    context_object_name = 'orderby_records'
    #モデルBlogPostのオブジェクトにorder_by()を適用して
    #BlogPostのレコードを投稿日時の降順で並べ替える
    queryset = BlogPost.objects.order_by('-posted_at')

    #1ページに表示するレコードの件数
    paginate_by = 3

class BlogDetail(DetailView):
    """詳細ページのビューで投稿記事の詳細を表示するのでDetailViewを継承する
    Attributes:
    template_name: レンダリングするテンプレート
    Model: モデルのクラス
    """
    #post.htmlをレンダリングする
    template_name = 'post.html'
    #クラス変数modelにBlogPostを設定
    model = BlogPost

class ScienceView(ListView):
    template_name = 'science_list.html'
    model = BlogPost
    # object_listキーの別名を設定
    context_object_name = 'science_records'
    # caregory='science'のレコードを抽出して投稿日時の降順で並べ替える
    queryset = BlogPost.objects.filter(category='science').order_by('-posted_at')
    # 1ページに表示するレコードの件数
    pagenate_by = 2


class DailylifeView(ListView):
    template_name = 'dailylife_list.html'
    model = BlogPost
    # object_listキーの別名を設定
    context_object_name = 'dailylife_records'
    # caregory='science'のレコードを抽出して投稿日時の降順で並べ替える
    queryset = BlogPost.objects.filter(category='dailylife').order_by('-posted_at')
    # 1ページに表示するレコードの件数
    pagenate_by = 2


class MusicView(ListView):
    template_name = 'music_list.html'
    model = BlogPost
    # object_listキーの別名を設定
    context_object_name = 'music_records'
    # caregory='science'のレコードを抽出して投稿日時の降順で並べ替える
    queryset = BlogPost.objects.filter(category='music').order_by('-posted_at')
    # 1ページに表示するレコードの件数
    pagenate_by = 2




    
