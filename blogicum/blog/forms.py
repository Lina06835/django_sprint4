from django import forms
from django.contrib.auth import get_user_model

from django.utils import timezone  
from django.core.exceptions import ValidationError
from datetime import datetime

from blog.models import Post, Comment
User = get_user_model()

class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name')

class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'text', 'pub_date', 'location', 'category', 'image', 'is_published')
        widgets = {
            'pub_date': forms.DateTimeInput(attrs={'type': 'datetime-local',
                                                   'value': datetime.now().strftime('%Y-%m-%dT%H:%M')})
        }
        help_texts = {
            'pub_date': 'Оставьте пустым для публикации сейчас. Можно установить будущую дату для отложенной публикации.',
        }
    # def clean_pub_date(self):
    #     pub_date = self.cleaned_data.get('pub_date')
    #     if pub_date and pub_date < timezone.now():
    #         raise ValidationError('Нельзя установить дату в прошлом!')
    #     return pub_date
    
class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('text',)