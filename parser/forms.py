from django import forms
from . import models, rezka_parser, manas_parser


class ParserSiteForm(forms.Form):
    MEDIA_CHOICES = (
        ("rezka.ag", "rezka.ag"),
        ("manas.kg", "manas.kg")
    )

    media_type = forms.ChoiceField(choices=MEDIA_CHOICES)

    class Meta:
        fields = ['media_type']

    def parser_data(self):
        if self.data['media_type'] == 'rezka.ag':
            film_parser = rezka_parser.parsing()
            for film in film_parser:
                models.RezkaParser.objects.create(**film)
        elif self.data['media_type'] == 'manas.kg':
            film_parser = manas_parser.parser()
            for film in film_parser:
                models.ManasParser.objects.create(**film)
