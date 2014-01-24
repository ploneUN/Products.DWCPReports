# -*- coding: utf-8 -*-
#
# File: RPSCPPriorityCode.py
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
copied_fields['description'] = OrderedBaseFolderSchema['description'].copy()
copied_fields['description'].schemata = "default"
copied_fields['startDate'] = ATEventSchema['startDate'].copy()
copied_fields['endDate'] = ATEventSchema['endDate'].copy()
schema = Schema((

    copied_fields['title'],

    copied_fields['description'],

    copied_fields['startDate'],

    copied_fields['endDate'],


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

RPSCPPriorityCode_schema = OrderedBaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class RPSCPPriorityCode(OrderedBaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IRPSCPPriorityCode)

    meta_type = 'RPSCPPriorityCode'
    _at_rename_after_creation = True

    schema = RPSCPPriorityCode_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(RPSCPPriorityCode, PROJECTNAME)
# end of class RPSCPPriorityCode

##code-section module-footer #fill in your manual code here
##/code-section module-footer



