# -*- coding: utf-8 -*-
#
# File: RPSPriority.py
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

from Products.DWCPReports.RPSBase import RPSBase

##/code-section module-header

copied_fields = {}
copied_fields['description'] = OrderedBaseFolderSchema['description'].copy()
copied_fields['description'].schemata = "default"
copied_fields['description'].widget.description = "Example: Stopping Exploitation at Work"
copied_fields['title'] = OrderedBaseFolderSchema['title'].copy()
copied_fields['title'].widget.description = "Example: Priority 1"
copied_fields['rps_priority_code'] = RPSBase.schema['rps_priority_code'].copy()
schema = Schema((

    copied_fields['description'],

    copied_fields['title'],

    copied_fields['rps_priority_code'],


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

RPSPriority_schema = OrderedBaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class RPSPriority(OrderedBaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IRPSPriority)

    meta_type = 'RPSPriority'
    _at_rename_after_creation = True

    schema = RPSPriority_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(RPSPriority, PROJECTNAME)
# end of class RPSPriority

##code-section module-footer #fill in your manual code here
##/code-section module-footer



