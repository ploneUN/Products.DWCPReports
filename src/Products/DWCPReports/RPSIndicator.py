# -*- coding: utf-8 -*-
#
# File: RPSIndicator.py
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
copied_fields['title'] = BaseFolderSchema['title'].copy()
copied_fields['description'] = BaseFolderSchema['description'].copy()
copied_fields['startDate'] = ATEventSchema['startDate'].copy()
copied_fields['startDate'].required = 1
copied_fields['startDate'].widget.show_hm = False
copied_fields['startDate'].widget.label = "Indicator Starting Period"
copied_fields['endDate'] = ATEventSchema['endDate'].copy()
copied_fields['endDate'].required = 1
copied_fields['endDate'].widget.show_hm = False
copied_fields['endDate'].widget.label = "Indicator Target Date"
schema = Schema((

    copied_fields['title'],

    copied_fields['description'],

    TextField(
        name='baseline',
        widget=TextAreaWidget(
            label="Indicator Baseline",
            label_msgid='DWCPReports_label_baseline',
            i18n_domain='DWCPReports',
        ),
        required=1,
    ),
    copied_fields['startDate'],

    TextField(
        name='target',
        widget=TextAreaWidget(
            label="Indicator Target",
            label_msgid='DWCPReports_label_target',
            i18n_domain='DWCPReports',
        ),
        required=1,
    ),
    copied_fields['endDate'],

    FileField(
        name='file1',
        widget=FileField._properties['widget'](
            label="Upload related document here",
            label_msgid='DWCPReports_label_file1',
            i18n_domain='DWCPReports',
        ),
        storage=AttributeStorage(),
        searchable=True,
    ),
    TextField(
        name='source',
        widget=TextAreaWidget(
            label="Means of Verification",
            description="Please cite reports or documents for this indicator",
            label_msgid='DWCPReports_label_source',
            description_msgid='DWCPReports_help_source',
            i18n_domain='DWCPReports',
        ),
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

RPSIndicator_schema = BaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class RPSIndicator(BaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IRPSIndicator)

    meta_type = 'RPSIndicator'
    _at_rename_after_creation = True

    schema = RPSIndicator_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(RPSIndicator, PROJECTNAME)
# end of class RPSIndicator

##code-section module-footer #fill in your manual code here
##/code-section module-footer



