from django.db import models
import datetime
from django.core.exceptions import ValidationError


class Imovel(models.Model):
    # id = models.AutoField(primary_key=True)
    limite_hospedes = models.IntegerField(default=1)
    qtd_banheiros = models.IntegerField(default=1)
    aceita_pets = models.BooleanField(default=False)
    limpeza = models.DecimalField(max_digits=6, decimal_places=2, default=70.00)
    data_ativacao = models.DateField(default=datetime.date.today)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

# python manage.py makemigrations
# python manage.py migrate
# python manage.py loaddata imovel

class Anuncio(models.Model):
    imovel_anunciando = models.ForeignKey(Imovel,
        related_name="anuncios", on_delete=models.CASCADE)
    plataforma_anunciante = models.CharField(max_length=50)
    taxa_plataforma = models.DecimalField(max_digits=6, decimal_places=2, default=50.00)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Reserva(models.Model):
    anuncio_referencia = models.ForeignKey(Anuncio,
        related_name="reservas", on_delete=models.CASCADE)
    data_check_in = models.DateField(default=datetime.date.today)
    data_check_out = models.DateField(default=datetime.date.today)
    preco_total = models.DecimalField(max_digits=6, decimal_places=2, default=100.00)
    comentario = models.TextField(default='')
    numero_hospedes = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def save(self, *args, **kwargs):
        if self.data_check_out < self.data_check_in:
            raise ValidationError("Data de check-out inválida!")
        super(Reserva, self).save(*args, **kwargs)
