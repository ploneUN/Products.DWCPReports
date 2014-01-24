# -*- coding: utf-8 -*-
#
# File: RPSBase.py
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

from Products.ATReferenceBrowserWidget.ATReferenceBrowserWidget import ReferenceBrowserWidget

##/code-section module-header

schema = Schema((

    ReferenceField(
        name='rps_cpo_code',
        widget=ReferenceBrowserWidget(
            label="Linked CPO Code(s)",
            label_msgid='DWCPReports_label_rps_cpo_code',
            i18n_domain='DWCPReports',
        ),
        multiValued=True,
        relationship="RelatedCPOCode",
        allow_browse=True,
        allowed_types=('RPSCPCode'),
        base_query={'portal_type':'RPSCPCode'},
        startup_directory="/dwcp/iris-cp-priority-codes",
    ),
    ReferenceField(
        name='national_framework',
        widget=ReferenceBrowserWidget(
            label="Link to National Development Framework Section",
            description="Links to National Development Framework Documents Section",
            label_msgid='DWCPReports_label_national_framework',
            description_msgid='DWCPReports_help_national_framework',
            i18n_domain='DWCPReports',
        ),
        allowed_types=('NDFPriority'),
        multiValued=True,
        relationship="RelatedNDFPriority",
    ),
    ReferenceField(
        name='undaf',
        widget=ReferenceBrowserWidget(
            label="Link to UNDAF Outcome",
            description="Link to UNDAF Outcome",
            label_msgid='DWCPReports_label_undaf',
            description_msgid='DWCPReports_help_undaf',
            i18n_domain='DWCPReports',
        ),
        allowed_types=('UNDAFOutcome'),
        base_query={'portal_type':'UNDAFOutcome'},
        multiValued=True,
        relationship="RelatedUNDAF",
    ),
    ReferenceField(
        name='partner',
        widget=ReferenceBrowserWidget(
            label="Partner(s)",
            description="Partners for this CPO",
            label_msgid='DWCPReports_label_partner',
            description_msgid='DWCPReports_help_partner',
            i18n_domain='DWCPReports',
        ),
        allowed_types=('Partner'),
        base_query={'portal_type':'Partner'},
        multiValued=1,
        relationship="RelatedPartner",
    ),
    ReferenceField(
        name='rps_priority_code',
        widget=ReferenceBrowserWidget(
            label="Related IRIS CPO Priority Code(s)",
            label_msgid='DWCPReports_label_rps_priority_code',
            i18n_domain='DWCPReports',
        ),
        multiValued=True,
        relationship="RelatedPriorityCode",
        allowed_types=('RPSCPPriorityCode'),
        base_query={'portal_type':'RPSCPPriorityCode'},
        startup_directory="/dwcp/iris-cp-priority-codes",
    ),
    ReferenceField(
        name='pb_outcome',
        widget=ReferenceBrowserWidget(
            label="Link to P&B Outcome",
            label_msgid='DWCPReports_label_pb_outcome',
            i18n_domain='DWCPReports',
        ),
        allowed_types=('PBOutcome'),
        base_query={'portal_type':'PBOutcome'},
        multiValued=True,
        relationship="RelatedPBOutcome",
    ),
    ReferenceField(
        name='pb_indicator',
        widget=ReferenceBrowserWidget(
            label="Link to ILO Outcome Indicator Code",
            label_msgid='DWCPReports_label_pb_indicator',
            i18n_domain='DWCPReports',
        ),
        allowed_types=('PBIndicator'),
        base_query={'portal_type':'PBIndicator'},
        multiValued=True,
        relationship="RelatedPBIndicator",
    ),

),
)

##code-section after-local-schema #fill in your manual code here
##/code-section after-local-schema

RPSBase_schema = schema.copy()

##code-section after-schema #fill in your manual code here
##/code-section after-schema

class RPSBase(BaseContent, BrowserDefaultMixin):
    """
    """
    security = ClassSecurityInfo()

    implements(interfaces.IRPSBase)

    _at_rename_after_creation = True

    schema = RPSBase_schema

    ##code-section class-header #fill in your manual code here
    ##/code-section class-header

    # Methods

# end of class RPSBase

##code-section module-footer #fill in your manual code here
##/code-section module-footer



