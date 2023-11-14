# 페이지 요청시 전달되는  파라미터들을 쉽게
# 관리하기 위해 사용하는 클래스
from django import forms
from board.models import Question, Answer

class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question # 사용할 모델
        fields = ['subject','content'] # QuestionForm에서 사용할 Question 모델의 속성
        # widgets = {
        #     'subject': forms.TextInput(attrs={'class':'form-control'}),
        #     'content': forms.Textarea(attrs={'class':'form-control', 'rows':10}),
        # }
        labels = {
            'subject':'제목',
            'content':'내용',
        }

class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer 
        fields = ['content']
        labels = {
            'content':'답변내용'
        }