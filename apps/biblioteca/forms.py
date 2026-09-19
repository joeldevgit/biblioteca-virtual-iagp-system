from django import forms

from .models import Documento


class DocumentoForm(forms.ModelForm):

    class Meta:
        model = Documento

        fields = [
            "titulo",
            "categoria",
            "institucion",
            "tipo",
            "autor",
            "tema",
            "descripcion",
            "fecha",
            "anio",
            "pdf",
            "pdf_url",
            "activo",
        ]

        widgets = {
            "titulo": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Título del documento",
                }
            ),

            "categoria": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "institucion": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "tipo": forms.Select(
                attrs={
                    "class": "form-select",
                }
            ),

            "autor": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Autor",
                }
            ),

            "tema": forms.TextInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Tema",
                }
            ),

            "descripcion": forms.Textarea(
                attrs={
                    "class": "form-control",
                    "rows": 4,
                    "placeholder": "Descripción del documento",
                }
            ),

            "fecha": forms.DateInput(
                attrs={
                    "class": "form-control",
                    "type": "date",
                }
            ),

            "anio": forms.NumberInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "Año",
                    "min": 1900,
                }
            ),

            "pdf": forms.ClearableFileInput(
                attrs={
                    "class": "form-control",
                    "accept": "application/pdf",
                }
            ),

            "pdf_url": forms.URLInput(
                attrs={
                    "class": "form-control",
                    "placeholder": "https://...",
                }
            ),

            "activo": forms.CheckboxInput(
                attrs={
                    "class": "form-check-input",
                }
            ),
        }