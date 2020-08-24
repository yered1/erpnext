from __future__ import unicode_literals

from frappe import _


def get_data():
	return {
		'heatmap': True,
		'heatmap_message': _('This is based on transactions against this Customer. See timeline below for details'),
		'fieldname': 'customer',
		'non_standard_fieldnames': {
			'Payment Entry': 'party_name'
		},
		'transactions': [
			{
				'label': _('Pre Sales'),
				'items': ['Opportunity', 'Quotation']
			},
			{
				'label': _('Orders'),
				'items': ['Sales Order', 'Delivery Note', 'Sales Invoice']
			},
			{
				'label': _('Service Level Agreement'),
				'items': ['Service Level Agreement']
			},
			{
				'label': _('Payments'),
				'items': ['Payment Entry']
			},
			{
				'label': _('Support'),
				'items': ['Issue']
			},
			{
				'label': _('Projects'),
				'items': ['Project']
			},
			{
				'label': _('Pricing'),
				'items': ['Pricing Rule']
			},
			{
				'label': _('Subscriptions'),
				'items': ['Subscription']
			}
		]
	}
