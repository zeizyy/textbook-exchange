from django.contrib import admin
from exchange.models import Book, User, Request
from import_export import resources
from import_export.admin import ImportExportModelAdmin, ImportExportMixin


# Register your models here.
# admin.site.register(Book)
# admin.site.register(User)
# admin.site.register(Request)

#Book
class BookResource(resources.ModelResource):
    class Meta:
        model = Book

class BookAdmin(ImportExportModelAdmin):
    resource_class = BookResource
    pass

admin.site.register(Book,BookAdmin)

#User
class UserResource(resources.ModelResource):
    class Meta:
        model = User

class UserAdmin(ImportExportModelAdmin):
    resource_class = UserResource
    pass

admin.site.register(User,UserAdmin)


#Request
class RequestResource(resources.ModelResource):
    class Meta:
        model = Request

class RequestAdmin(ImportExportModelAdmin):
    resource_class = RequestResource
    pass

admin.site.register(Request,RequestAdmin)