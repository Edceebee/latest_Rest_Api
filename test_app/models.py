from django.db import models


class TestModel(models.Model):
    name = models.CharField(max_length=255, unique=True, null=True, blank=False, error_messages={
        "null": "this field cannot be null",
        "blank": "this field cannot be blank"})
    description = models.TextField()
    phone_number = models.PositiveIntegerField()
    is_live = models.BooleanField()
    amount = models.FloatField()
    user_name = models.CharField(max_length=250, editable=False, default="null")
    created_at = models.DateTimeField(auto_now=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    def __str__(self):
        # return f"{self.name} - {self.created_at.strftime('%H: %M:')}"
        return f"{self.name}"

    class Meta:
        verbose_name_plural = "Test Model"

    # def save(self, *args, **kwargs):
    #     self.user_name = f"{self.name} - {self.amount}"
    #     super().save(*args, **kwargs)


class ModelX(models.Model):
    test_content = models.ForeignKey(TestModel, on_delete=models.CASCADE, related_name="test_content")
    mileage = models.FloatField()
    created_at = models.DateTimeField(auto_now=True, )
    updated_at = models.DateTimeField(auto_now=True, )

    def __str__(self):
        return f"{self.test_content} - {self.mileage}"

    class Meta:
        verbose_name_plural = "ModelX"


# class ModelY(models.Model):
#     test_content = models.OneToOneField(TestModel, on_delete=models.CASCADE, related_name="test_content_y")
#     mileage = models.FloatField()
#     created_at = models.DateTimeField(auto_now=True, )
#     updated_at = models.DateTimeField(auto_now=True, )
#
#     def __str__(self):
#         return f"{self.test_content} - {self.mileage}"
#
#     class Meta:
#         verbose_name_plural = "ModelY"
