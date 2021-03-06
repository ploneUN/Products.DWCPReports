# -*- coding: utf-8 -*-
#
# File: PBImmediateOutcome.py
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
##/code-section module-header

copied_fields = {}
copied_fields['title'] = BaseFolderSchema['title'].copy()
copied_fields['title'].widget.label = "Immediate Outcome Code and Year"
copied_fields['title'].widget.description = "Example: 210150 08-09"
copied_fields['description'] = BaseFolderSchema['description'].copy()
copied_fields['description'].required = True
copied_fields['description'].schemata = "default"
copied_fields['description'].widget.description = "Example:  Increase member State and development partner capacity to develop and implement policies and programmes on"
schema = Schema((

    copied_fields['title'],

    copied_fields['description'],


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

PBImmediateOutcome_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class PBImmediateOutcome(BaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IPBImmediateOutcome)

    meta_type = 'PBImmediateOutcome'
    _at_rename_after_creation = True

    schema = PBImmediateOutcome_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(PBImmediateOutcome, PROJECTNAME)
# end of class PBImmediateOutcome

##code-section module-footer #fill in your manual code here
##/code-section module-footer



