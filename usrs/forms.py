# django
from django import forms
from django.contrib.admin.forms import forms as adminforms
# third party
from db_file_storage.form_widgets import DBClearableFileInput, \
    DBAdminClearableFileInput
# project
from .models import Book
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.core.exceptions import NON_FIELD_ERRORS

class ProfileBookForm(forms.ModelForm):
    class Meta:
        model = Book
        # exclude = ['md5s','ownr']
        fields = ['name','index',]
        


class BookForm(ProfileBookForm):
    encpt_key = forms.CharField(max_length=500)
    en_schm = forms.CharField(max_length=50)
    sharing = forms.CharField(max_length=500)
    class Meta(object):
        model = Book
        fields = ProfileBookForm.Meta.fields + ['encpt_key','en_schm','sharing',]
        widgets = {
            'index': DBClearableFileInput,
#            'pages': DBClearableFileInput,
#            'cover': DBClearableFileInput,
        }
        # exclude = ['md5s','ownr']
        
        # def clean(self):
        #     cleaned_data = super(BookForm, self).clean()
        #     if 'index' in self.errors:
        #         del self.errors['index']
        #     return cleaned_data
    # def clean(self):
    #     cleaned_data = super(BookForm,self).clean()
    #     name=self.cleaned_data['name']
    #     ownr=self.cleaned_data['ownr']
    #     index=self.cleaned_data['index']
    #     # ownr=self.cleaned_data['ownr']
    #     if Book.objects.filter(name=name,ownr=ownr):
    #         if Book.objects.filter(ownr=ownr,name=name,index=index):
    #             raise forms.ValidationError('Already exists bro!!')
    #         # else:
    #             # raise forms.ValidationError(index)
    #     return cleaned_data
    # def fun():
    # 	self.cleaned_data['name']=self.cleaned_data['name']+"1"

    # def validate_unique(self):
    #     exclude = self._get_validation_exclusions()
    #     # exclude.remove('index')
    #     # exclude.remove('ownr')
    #     try:
    #         self.instance.validate_unique(exclude=exclude)
    #     except ValidationError as e:
    #     	self._update_errors(e)
            
            # raise ValidationError('Bro please change it:')
        	# self.delete
        	# self.save
        # except IntegrityError:
        # 	self.save
            #     {
            #         NON_FIELD_ERRORS : [
            #            'Same exists dude',
            #         ],
            #     }
    #         # )
    # def save(self , commit=True):
    #     instance=super(BookForm,self).save(commit=False)
    #     if commit:
    #         cleaned_data = super(BookForm,self).clean()
    #         name=self.cleaned_data['name']
    #         ownr=self.cleaned_data['ownr']
    #         # if Book.objects.filter(name=name,ownr=ownr):
    #         return redirect('model_files:book.delete',kwargs={'pk': Book.objects.filter(name=name,ownr=ownr).first().pk})
    #         # instance.save()
    #     return instance
    # def delete:


class BookAdminForm(adminforms.ModelForm):
    class Meta(object):
        model = Book
        exclude = []
        widgets = {
            'index': DBAdminClearableFileInput,
#            'pages': DBAdminClearableFileInput,
#            'cover': DBAdminClearableFileInput,
        }
#class SoundDeviceForm(forms.ModelForm):
#    class Meta(object):
#        model = SoundDevice
#        exclude = []
