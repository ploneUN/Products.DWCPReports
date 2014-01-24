# -*- coding: utf-8 -*-
#
# File: RPSCPO.py
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
from Products.DWCPReports.RPSBase import RPSBase
from Products.DWCPReports.RPSBaseline import RPSBaseline
from Products.DWCPReports.RPSIndicator import RPSIndicator

##/code-section module-header

copied_fields = {}
copied_fields['title'] = OrderedBaseFolderSchema['title'].copy()
copied_fields['title'].widget.label = "Country Programme Outcome"
copied_fields['title'].widget.description = "Example: CPO 1.1"
copied_fields['description'] = OrderedBaseFolderSchema['description'].copy()
copied_fields['description'].schemata = "default"
copied_fields['description'].widget.description = "Brief one line description of Country Practice Outcome"
copied_fields['country'] = ILOIntranetBase.schema['country'].copy()
copied_fields['theme'] = ILOIntranetBase.schema['theme'].copy()
copied_fields['rps_cpo_code'] = RPSBase.schema['rps_cpo_code'].copy()
copied_fields['pb_indicator'] = RPSBase.schema['pb_indicator'].copy()
copied_fields['partner'] = RPSBase.schema['partner'].copy()
copied_fields['undaf'] = RPSBase.schema['undaf'].copy()
copied_fields['national_framework'] = RPSBase.schema['national_framework'].copy()
schema = Schema((

    copied_fields['title'],

    copied_fields['description'],

    copied_fields['country'],

    StringField(
        name='cpo_status',
        widget=SelectionWidget(
            label="CPO Status",
            label_msgid='DWCPReports_label_cpo_status',
            i18n_domain='DWCPReports',
        ),
        vocabulary=['No Progress','On Track','Results Achieved'],
    ),
    copied_fields['theme'],

    LinesField(
        name='main_assumptions',
        widget=LinesField._properties['widget'](
            label="Main Assumptions",
            description="One assumption per line. Assumptions should be expressed in precise and positive terms, as the situations that have to happen for the internal logic of the country programme to come true. Not all the situations that may affect the country programme's implementation should be described as assumptions.",
            label_msgid='DWCPReports_label_main_assumptions',
            description_msgid='DWCPReports_help_main_assumptions',
            i18n_domain='DWCPReports',
        ),
    ),
    StringField(
        name='officer',
        widget=StringField._properties['widget'](
            label="Responsible Official",
            description="Name of Responsible Official",
            label_msgid='DWCPReports_label_officer',
            description_msgid='DWCPReports_help_officer',
            i18n_domain='DWCPReports',
        ),
    ),
    copied_fields['rps_cpo_code'],

    copied_fields['pb_indicator'],

    copied_fields['partner'],

    copied_fields['undaf'],

    copied_fields['national_framework'],


),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

RPSCPO_schema = OrderedBaseFolderSchema.copy() + \
    schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class RPSCPO(OrderedBaseFolder, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IRPSCPO)

    meta_type = 'RPSCPO'
    _at_rename_after_creation = True

    schema = RPSCPO_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

    # Manually created methods

    def baselines(self):
        "Get baselines contained in this folder."

        ##FIXME probably can be rewritten as a list comprehension

        output = list()

        for item in self.listFolderContents():
            if isinstance(item, RPSBaseline):
                    output.append(item)

        return output

    def indicators(self):
        "Get indicators contained in this folder."

        ##FIXME probably can be rewritten as a list comprehension

        output = list()

        for item in self.listFolderContents():
            if isinstance(item, RPSIndicator):
                    output.append(item)

        return output

    def ndfpriority(self):
        "Get NDFPriority contained in this folder."

        ##FIXME probably can be rewritten as a list comprehension

        output = list()

        for item in self.getRefs(relationship='NDFPriority'):
            output.append(item)

        return output



registerType(RPSCPO, PROJECTNAME)
# end of class RPSCPO

##code-section module-footer #fill in your manual code here
##/code-section module-footer



