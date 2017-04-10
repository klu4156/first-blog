from django import forms
from .models import Post

#modelform is from Django, tells Django form saves to model
class PostForm(forms.ModelForm):
	class Meta: #tells Django which model to use
		model = Post
		fields = ('title', 'text',) #only want title and text exposed to form user
		#author is logged in user, created date is current time