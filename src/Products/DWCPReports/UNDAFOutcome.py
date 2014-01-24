# -*- coding: utf-8 -*-
#
# File: UNDAFOutcome.py
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
copied_fields['title'] = BaseSchema['title'].copy()
copied_fields['title'].widget.label = "UNDAF Outcome"
copied_fields['title'].widget.description = "Example: UNDAF Outcome 1 or UNDAF Sub-Outcome 1.1"
copied_fields['description'] = BaseSchema['description'].copy()
copied_fields['description'].required = 1
copied_fields['description'].schemata = "default"
copied_fields['description'].widget.description = "Brief description of UNDAF Outcome. Example: Increased opportunities for sustainable livelihoods"
schema = Schema((

    copied_fields['title'],

    copied_fields['description'],


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

UNDAFOutcome_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class UNDAFOutcome(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IUNDAFOutcome)

    meta_type = 'UNDAFOutcome'
    _at_rename_after_creation = True

    schema = UNDAFOutcome_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(UNDAFOutcome, PROJECTNAME)
# end of class UNDAFOutcome

##code-section module-footer #fill in your manual code here
##/code-section module-footer



