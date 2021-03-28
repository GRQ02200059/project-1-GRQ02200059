from django.test import TestCase

# Create your tests here.
md = markdown2.Markdown()
html1 = md.convert(text1)