from django import forms
from app.models import Node, Rule

class NodeForm(forms.ModelForm):
    class Meta:
        model = Node
        fields = ['type', 'operator', 'value', 'left', 'right']

class RuleForm(forms.ModelForm):
    class Meta:
        model = Rule
        fields = ['name', 'root_node']
