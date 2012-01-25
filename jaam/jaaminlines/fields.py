from django.db import models
from django import forms

from ckeditor.widgets import CKEditorWidget
from ckeditor.fields import RichTextField, RichTextFormField

class RichTextInlinesField(RichTextField):
	pass

class RichTextInlinesFormField(RichTextFormField):
	pass