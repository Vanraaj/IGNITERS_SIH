from django.contrib import admin
from .models import Classroom
from .models import Office
from .models import Miscellaneous
from .models import FacultyRoom

# Register your models here.

admin.site.register(Classroom)
admin.site.register(Office)
admin.site.register(Miscellaneous)
admin.site.register(FacultyRoom)
