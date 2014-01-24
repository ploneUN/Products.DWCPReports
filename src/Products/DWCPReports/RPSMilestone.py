# -*- coding: utf-8 -*-
#
# File: RPSMilestone.py
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
copied_fields['endDate'] = ATEventSchema['endDate'].copy()
copied_fields['endDate'].widget.label = "Milestone End Date"
copied_fields['endDate'].widget.show_hm = False
copied_fields['title'] = BaseSchema['title'].copy()
copied_fields['title'].widget.description = "Example: End of 2008"
copied_fields['description'] = BaseSchema['description'].copy()
copied_fields['description'].schemata = "default"
copied_fields['description'].widget.description = "Brief description or background note. Example: The Malaysian government has taken concrete steps to develop and implement new policies on income security, with the participation of the social partners"
schema = Schema((

    TextField(
        name='milestones',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Milestones",
            description="Brief description of milestones (1 per line). For long lines that wrap around, press enter to separate between milestones.",
            label_msgid='DWCPReports_label_milestones',
            description_msgid='DWCPReports_help_milestones',
            i18n_domain='DWCPReports',
        ),
        default_output_type='text/html',
        required=1,
    ),
    StringField(
        name='milestone_status',
        widget=SelectionWidget(
            label="Status",
            label_msgid='DWCPReports_label_milestone_status',
            i18n_domain='DWCPReports',
        ),
        vocabulary=['No Progress','On Track','Results Achieved'],
    ),
    copied_fields['endDate'],

    TextField(
        name='progress_1',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Progress Report",
            description="Limit to 500 words or less.",
            label_msgid='DWCPReports_label_progress_1',
            description_msgid='DWCPReports_help_progress_1',
            i18n_domain='DWCPReports',
        ),
        default_output_type='text/html',
    ),
    TextField(
        name='problems',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="New development or problems",
            description="New development or problems/ issues affecting the achievement of the outcome",
            label_msgid='DWCPReports_label_problems',
            description_msgid='DWCPReports_help_problems',
            i18n_domain='DWCPReports',
        ),
        default_output_type='text/html',
    ),
    TextField(
        name='modifications',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Modifications",
            description="Please provide a brief description of main strategy or any modifications to be made if need be in the next year",
            label_msgid='DWCPReports_label_modifications',
            description_msgid='DWCPReports_help_modifications',
            i18n_domain='DWCPReports',
        ),
        default_output_type='text/html',
    ),
    TextField(
        name='gender_concerns',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label="Gender Concerns",
            description="Describe how gender concerns have been mainstreamed",
            label_msgid='DWCPReports_label_gender_concerns',
            description_msgid='DWCPReports_help_gender_concerns',
            i18n_domain='DWCPReports',
        ),
        default_output_type='text/html',
    ),
    FileField(
        name='file1',
        widget=FileField._properties['widget'](
            label="Document Attachment 1",
            label_msgid='DWCPReports_label_file1',
            i18n_domain='DWCPReports',
        ),
        storage=AttributeStorage(),
        searchable=True,
    ),
    FileField(
        name='file2',
        widget=FileField._properties['widget'](
            label="Document Attachment 2",
            label_msgid='DWCPReports_label_file2',
            i18n_domain='DWCPReports',
        ),
        storage=AttributeStorage(),
        searchable=True,
    ),
    FileField(
        name='file3',
        widget=FileField._properties['widget'](
            label="Document Attachment 3",
            label_msgid='DWCPReports_label_file3',
            i18n_domain='DWCPReports',
        ),
        storage=AttributeStorage(),
        searchable=True,
    ),
    copied_fields['title'],

    copied_fields['description'],


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

RPSMilestone_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class RPSMilestone(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IRPSMilestone)

    meta_type = 'RPSMilestone'
    _at_rename_after_creation = True

    schema = RPSMilestone_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods


registerType(RPSMilestone, PROJECTNAME)
# end of class RPSMilestone

##code-section module-footer #fill in your manual code here
##/code-section module-footer



