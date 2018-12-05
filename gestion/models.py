from django.db import models

class Option(models.Model):
    name = models.CharField('Nom', max_length=64)
    description = models.TextField('Description')
    price = models.FloatField('Prix option')

    def __str__(self):
        return self.name + ' (' + str(self.price) + ' € )'

class Contract(models.Model):
    reference = models.CharField('Réf.', max_length=16, unique=True, blank=True)
    startDate = models.DateField('Date début séjour')
    endDate = models.DateField('Date fin séjour')
    options = models.ManyToManyField(Option)
    price = models.FloatField('Prix location')
#    totalPrice = models.FloatField('Prix total du séjour')
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

class Apartment(models.Model):
    CHAUDANNES = 'CHAUD'
    BUFFAZ = 'BUFF'
    ANDAGNE = 'AND'
    BUILDING_CHOICES = (
        (CHAUDANNES, 'Les Chaudannes'),
        (BUFFAZ, 'La Buffaz'),
        (ANDAGNE, 'Andagne'),
    )
    reference = models.SlugField('Réf.', max_length=32, unique=True, blank=True)
    building = models.CharField('Bâtiment', max_length=16, choices=BUILDING_CHOICES)
    number = models.PositiveSmallIntegerField('Numéro')
    capacity = models.PositiveSmallIntegerField('Capacité')
    floor = models.PositiveSmallIntegerField('Etage')
    numRooms = models.PositiveSmallIntegerField('Nombre de pièces')
    description = models.TextField('Description')
    isOpen = models.BooleanField('Réservable', default=True)

    def __str__(self):
        return self.reference

    def save(self, *args, **kwargs):
        self.reference = self.building + str(self.number)
        super(Apartment, self).save(*args, **kwargs)
    
    @classmethod
    def create(cls, building, number, isOpen):
        self.building = building
        self.number = number
        self.isOpen = isOpen
        self.save()

class Customer(models.Model):
    CIV_M = 'M.'
    CIV_MME = 'Mme'
    CIV_M_MME = 'M. ou Mme'
    CIV_CHOICES = (
        (CIV_M, 'Monsieur'),
        (CIV_MME, 'Madame'),
        (CIV_M_MME, 'Monsieur ou Madame'),
    )
    civility = models.CharField('Civilité', max_length=16, choices=CIV_CHOICES, blank=True)
    firstname = models.CharField('Prénom', max_length=64)
    lastname = models.CharField('Nom', max_length=64)
    email = models.EmailField(max_length=254, unique=True)
    phone = models.CharField('Téléphone', max_length=16, blank=True)
    address = models.TextField('Adresse')
    postalCode = models.IntegerField('Code postal')
    city = models.CharField('Ville', max_length=64)
    country = models.CharField('Pays', max_length=64, default='FRANCE')
    reminder = models.TextField('Pense bête', blank=True)

    def __str__(self):
        return self.civility + ' ' + self.lastname + ' ' + self.firstname
    
    def save(self, *args, **kwargs):
        self.lastname = self.lastname.upper()
        super(Customer, self).save(*args, **kwargs)
