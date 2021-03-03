from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import User

# Create your models here.
class Incidencia(models.Model):
    class Tipo(models.TextChoices):
        CONSULTA    = '00', _('Consulta')
        ERROR       = '01', _('Error')
        CONTIZACION = '02', _('Cotización')
    
    class Estado(models.TextChoices):
        SIN_ASIGNAR = '00', _('Sin asignar')
        ASIGNADO    = '01', _('Asignado')
        RESUELTO    = '02', _('Resuelto')
        CANCELADO   = 'XX', _('Cancelado')
        DEVUELTO    = 'DV', _('Devuelto')

    inc_id                  = models.AutoField(primary_key=True)
    inc_usuario             = models.ForeignKey(User,related_name='User_cliente',on_delete=models.PROTECT,limit_choices_to={'groups__name':'Clientes'},null=True)
    inc_tipo                = models.CharField(max_length=2,choices=Tipo.choices,default='00')
    inc_descripcion         = models.CharField(max_length=255)
    inc_detalle             = models.TextField()
    inc_estado              = models.CharField(max_length=2,choices=Estado.choices,default='00')
    inc_fecha_apertura      = models.DateField(auto_now_add=True)
    inc_fecha_modificacion  = models.DateTimeField(auto_now=True)
    inc_fecha_cierre        = models.DateField(null=True,blank=True)
    inc_responsable         = models.ForeignKey(User,related_name='User_agente',on_delete=models.PROTECT,limit_choices_to={'groups__name': "Agentes"},null=True,blank=True)

    def __str__(self):
        return str(self.inc_id)+ " - " + str(self.inc_descripcion)
