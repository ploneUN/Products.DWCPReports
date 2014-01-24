# -*- coding: utf-8 -*-
#
# File: RPSIndicatorInterval.py
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
copied_fields['title'].widget.description = "Period indicator, such as 2009 or 2009-2010"
copied_fields['endDate'] = ATEventSchema['endDate'].copy()
copied_fields['endDate'].required = 1
copied_fields['endDate'].widget.label = "Date of Indicator Interval Target"
copied_fields['endDate'].widget.show_hm = False
schema = Schema((

    copied_fields['title'],

    copied_fields['endDate'],

    TextField(
        name='planned',
        widget=TextAreaWidget(
            label="Planned",
            label_msgid='DWCPReports_label_planned',
            i18n_domain='DWCPReports',
        ),
        required=1,
    ),
    TextField(
        name='actual',
        widget=TextAreaWidget(
            label='Actual',
            label_msgid='DWCPReports_label_actual',
            i18n_domain='DWCPReports',
        ),
    ),
    FileField(
        name='file1',
        widget=FileField._properties['widget'](
            label="Upload Document Attachment here",
            label_msgid='DWCPReports_label_file1',
            i18n_domain='DWCPReports',
        ),
        storage=AttributeStorage(),
        searchable=True,
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

RPSIndicatorInterval_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class RPSIndicatorInterval(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IRPSIndicatorInterval)

    meta_type = 'RPSIndicatorInterval'
    _at_rename_after_creation = True

    schema = RPSIndicatorInterval_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(RPSIndicatorInterval, PROJECTNAME)
# end of class RPSIndicatorInterval

##code-section module-footer #fill in your manual code here
##/code-section module-footer



