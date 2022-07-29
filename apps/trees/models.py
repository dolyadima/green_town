from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.postgres.fields import ArrayField
from django.utils.crypto import get_random_string


def get_id_trees():
    return get_random_string(32)


class Tree(models.Model):
    registration_number = models.CharField(_('регистрационный номер'), max_length=255, default=get_id_trees)
    x_coord = models.FloatField(_('широта'), default=0.0)  # latitude
    y_coord = models.FloatField(_('долгота'), default=0.0)  # longitude
    crown_radius = models.FloatField(_('радиус кроны'), default=0.0)
    age = models.PositiveIntegerField(_('возраст'), default=0)

    class Types(models.IntegerChoices):
        PIHTA = (1, _('пихта'))
        EL = (2, _('ель'))
        SOSNA = (3, _('сосна'))
        LISTVENNICA = (4, _('лиственница'))
        BEREZA = (5, _('берёза'))
        LIPA = (6, _('липа'))
        DUB = (7, _('дуб'))
        OSINA = (8, _('осина'))
        KLEN = (9, _('клён'))
        KASHTAN = (10, _('каштан'))
    type = models.PositiveSmallIntegerField(_('вид'), choices=Types.choices, default=Types.KASHTAN)

    class Condition(models.IntegerChoices):
        GOOD = (1, _('хорошее'))
        MIDDLE = (2, _('среднее'))
        BAD = (3, _('плохое'))
    condition = models.PositiveSmallIntegerField(_('состояние'), choices=Condition.choices, default=Condition.GOOD)

    photo_path = models.FileField(_('фото'), default='/trees/img/000_tree.png')  # get from static and put into media
    list_tasks = ArrayField(models.CharField(max_length=255), blank=True, default=list)

    class Meta:
        verbose_name = 'Дерево'
        verbose_name_plural = 'Деревья'

    def __str__(self):
        return f'{self.get_type_display()}: {self.registration_number}'
