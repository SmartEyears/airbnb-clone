from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models


# 모델을 admin패널로 가져오려면 모델을 레지스터 해줘야한다.
# admin.site.register(models.User, CustomUserAdmin) 밑에 @decorator와 같이 모델을 레지스터 해주는 코드임
@admin.register(models.User)
class CustomUserAdmin(UserAdmin):

    """Custom User Admin"""

    fieldsets = UserAdmin.fieldsets + (
        (
            "CustomField",
            {
                "fields": (
                    "avatar",
                    "gender",
                    "bio",
                    "birthdate",
                    "language",
                    "currency",
                    "superhost",
                )
            },
        ),
    )

    list_filter = UserAdmin.list_filter + ("superhost",)

    list_display = (
        "username",
        "first_name",
        "last_name",
        "email",
        "is_active",
        "language",
        "currency",
        "superhost",
        "is_staff",
        "is_superuser",
    )

