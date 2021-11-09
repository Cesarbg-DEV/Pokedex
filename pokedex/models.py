from django.db import models

class Pokemon(models.Model):
    nombre = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    especie2 = models.CharField(max_length=50,null=True)
    altura = models.IntegerField(default=2)
    peso = models.IntegerField(default=2)
    habilidades = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    img = models.ImageField(upload_to='static/img/',null=True, blank=True)

    
    def __str__(self):
        return str(self.nombre) + " (" + str(self.id) + ") "

    class Meta:
        verbose_name = "Pokemon"
        verbose_name_plural = "Pokemones"

class Estadistica(models.Model):
    salud = models.IntegerField(default=2)
    ataque = models.IntegerField(default=2)
    defensa = models.IntegerField(default=2)
    velataque = models.IntegerField(default=2)
    veldefensa = models.IntegerField(default=2)
    velocidad =  models.IntegerField(default=2)
    total = models.IntegerField(default=2)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE,null=True)

class Evolucion(models.Model):
    nombreevo = models.CharField(max_length=50)
    especie = models.CharField(max_length=50)
    altura = models.IntegerField(default=2)
    peso = models.IntegerField(default=2)
    habilidades = models.CharField(max_length=50)
    genero = models.CharField(max_length=50)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE,null=True)

    def __str__(self):
        return str(self.nombreevo) + " (" + str(self.id) + ") "

    class Meta:
        verbose_name = "Evolucion"
        verbose_name_plural = "Evoluciones"

class Movimiento(models.Model):
    movimiento = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    poder = models.IntegerField(default=2)
    accion = models.CharField(max_length=50)
    efecto = models.CharField(max_length=50)
    pokemon = models.ForeignKey(Pokemon, on_delete=models.CASCADE,null=True)