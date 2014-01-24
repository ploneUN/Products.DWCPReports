# -*- coding: utf-8 -*-
#
# File: UNDAFDocument.py
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
from Products.ATContentTypes.content.link import ATLink
from Products.ATContentTypes.content.link import ATLinkSchema

##/code-section module-header

copied_fields = {}
copied_fields['title'] = OrderedBaseFolderSchema['title'].copy()
copied_fields['title'].widget.label = "UNDAF Document"
copied_fields['title'].widget.description = "Example: UNDAF Indonesia 2006-2010"
copied_fields['description'] = OrderedBaseFolderSchema['description'].copy()
copied_fields['description'].schemata = "default"
copied_fields['description'].widget.description = "Brief description of UNDAF Document"
copied_fields['startDate'] = ATEventSchema['startDate'].copy()
copied_fields['startDate'].required = False
copied_fields['startDate'].widget.show_hm = False
copied_fields['startDate'].widget.label = "Document Start Date"
copied_fields['startDate'].widget.description = "Select Jan 1st as the starting date"
copied_fields['startDate'].widget.future_years = 20
copied_fields['endDate'] = ATEventSchema['endDate'].copy()
copied_fields['endDate'].required = False
copied_fields['endDate'].widget.show_hm = False
copied_fields['endDate'].widget.label = "Document End Date"
copied_fields['endDate'].widget.description = "Select Dec 31st as ending date"
copied_fields['endDate'].widget.future_years = 20
copied_fields['remoteUrl'] = ATLinkSchema['remoteUrl'].copy()
copied_fields['remoteUrl'].required = False
copied_fields['remoteUrl'].widget.description = "URL to original document if any"
schema = Schema((

    copied_fields['title'],

    copied_fields['description'],

    copied_fields['startDate'],

    copied_fields['endDate'],

    copied_fields['remoteUrl'],

    FileField(
        name='file1',
        widget=FileField._properties['widget'](
            label='File1',
            label_msgid='DWCPReports_label_file1',
            i18n_domain='DWCPReports',
        ),
        storage=AttributeStorage(),
        searchable=True,
    ),
    FileField(
        name='file2',
        widget=FileField._properties['widget'](
            label='File2',
            label_msgid='DWCPReports_label_file2',
            i18n_domain='DWCPReports',
        ),
        storage=AttributeStorage(),
        searchable=True,
    ),
    FileField(
        name='file3',
        widget=FileField._properties['widget'](
            label='File3',
            label_msgid='DWCPReports_label_file3',
            i18n_domain='DWCPReports',
        ),
        storage=AttributeStorage(),
        searchable=True,
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

UNDAFDocument_schema = OrderedBaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class UNDAFDocument(OrderedBaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IUNDAFDocument)

    meta_type = 'UNDAFDocument'
    _at_rename_after_creation = True

    schema = UNDAFDocument_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(UNDAFDocument, PROJECTNAME)
# end of class UNDAFDocument

##code-section module-footer #fill in your manual code here
##/code-section module-footer



