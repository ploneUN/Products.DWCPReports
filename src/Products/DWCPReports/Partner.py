# -*- coding: utf-8 -*-
#
# File: Partner.py
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
from Products.ILOIntranetTypes.ILOIntranetBase import ILOIntranetBase
from Products.ILOIntranetTypes.MissionReport import MissionReport
from Products.DWCPReports.RPSBase import RPSBase
from Products.DWCPReports.RPSCPO import RPSCPO
##/code-section module-header

copied_fields = {}
copied_fields['title'] = BaseSchema['title'].copy()
copied_fields['title'].label = "ILO Partner"
copied_fields['title'].widget.description = "Example: Ministry of Human Resources, Malaysia or UNDP Country Office, Malaysia"
copied_fields['description'] = BaseSchema['description'].copy()
copied_fields['description'].schemata = "default"
copied_fields['description'].widget.label = "Brief description of Partner"
copied_fields['theme'] = ILOIntranetBase.schema['theme'].copy()
schema = Schema((

    copied_fields['title'],

    copied_fields['description'],

    StringField(
        name='organization_type',
        widget=SelectionWidget(
            label="Organization Type",
            label_msgid='DWCPReports_label_organization_type',
            i18n_domain='DWCPReports',
        ),
        vocabulary=['Donor Agency','Employer Organization','Government Agency','None-governmental Organization','Research and Academic Institution','Trade Union','UN Partner'],
    ),
    copied_fields['theme'],

    TextField(
        name='notes',
        allowable_content_types=('text/plain', 'text/structured', 'text/html', 'application/msword',),
        widget=RichWidget(
            label='Notes',
            label_msgid='DWCPReports_label_notes',
            i18n_domain='DWCPReports',
        ),
        default_output_type='text/html',
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

Partner_schema = BaseSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class Partner(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IPartner)

    meta_type = 'Partner'
    _at_rename_after_creation = True

    schema = Partner_schema

    ##code-section class-header #fill in your manual code here

    def cpos(self):
        "Get related CPO"

        output =  list()


        for item in self.getBRefs():
            if isinstance(item, RPSCPO):
                    output.append(item)

        return output

    def mission_reports(self):
        "Get related Mission Reports"

        output =  list()

        for item in self.getBRefs():
            if isinstance(item, MissionReport):
                    output.append(item)

        return output

    ##/code-section class-header

    # Methods

    # Manually created methods

    def cpos(self):
        "Get related CPO"

        output =  list()


        for item in self.getBRefs():
            if isinstance(item, RPSCPO):
                    output.append(item)

        return output

    def mission_reports(self):
        "Get related Mission Reports"

        output =  list()

        for item in self.getBRefs():
            if isinstance(item, MissionReport):
                    output.append(item)

        return output



registerType(Partner, PROJECTNAME)
# end of class Partner

##code-section module-footer #fill in your manual code here
##/code-section module-footer



