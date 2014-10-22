#!-*- coding: utf-8 -*-
from django.db import models

#TODO: navbar menu
class NavbarMenu(models.Model):
    class Meta:
        db_table = "navbarmenu"
        verbose_name = "Главное Меню"
    navbar_menu = models.CharField(max_length=50, verbose_name='Введите новое категорию в меню')


#TODO: about menu
class AboutMenu(models.Model):
    class Meta:
        db_table = "aboutmenu"
        verbose_name = " Выпадающие меню (About: Главное меню)"
    about_menu = models.CharField(max_length=50, verbose_name='Подпункты Меню')
#TODO: about level menu


#TODO: footerbar
class FooterBar(models.Model):
    class Meta:
        db_table = "footer"
        verbose_name = "Подвал"
    footer_bar = models.CharField(max_length=50, verbose_name='Пункты Меню (зеркало главного меню)')


#TODO: Slogan home
class SloganHome(models.Model):
    class Meta:
        db_table = 'sloganhome'
        verbose_name = "Слоган (Главная страница)"
    sloganHome_title = models.CharField(max_length= 300, verbose_name='Слоган Главная Стриница')

#TODO: slogan min home


#TODO: Baner home
class BanerHome(models.Model):
    class Meta:
        db_table = 'banerhome'
        verbose_name = "Баннер Главная страница"
    banerhome_title = models.CharField(max_length=50, verbose_name='Баннер заголовок')
    banerhome_body = models.CharField(max_length=100, verbose_name='Баннер текст')
    banerhome_images = models.CharField(max_length=50, verbose_name='Фон картинка')

#TODO: title article home
class TitleArticleHome(models.Model):
    class Meta:
        db_table = "titlearticlehome"

        verbose_name = "Заголовок Статья (Главная Страница)"
    titleArticleHome_title = models.CharField(max_length=150, verbose_name='Заголовок')

#TODO: main article home
class MainArticleHome(models.Model):
    class Meta:
        db_table = "mainarticlehome"
        verbose_name = "Тело статья (главная страница)"
    mainArticleHome_title = models.CharField(max_length=200, verbose_name='Заголовок главной статьи')
    mainArticleHome_body = models.TextField(verbose_name='Текст статьи')

#TODO: article second home
class ArticleSecondHome(models.Model):
    class Meta:
        db_table = "mainarticlesecondhome"
        verbose_name = "Доп.статья (Главная страница)"
    articleSecodHome_title = models.CharField(max_length=20, verbose_name='Заголовок доп. статьи')
    articleSecondHome_body = models.TextField(verbose_name='Текст стаьи')

#TODO: main article about
class MainArticleAbout(models.Model):
    class Meta:
        db_table = "mainarticleabout"
        verbose_name = "Главная Страница (Об этом)"
    mainArticleAbout_title = models.CharField(max_length=200)
    mainArticleAbout_body = models.TextField()

#TODO: article second about
class ArticleSecondAbout(models.Model):
    class Meta:
        db_table = "articlesecondabout"
        verbose_name = "Доп.статьи: (About page)"
    articleSecondAbout_body = models.TextField()
    articleSecondAbout_author = models.TextField()

#TODO: title team about
class TitleTeamAbout(models.Model):
    class Meta:
        db_table = "titleteamabout"
        verbose_name = "Команда (статья)"
    titleTeamAbout = models.CharField(max_length=30)
    titlePeople = models.CharField(max_length=50)
    titlePeople_body = models.TextField()

#TODO: link about
class LinkAbout(models.Model):
    class Meta:
        db_table = "linkabout"
        verbose_name = "Линки (About)"
    linkabout = models.CharField(max_length=50)

#TODO: product
class Product(models.Model):
    class Meta:
        db_table = "product"
        verbose_name = "Продукт"
    poduct_slogan = models.CharField(max_length=100)
    poductNameImages = models.CharField(max_length=50)

#TODO: project page
class ProjectPage(models.Model):
    class Meta:
        db_table = "project"
        verbose_name = "Проекты"
    project_slogan = models.CharField(max_length=100)
    projectArticle_title = models.CharField(max_length=100)
    projectArticle_preview = models.CharField(max_length=200)
    projectArticle_body = models.TextField()

#TODO: Contact

class Contact(models.Model):
    class Meta:
        db_table = "contact"
        verbose_name = "Контакты"
    contact_map_title = models.CharField(max_length=150)
    contact_article = models.TextField()
    contact_adress_index = models.CharField(max_length=150)
    contact_adress_city = models.CharField(max_length=150)
    contact_adress_street = models.CharField(max_length=150)
    contact_adress_office = models.CharField(max_length=150)
    contact_adress_telephone = models.CharField(max_length=150)
    contact_adress_mob = models.CharField(max_length=150)
    contact_adress_email = models.CharField(max_length=150)

#TODO: feedback
class Feedback(models.Model):
    class Meta:
        db_table = "feedback"
        verbose_name = "Форма обратной связи"
    feedback_name = models.CharField(max_length=200)
    feedback_email = models.CharField(max_length=200)
    feedback_phone = models.CharField(max_length=200)
    feedback_text = models.TextField()

