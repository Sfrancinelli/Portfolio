from django.db import models


# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='project_images/')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Proyectos"
        verbose_name_plural = "Proyectos"

    def __str__(self):
        return self.title


class Tag(models.Model):
    name = models.CharField(max_length=50)

    class Meta:
        verbose_name = "Etiquetas"
        verbose_name_plural = "Etiquetas"

    def __str__(self):
        return self.name


class ProjectTag(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.project.title} - {self.tag.name}"


class Contact(models.Model):
    name = models.CharField(max_length=155, verbose_name='Nombre')
    email = models.EmailField(max_length=100, verbose_name='Email')
    message = models.CharField(max_length=800, verbose_name='Mensaje')
    sent = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de envío")

    class Meta:
        verbose_name = "Contactos"
        verbose_name_plural = "Contactos"

    def __str__(self):
        return self.asignatura
