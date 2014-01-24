# -*- coding: utf-8 -*-
#
# File: NDFDocument.py
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
copied_fields['title'].widget.description = "Example: National Medium Term Development Plan (RPJM) 2005-2009"
copied_fields['description'] = OrderedBaseFolderSchema['description'].copy()
copied_fields['description'].schemata = "default"
copied_fields['remoteUrl'] = ATLinkSchema['remoteUrl'].copy()
copied_fields['remoteUrl'].required = False
schema = Schema((

    copied_fields['title'],

    copied_fields['description'],

    copied_fields['remoteUrl'],

    FileField(
        name='file1',
        widget=FileField._properties['widget'](
            label="Document Attachment 1",
            label_msgid='DWCPReports_label_file1',
            i18n_domain='DWCPReports',
        ),
        storage=AttributeStorage(),
        searchable=1,
    ),
    FileField(
        name='file2',
        widget=FileField._properties['widget'](
            label="Document Atttachment 2",
            label_msgid='DWCPReports_label_file2',
            i18n_domain='DWCPReports',
        ),
        storage=AttributeStorage(),
        searchable=1,
    ),
    FileField(
        name='file3',
        widget=FileField._properties['widget'](
            label="Document Attachment 3",
            label_msgid='DWCPReports_label_file3',
            i18n_domain='DWCPReports',
        ),
        storage=AttributeStorage(),
        searchable=1,
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

NDFDocument_schema = OrderedBaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class NDFDocument(OrderedBaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.INDFDocument)

    meta_type = 'NDFDocument'
    _at_rename_after_creation = True

    schema = NDFDocument_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(NDFDocument, PROJECTNAME)
# end of class NDFDocument

##code-section module-footer #fill in your manual code here
##/code-section module-footer



