from django.contrib import admin
from .models import Choice, Question


class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    # 新增順序欄位
    list_display = ("question_text", "pub_date", "was_published_recently", "type", "position")

    # 新增排序功能
    ordering = ("position",)

    # 新增變更順序的動作
    def change_position(self, request, queryset):
        # 取得所有選取的問題
        questions = queryset.all()

        # 根據問題的 ID 對問題進行排序
        questions = sorted(questions, key=lambda question: question.id)

        # 更新問題的順序
        for i, question in enumerate(questions):
            question.position = i
            question.save()

        # 顯示成功訊息
        self.message_user(request, "問題順序已更新成功。")

    # 新增動作
    actions = ["change_position"]

    # 新增只讀欄位
    readonly_fields = ("position",)

    list_filter = ["pub_date"]
    search_fields = ["question_text"]
    fieldsets = [
        (None, {"fields": ["question_text"]}),
        ("Date information", {"fields": ["pub_date"]}),
        ("Type", {"fields": ("type",)}),
    ]
    inlines = [ChoiceInline]


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)