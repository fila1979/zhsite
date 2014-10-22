from django.contrib import admin
from zhapp.models import *



class NavbarMenuAdmin(admin.ModelAdmin):
    fields = ['navbar_menu']
    list_filter = ['navbar_menu']



admin.site.register(NavbarMenu, NavbarMenuAdmin)
admin.site.register(AboutMenu)
admin.site.register(FooterBar)
admin.site.register(SloganHome)
admin.site.register(BanerHome)
admin.site.register(TitleArticleHome)
admin.site.register(MainArticleHome)
admin.site.register(ArticleSecondHome)
admin.site.register(MainArticleAbout)
admin.site.register(ArticleSecondAbout)
admin.site.register(TitleTeamAbout)
admin.site.register(LinkAbout)
admin.site.register(Product)
admin.site.register(ProjectPage)
admin.site.register(Contact)
admin.site.register(Feedback)

