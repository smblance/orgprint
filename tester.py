# -*- coding: utf-8 -*-

import json

with open('supplies.json','r') as f:
	supplies = json.load(f)

for item in supplies:
	if u'Производитель' in item['data']:
		if item['data'][u'Производитель'] != 'BLOSSOM':
			print item['data'][u'Производитель']
	else:
		print item['data'].keys()
print 'finish'


