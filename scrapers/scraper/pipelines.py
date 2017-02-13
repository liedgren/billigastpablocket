# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import sys
# Add the ptdraft folder path to the sys.path list
sys.path.append('../../billigastpablocket')
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "billigastpablocket.settings")

import django
django.setup()

import app.models as models
import re
import requests

class ItemPipeline(object):

	def process_item(self, item, spider):
		if len(models.Listing.objects.filter(name = item['name']).filter(price = item['price'])) == 0:
			b = models.Listing.objects.create(name = item['name'], price = item['price'], category = item['category'], location = item['location'])
			b.save()	
		else:
			pass		