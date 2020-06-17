from django.db import models


class User(models.Model):
    name = models.CharField('Nome', max_length=50)
    last_login = models.DateTimeField('Último login', auto_now=True)
    email = models.CharField('E-mail', max_length=254)
    password = models.CharField('Nome', max_length=50)


class Agent(models.Model):
    name = models.CharField('Nome', max_length=50)
    status = models.BooleanField('Status')
    env = models.CharField('Env', max_length=20)
    version = models.CharField('Version', max_length=5)
    address = models.GenericIPAddressField('IP Address', max_length=39)


class Event(models.Model):
    level = models.CharField('Level', max_length=20)
    data = models.TextField('Data')
    arquivado = models.BooleanField('Arquivado')
    date = models.DateField('Date', auto_now=True)
    agent_id = models.ForeignKey(Agent, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)


class Group(models.Model):
    name = models.CharField('Nome', max_length=50)


class GroupUser(models.Model):
    group_id = models.ForeignKey(Group, on_delete=models.CASCADE)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
