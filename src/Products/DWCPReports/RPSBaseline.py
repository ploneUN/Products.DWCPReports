# -*- coding: utf-8 -*-
#
# File: RPSBaseline.py
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
from Products.DWCPReports.RPSMilestone import RPSMilestone

##/code-section module-header

copied_fields = {}
copied_fields['startDate'] = ATEventSchema['startDate'].copy()
copied_fields['startDate'].widget.show_hm = False
copied_fields['startDate'].widget.label = "Starting Date"
copied_fields['description'] = OrderedBaseFolderSchema['description'].copy()
copied_fields['title'] = OrderedBaseFolderSchema['title'].copy()
copied_fields['title'].widget.description = "Example: At the beginning of 2008"
schema = Schema((

    copied_fields['startDate'],

    copied_fields['description'],

    TextField(
        name='baseline',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Starting Situation",
            description="One per line.",
            label_msgid='DWCPReports_label_baseline',
            description_msgid='DWCPReports_help_baseline',
            i18n_domain='DWCPReports',
        ),
        default_output_type='text/html',
        required=1,
    ),
    copied_fields['title'],


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

RPSBaseline_schema = OrderedBaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class RPSBaseline(OrderedBaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IRPSBaseline)

    meta_type = 'RPSBaseline'
    _at_rename_after_creation = True

    schema = RPSBaseline_schema

    ##code-section class-header #fill in your manual code here

    def milestones(self):
        "Get milestones contained in this folder."

        ##FIXME probably can be rewritten as a list comprehension

        output = list()

        for item in self.listFolderContents():
            if isinstance(item, RPSMilestone):
                    output.append(item)
        return output




    ##/code-section class-header

    # Methods

    # Manually created methods

    def milestones(self):
        "Get milestones contained in this folder."

        ##FIXME probably can be rewritten as a list comprehension

        output = list()

        for item in self.listFolderContents():
            if isinstance(item, RPSMilestone):
                    output.append(item)
        return output



registerType(RPSBaseline, PROJECTNAME)
# end of class RPSBaseline

##code-section module-footer #fill in your manual code here
##/code-section module-footer



