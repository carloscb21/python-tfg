#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.db import models


BUILDINGCHOICES = (
    ('MARKET', 'Market'),
    ('COMPANY', 'Company'),
    ('HOSPITAL', 'Hospital'),
    ('OTHERS', 'Other'),
)

NFCCHOICES = (
    ('YES', 'Yes'),
    ('No', 'No'),
)


class TypeofDesign(models.Model):
    name = models.CharField(max_length=60)
    description = models.CharField(max_length=200)
    building = models.CharField(max_length=60, choices=BUILDINGCHOICES, default='OTHERS')

    def __unicode__(self):
        return unicode(self.name)


class Vertex(models.Model):
    is_origin_point = models.BooleanField(default=False)
    nfc_code = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    nfc_type = models.CharField(max_length=60, choices=NFCCHOICES, default='NO')
    number_floor = models.IntegerField(default=0)
    point_x = models.IntegerField(default=0)
    point_y = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % self.name


class Edge(models.Model):
    number_floor = models.IntegerField(default=0)
    vertex_one = models.ForeignKey(Vertex, on_delete=models.CASCADE, related_name='edge_vertex_one')
    vertex_two = models.ForeignKey(Vertex, on_delete=models.CASCADE, related_name='edge_vertex_two')
    weight = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % self.edge


class Map(models.Model):
    edge = models.ForeignKey(Edge)
    numbers_floor = models.IntegerField(default=0)

    def __unicode__(self):
        return u'%s' % self.edge


class DesignPlans(models.Model):
    is_active = models.BooleanField(default=False)
    type_design = models.ForeignKey(TypeofDesign)
    name = models.CharField(max_length=200, unique=True)
    map = models.OneToOneField(Map)
    description = models.TextField(blank=True)

    def __unicode__(self):
        return unicode(self.name) or u''







