from django.db import models

class Option(models.Model):
    name = models.CharField('Nom', max_length=64)
    description = models.TextField('Description')
    price = models.FloatField('Prix option')

    def __str__(self):
        return self.name

class Contract(models.Model):
    reference = models.CharField('Réf.', max_length=16, unique=True, blank=True)
    startDate = models.DateField('Date début séjour')
    endDate = models.DateField('Date fin séjour')
    options = models.ManyToManyField(Option)
    price = models.FloatField('Prix du séjour')
    apartment = models.ForeignKey('Apartment', on_delete=models.CASCADE)
    customer = models.ForeignKey('Customer', on_delete=models.CASCADE)
    firmed = models.BooleanField('Contrat signé ?', default=False)
    createdAt = models.DateTimeField('Date de création', auto_now=False, auto_now_add=True)
    updatedAt = models.DateTimeField('Dernière modification', auto_now=True, auto_now_add=False)

    def __str__(self):
        return self.reference
    
    def save(self, *args, **kwargs):
        self.reference = self.startDate.strftime('%y%m%d') + '-' + self.apartment.reference
        super(Contract, self).save(*args, **kwargs)
