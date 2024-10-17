from django.db import models

class Node(models.Model):
    TYPE_CHOICES = [
        ('operator', 'Operator'),
        ('operand', 'Operand'),
    ]

    OPERATOR_CHOICES = [
        ('AND', 'AND'),
        ('OR', 'OR'),
        ('>', 'Greater Than'),
        ('<', 'Less Than'),
        ('=', 'Equals'),
    ]

    type = models.CharField(max_length=10, choices=TYPE_CHOICES)
    operator = models.CharField(max_length=3, choices=OPERATOR_CHOICES, null=True, blank=True)
    left = models.ForeignKey('self', on_delete=models.CASCADE, related_name='left_child', null=True, blank=True)
    right = models.ForeignKey('self', on_delete=models.CASCADE, related_name='right_child', null=True, blank=True)
    value = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return f"Node({self.type}, {self.operator or self.value})"

class Rule(models.Model):
    name = models.CharField(max_length=100)
    root_node = models.ForeignKey(Node, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

