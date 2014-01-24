# -*- coding: utf-8 -*-
#
# File: DWCPReports.py
#
# Copyright (c) 2009 by []
# Generator: ArchGenXML Version 2.4.1
#            http://plone.org/products/archgenxml
#
# GNU General Public License (GPL)
#

__author__ = """unknown <unknown>"""
__docformat__ = 'plaintext'


# Product configuration.
#
# The contents of this module will be imported into __init__.py, the
# workflow configuration and every content type module.
#
# If you wish to perform custom configuration, you may put a file
# AppConfig.py in your product's root directory. The items in there
# will be included (by importing) in this file if found.

from Products.CMFCore.permissions import setDefaultRoles
##code-section config-head #fill in your manual code here
##/code-section config-head


PROJECTNAME = "DWCPReports"

# Permissions
DEFAULT_ADD_CONTENT_PERMISSION = "Add portal content"
setDefaultRoles(DEFAULT_ADD_CONTENT_PERMISSION, ('Manager', 'Owner', 'Contributor'))
ADD_CONTENT_PERMISSIONS = {
    'RPSMonitoringPlan': 'DWCPReports: Add RPSMonitoringPlan',
    'RPSPriority': 'DWCPReports: Add RPSPriority',
    'RPSCPO': 'DWCPReports: Add RPSCPO',
    'RPSBaseline': 'DWCPReports: Add RPSBaseline',
    'RPSMilestone': 'DWCPReports: Add RPSMilestone',
    'RPSCPCode': 'DWCPReports: Add RPSCPCode',
    'Partner': 'DWCPReports: Add Partner',
    'NDFDocument': 'DWCPReports: Add NDFDocument',
    'UNDAFDocument': 'DWCPReports: Add UNDAFDocument',
    'RPSCPPriorityCode': 'DWCPReports: Add RPSCPPriorityCode',
    'RPSIndicator': 'DWCPReports: Add RPSIndicator',
    'RPSIndicatorInterval': 'DWCPReports: Add RPSIndicatorInterval',
    'UNDAFOutcome': 'DWCPReports: Add UNDAFOutcome',
    'NDFPriority': 'DWCPReports: Add NDFPriority',
    'PBOutcome': 'DWCPReports: Add PBOutcome',
    'PBIndicator': 'DWCPReports: Add PBIndicator',
    'DWCPCountryFolder': 'DWCPReports: Add DWCPCountryFolder',
    'NDFFolder': 'DWCPReports: Add NDFFolder',
    'UNDAFFolder': 'DWCPReports: Add UNDAFFolder',
    'PartnersFolder': 'DWCPReports: Add PartnersFolder',
}

setDefaultRoles('DWCPReports: Add RPSMonitoringPlan', ('Manager','Owner'))
setDefaultRoles('DWCPReports: Add RPSPriority', ('Manager','Owner'))
setDefaultRoles('DWCPReports: Add RPSCPO', ('Manager','Owner'))
setDefaultRoles('DWCPReports: Add RPSBaseline', ('Manager','Owner'))
setDefaultRoles('DWCPReports: Add RPSMilestone', ('Manager','Owner'))
setDefaultRoles('DWCPReports: Add RPSCPCode', ('Manager','Owner'))
setDefaultRoles('DWCPReports: Add Partner', ('Manager','Owner'))
setDefaultRoles('DWCPReports: Add NDFDocument', ('Manager','Owner'))
setDefaultRoles('DWCPReports: Add UNDAFDocument', ('Manager','Owner'))
setDefaultRoles('DWCPReports: Add RPSCPPriorityCode', ('Manager','Owner'))
setDefaultRoles('DWCPReports: Add RPSIndicator', ('Manager','Owner'))
setDefaultRoles('DWCPReports: Add RPSIndicatorInterval', ('Manager','Owner'))
setDefaultRoles('DWCPReports: Add UNDAFOutcome', ('Manager','Owner'))
setDefaultRoles('DWCPReports: Add NDFPriority', ('Manager','Owner'))
setDefaultRoles('DWCPReports: Add PBOutcome', ('Manager','Owner'))
setDefaultRoles('DWCPReports: Add PBIndicator', ('Manager','Owner'))
setDefaultRoles('DWCPReports: Add DWCPCountryFolder', ('Manager','Owner'))
setDefaultRoles('DWCPReports: Add NDFFolder', ('Manager','Owner'))
setDefaultRoles('DWCPReports: Add UNDAFFolder', ('Manager','Owner'))
setDefaultRoles('DWCPReports: Add PartnersFolder', ('Manager','Owner'))

product_globals = globals()

# Dependencies of Products to be installed by quick-installer
# override in custom configuration
DEPENDENCIES = []

# Dependend products - not quick-installed - used in testcase
# override in custom configuration
PRODUCT_DEPENDENCIES = []

##code-section config-bottom #fill in your manual code here
##/code-section config-bottom


# Load custom configuration not managed by archgenxml
try:
    from Products.DWCPReports.AppConfig import *
except ImportError:
    pass
