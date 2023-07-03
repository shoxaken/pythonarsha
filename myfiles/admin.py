from django.contrib import admin
from myfiles.models import Portfolio, Type, Baza , Team , Contact , Join


class AdminPortifolio(admin.ModelAdmin):
    list_display = ['id', 'name', 'company_name', 'deadline', 'type', 'picture1']


admin.site.register(Portfolio,AdminPortifolio)

class AdminType(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Type,AdminType)


class AdminServer(admin.ModelAdmin):
    list_display = ['id', 'name' , 'picture1' , 'description']


admin.site.register(Baza,AdminServer)



class AdminTeam(admin.ModelAdmin):
    list_display = ['id', 'name' , 'lovozimi' , 'description' , 'picture1' , 'link1' , 'link2' , 'link3' , 'link4' ,]


admin.site.register(Team,AdminTeam)




class AdminContact(admin.ModelAdmin):
    list_display = ['id', 'name' , 'email' , 'description' , 'subject']


admin.site.register(Contact,AdminContact)
# Register your models here.

class AdminJoin(admin.ModelAdmin):
    list_display = ['id', 'email']


admin.site.register(Join,AdminJoin)