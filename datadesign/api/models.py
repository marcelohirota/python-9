from django.db import models
from django.core.validators import EmailValidator, MinLengthValidator, validate_ipv4_address, ValidationError


def level_validator(level):
    if level not in ['CRITICAL', 'DEBUG', 'ERROR', 'WARNING', 'INFO']:
        raise ValidationError(
            'Level not allowed. Use CRITICAL, DEBUG, ERROR, WARNING or INFO')


class User(models.Model):
    name = models.CharField('Nome', max_length=50)
    last_login = models.DateTimeField('Último login', auto_now=True)
    email = models.CharField(
        'E-mail', max_length=254, validators=[EmailValidator()])
    password = models.CharField(
        'Nome', max_length=50, validators=[MinLengthValidator(8)])

    def __str__(self):
        return self.name


class Agent(models.Model):
    name = models.CharField('Nome', max_length=50)
    status = models.BooleanField('Status')
    env = models.CharField('Env', max_length=20)
    version = models.CharField('Version', max_length=5)
    address = models.GenericIPAddressField(
        'IP Address', max_length=39, validators=[validate_ipv4_address])

    def __str__(self):
        return self.name


class Event(models.Model):
    level = models.CharField(
        'Level', max_length=20, validators=[level_validator])
    data = models.TextField('Data')
    arquivado = models.BooleanField('Arquivado')
    date = models.DateField('Date', auto_now=True)
    agent = models.ForeignKey(Agent, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField('Nome', max_length=50)

    def __str__(self):
        return self.name


class GroupUser(models.Model):
    group = models.ForeignKey(Group, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
