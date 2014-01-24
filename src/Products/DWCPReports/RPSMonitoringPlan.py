# -*- coding: utf-8 -*-
#
# File: RPSMonitoringPlan.py
#
# Copyright (c) 2009 by []
# Generator: ArchGenXML Version 2.4.1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'

from AccessControl import ClassSecurityInfo
from Products.Archetypes.atapi import *
from zope.interface import implements
import interfaces

from Products.CMFDynamicViewFTI.browserdefault import BrowserDefaultMixin

from Products.DWCPReports.config import *

##code-section module-header #fill in your manual code here

from Products.ATContentTypes.content.event import ATEvent
from Products.ATContentTypes.content.event import ATEventSchema

##/code-section module-header

copied_fields = {}
copied_fields['title'] = OrderedBaseFolderSchema['title'].copy()
copied_fields['title'].widget.description = "Example: AFG Monitoring Plan 2010-2012"
copied_fields['description'] = OrderedBaseFolderSchema['description'].copy()
copied_fields['description'].schemata = "default"
copied_fields['startDate'] = ATEventSchema['startDate'].copy()
copied_fields['startDate'].widget.label = "Period Start"
copied_fields['startDate'].widget.show_hm = False
copied_fields['endDate'] = ATEventSchema['endDate'].copy()
copied_fields['endDate'].widget.label = "Period End"
copied_fields['endDate'].widget.show_hm = False
copied_fields['endDate'].widget.future_years = 20
schema = Schema((

    copied_fields['title'],

    copied_fields['description'],

    copied_fields['startDate'],

    copied_fields['endDate'],

    DateTimeField(
        name='preparationDate',
        widget=DateTimeField._properties['widget'](
            show_hm=False,
            label="Preparation Date",
            label_msgid='DWCPReports_label_preparationDate',
            i18n_domain='DWCPReports',
        ),
    ),
    DateTimeField(
        name='revisionDate',
        widget=DateTimeField._properties['widget'](
            label="Revision Date",
            show_hm=False,
            label_msgid='DWCPReports_label_revisionDate',
            i18n_domain='DWCPReports',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

RPSMonitoringPlan_schema = OrderedBaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class RPSMonitoringPlan(OrderedBaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IRPSMonitoringPlan)

    meta_type = 'RPSMonitoringPlan'
    _at_rename_after_creation = True

    schema = RPSMonitoringPlan_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(RPSMonitoringPlan, PROJECTNAME)
# end of class RPSMonitoringPlan

##code-section module-footer #fill in your manual code here
##/code-section module-footer



