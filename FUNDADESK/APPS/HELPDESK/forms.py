from django import forms
from .models import Incidencia

class FormularioIncidencias(forms.ModelForm):
    class Meta:
        model = Incidencia
        fields = '__all__'
        labels = {'inc_usuario': 'USUARIO','inc_tipo':'TIPO','inc_descripcion':'DESCRIPCION','inc_detalle':'DETALLE','inc_estado':'ESTADO','inc_fecha_cierre':'CIERRE','inc_responsable':'RESPONSABLE'}