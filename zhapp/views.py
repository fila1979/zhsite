from django.shortcuts import render
from django.shortcuts import render_to_response
from zhapp.models import *

# def banerhome_first(request):
#     baner = BanerHome.objects.get()
#     imp_title = baner.banerhome_title
#     imp_body = baner.banerhome_body
#
#     return render_to_response('index.html', {'baner_title': imp_title, 'baner_body': imp_body})


def index(request):
    slogan = SloganHome.objects.get()
    slogan_imp = slogan.sloganHome_title

    baner = BanerHome.objects.all()
    cont_baner = baner.order_by()

    slogan_article = TitleArticleHome.objects.get()
    slogan_art_imp  = slogan_article.titleArticleHome_title

    mainarticle = MainArticleHome.objects.get()
    articlesecond = ArticleSecondHome.objects.get()

    return render_to_response(
        'index.html', {'slogan': slogan_imp,
                       'cont_baner': cont_baner,
                       'slogan_art': slogan_art_imp,
                       'mainarticle': mainarticle,
                       'articlesecond': articlesecond})




def about(request):

    main_art_about = MainArticleAbout.objects.get()

    art_second_about = ArticleSecondAbout.objects.all()
    art_second_imp = art_second_about.order_by()

    title_team = TitleTeamAbout.objects.all()
    title_team_imp =title_team.order_by()

    link_about = LinkAbout.objects.all()
    link_about_imp = link_about.order_by()

    return render_to_response(
        'about.html', {'main_art_about': main_art_about,
                      'art_second_imp': art_second_imp,
                      'title_ team_imp': title_team_imp,
                      'link_about_imp': link_about_imp})

def contacts(request):
    return render_to_response('contacts.html')

def product(request):
    return render_to_response('product.html')

def projects(request):
    return render_to_response('projects.html')


