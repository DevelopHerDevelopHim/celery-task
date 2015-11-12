#!/usr/bin/env python
# -*- coding: utf-8 -*-

from celery import Celery

results = []
celery = Celery()
celery.config_from_object('celeryconfig')