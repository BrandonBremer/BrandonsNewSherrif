from django import forms
from .models import Post
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('bounty', 'location', 'daterequested', 'general_location')

class LocationForm(forms.Form):
    LOCATIONS= [
    ('ALL', 'All Posts'),
    ('BICE', 'Bice House'),
    ('BOND', 'Bond House'),
    ('BROWN', 'Brown College'),
    ('COPELEY', 'Copeley Apartments'),
    ('SHEA', 'French House/Spanish House/Shea House'),
    ('GOOCH','Gooch Dillard/ Hereford'),
    ('GRANDMARC', 'GrandMarc At the Corner'),
    ('HEREFORD', 'Hereford College'),
    ('IRC', 'International Residential College'),
    ('JPA', 'JPA'),
    ('LAMBETH', 'Lambeth Field Apartments'),
    ('LARK', 'Lark on Main'),
    ('NEW_DORMS', 'New Dorms'),
    ('OLD_DORMS', 'Old Dorms'),
    ('PRESTON', 'Preston Avenue Area'),
    ('FLATS', 'The Flats at West Village'),
    ('LAWN', 'The Lawn'),
    ('STANDARD', 'The Standard')
    ]
    location_choice= forms.CharField(label='Filter by Location', widget=forms.Select(choices=LOCATIONS))
    sort_options = [
        ('bounty', 'By Pay'),
        ('daterequested', "Most to Least Urgent"),
        ('dateposted', 'Newest First'),
        ('old', 'Oldest First'),
    ]
    sorter = forms.CharField(label='Show First:', widget = forms.Select(choices=sort_options))
