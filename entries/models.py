from django.db import models

# Import from Djangos authentication system
from django.contrib.auth.models import User


class Entry(models.Model):
    entry_title = models.CharField(max_length=50)
    entry_text = models.TextField()
    entry_date = models.DateTimeField(auto_now_add=True)
    entry_author = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        # Changes objects display name in Admin page
        verbose_name_plural = 'entries'
        
    # Returns string representation of object
    def __str__(self):
        return self.entry_title
