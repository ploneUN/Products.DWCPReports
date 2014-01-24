# -*- coding: utf-8 -*-
#
# File: RPSCPCode.py
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
copied_fields['title'] = BaseSchema['title'].copy()
copied_fields['title'].widget.label = "CPO Code and Biennium"
copied_fields['title'].widget.description = "Enter IRIS CPO Code here eg. CHN 101 06-07"
copied_fields['description'] = BaseSchema['description'].copy()
copied_fields['description'].schemata = "default"
copied_fields['description'].widget.description = "A brief summary of the the Country Practice Outcome. Example: Stop Exploitation at Work"
copied_fields['startDate'] = ATEventSchema['startDate'].copy()
copied_fields['startDate'].widget.description = "Select Jan 1 as the date"
copied_fields['startDate'].widget.label = "Biennium Period Start"
copied_fields['startDate'].widget.show_hm = False
copied_fields['endDate'] = ATEventSchema['endDate'].copy()
copied_fields['endDate'].widget.label = "Biennium Period End"
copied_fields['endDate'].widget.description = "Select Dec 31st as the end date"
copied_fields['endDate'].widget.show_hm = False
schema = Schema((

    copied_fields['title'],

    copied_fields['description'],

    copied_fields['startDate'],

    copied_fields['endDate'],


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

RPSCPCode_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class RPSCPCode(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IRPSCPCode)

    meta_type = 'RPSCPCode'
    _at_rename_after_creation = True

    schema = RPSCPCode_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(RPSCPCode, PROJECTNAME)
# end of class RPSCPCode

##code-section module-footer #fill in your manual code here
##/code-section module-footer



