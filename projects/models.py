from django.db import models


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Categorías"
        verbose_name_plural = "Categorías"

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=100, verbose_name='Título')
    description = models.TextField(max_length=1050, verbose_name='Descripción')
    image = models.ImageField(upload_to='project_images/', blank=True, verbose_name='Imágen')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado')
    categories = models.ManyToManyField(Category)

    class Meta:
        verbose_name = "Proyectos"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50, verbose_name='Etiqueta')

    class Meta:
        verbose_name = "Etiquetas"
        verbose_name_plural = "Etiquetas"

    def __str__(self):
        return self.name


class ProjectTag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, verbose_name='Proyecto')
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE, verbose_name='Etiqueta')

    def __str__(self):
        return f"{self.project.title} - {self.tag.name}"


class Contact(models.Model):
    name = models.CharField(max_length=155, verbose_name='Nombre')
    email = models.EmailField(max_length=100, verbose_name='Email')
    company = models.CharField(max_length=85, verbose_name='Empresa')
    message = models.CharField(max_length=800, verbose_name='Mensaje')
    sent = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de envío")

    class Meta:
        verbose_name = "Contactos"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return f'Consulta de:{self.mame} / {self.email}'
