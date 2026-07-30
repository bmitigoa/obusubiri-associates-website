from django.contrib import admin

from .models import TrainingIntro


@admin.register(TrainingIntro)
class TrainingIntroAdmin(admin.ModelAdmin):
    fields = ('heading', 'lead', 'pullquote')

    def has_add_permission(self, request):
        # Only one row is allowed; hide the Add button when it already exists.
        return not TrainingIntro.objects.exists()

    def has_delete_permission(self, request, obj=None):
        return False
