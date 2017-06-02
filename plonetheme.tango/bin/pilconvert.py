#!/usr/bin/python
#
# The Python Imaging Library.
# $Id$
#
# convert image files
#
# History:
# 0.1   96-04-20 fl     Created
# 0.2   96-10-04 fl     Use draft mode when converting images
# 0.3   96-12-30 fl     Optimize output (PNG, JPEG)
# 0.4   97-01-18 fl     Made optimize an option (PNG, JPEG)
# 0.5   98-12-30 fl     Fixed -f option (from Anthony Baxter)
#

from __future__ import print_function



import sys
sys.path[0:0] = [
  '/home/vagrant/buildout-cache/eggs/Plone-5.0.6-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Pillow-3.3.0-py2.7-linux-i686.egg',
  '/home/vagrant/training/buildout/plonetheme.tango/src',
  '/home/vagrant/buildout-cache/eggs/plone.app.robotframework-1.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/robotframework_ride-1.5.2.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/watchdog-0.8.3-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/robotframework_debuglibrary-0.5-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.testrunner-4.4.4-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.schema-4.4.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.i18n-3.7.4-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.configuration-3.7.4-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.component-3.9.5-py2.7.egg',
  '/usr/local/lib/python2.7/dist-packages',
  '/home/vagrant/buildout-cache/eggs/selenium-2.53.6-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/robotsuite-1.7.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/robotframework_selenium2library-1.7.4-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/robotframework-3.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.uuid-1.0.4-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.testing-5.0.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.testing-5.0.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/five.globalrequest-1.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Babel-1.3-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.PluggableAuthService-1.11.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.PlonePAS-5.0.11-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.MailHost-2.13.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.CMFPlone-5.0.6-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.CMFCore-2.2.10-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.contenttypes-1.2.17-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.themingplugins-1.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.theming-1.3.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/z3c.jbot-0.7.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.GenericSetup-1.8.3-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.api-1.5-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.upgrade-1.3.27-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.openid-2.1.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.iterate-3.2.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.dexterity-2.3.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.caching-1.2.11-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.CMFPlacefulWorkflow-1.6.5-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.ATContentTypes-2.2.13-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.Archetypes-1.10.15-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/pathtools-0.1.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/argh-0.26.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/PyYAML-3.12-py2.7-linux-i686.egg',
  '/home/vagrant/buildout-cache/eggs/zope.interface-3.6.7-py2.7-linux-i686.egg',
  '/home/vagrant/buildout-cache/eggs/zope.exceptions-3.6.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/six-1.10.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.event-3.5.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.i18nmessageid-3.5.3-py2.7-linux-i686.egg',
  '/home/vagrant/buildout-cache/eggs/pytz-2015.7-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/unittest2-0.5.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/lxml-3.5.0-py2.7-linux-i686.egg',
  '/home/vagrant/buildout-cache/eggs/docutils-0.12-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/decorator-4.0.10-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.publisher-3.12.6-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.lifecycleevent-3.6.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.browserpage-3.12.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.testing-3.9.7-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Zope2-2.13.24-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.memoize-1.2.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/five.localsitemanager-2.0.5-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.dottedname-3.4.6-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.globalrequest-1.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.PluginRegistry-1.4-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.deprecation-3.4.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.session-3.6.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.protect-3.0.19-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.i18n-3.0.5-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.sendmail-3.7.5-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.deferredimport-3.5.3-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Persistence-2.13.2-py2.7-linux-i686.egg',
  '/home/vagrant/buildout-cache/eggs/DocumentTemplate-2.13.2-py2.7-linux-i686.egg',
  '/home/vagrant/buildout-cache/eggs/DateTime-4.0.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Acquisition-4.2.2-py2.7-linux-i686.egg',
  '/home/vagrant/buildout-cache/eggs/AccessControl-3.0.12-py2.7-linux-i686.egg',
  '/home/vagrant/buildout-cache/eggs/zope.traversing-3.13.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.tales-3.5.3-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.tal-3.5.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.structuredtext-3.5.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.site-3.9.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.pagetemplate-3.6.3-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.location-3.9.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.container-3.11.2-py2.7-linux-i686.egg',
  '/home/vagrant/buildout-cache/eggs/zope.cachedescriptors-3.5.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.app.locales-3.6.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/z3c.autoinclude-0.3.6-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/transaction-1.1.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/slimit-0.8.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plonetheme.barceloneta-1.6.21-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.theme-3.0.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.schema-1.0.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.registry-1.0.4-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.portlets-2.2.3-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.portlet.static-3.0.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.portlet.collection-3.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.outputfilters-2.1.5-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.locking-2.1.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.intelligenttext-2.1.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.indexer-1.0.4-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.contentrules-2.0.6-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.browserlayer-2.1.6-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.batching-1.1.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.workflow-2.2.6-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.vocabularies-3.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.viewletmanager-2.0.10-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.uuid-1.1.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.users-2.3.7-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.registry-1.3.12-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.redirector-1.3.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.portlets-3.1.3-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.locales-5.0.11-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.linkintegrity-3.0.6-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.layout-2.5.20-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.multilingual-4.0.3-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.i18n-3.0.3-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.folder-1.2.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.discussion-2.4.17-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.customerize-1.3.5-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.controlpanel-3.0.4-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.contentrules-4.0.11-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.contentmenu-2.1.8-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.contentlisting-1.2.7-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.content-3.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/mockup-2.1.5-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/five.pt-2.2.4-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/five.customerize-1.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/cssmin-0.2.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/borg.localrole-3.1.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/ZODB3-3.10.5-py2.7-linux-i686.egg',
  '/home/vagrant/buildout-cache/eggs/Products.statusmessages-4.1.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.contentmigration-2.1.13-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.ResourceRegistries-3.0.4-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.PortalTransforms-2.2.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.PlacelessTranslationService-2.0.6-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.PasswordResetTool-2.2.3-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.MimetypesRegistry-2.0.10-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.ExternalEditor-1.1.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.ExtendedPathIndex-3.1.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.DCWorkflow-2.2.5-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.CMFUid-2.2.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.CMFQuickInstallerTool-3.0.13-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.CMFEditions-2.2.21-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.CMFDynamicViewFTI-4.1.4-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.CMFDiffTool-3.1.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/ExtensionClass-4.1.2-py2.7-linux-i686.egg',
  '/home/vagrant/buildout-cache/eggs/zope.app.publication-3.12.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.ZSQLMethods-2.13.4-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.z3cform-1.2.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.lockingbehavior-1.0.4-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.versioningbehavior-1.2.9-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.namedfile-3.0.9-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.relationfield-1.3.3-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.dexterity-2.4.3-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.querystring-1.3.15-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.event-2.0.10-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.resource-1.0.6-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/roman-1.4.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/repoze.xmliter-0.6-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.transformchain-1.2.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.subrequest-1.7.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.resourceeditor-2.0.5-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/diazo-1.2.3-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.security-3.7.4-py2.7-linux-i686.egg',
  '/home/vagrant/buildout-cache/eggs/zope.formlib-4.0.6-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.ZCatalog-3.0.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.SecureMailHost-1.1.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.CMFFormController-3.0.6-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.ramcache-1.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.openid-2.0.4-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.viewlet-3.7.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.annotation-3.5.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/z3c.form-3.2.9-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.z3cform-0.8.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.supermodel-1.3.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.autoform-1.6.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.schemaeditor-2.0.11-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.rfc822-1.1.3-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.formwidget.namedfile-1.0.15-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.behavior-1.1.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.textfield-1.2.7-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/z3c.zcmlhook-1.0b1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.browserresource-3.10.3-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.cachepurging-1.0.12-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.caching-1.1.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/python_dateutil-2.4.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/ZConfig-2.9.3-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.validation-2.0.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.widgets-2.0.6-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.collection-1.1.6-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.blob-1.6.4-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.folder-1.0.9-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.datetime-3.4.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.contenttype-3.5.5-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.proxy-3.6.1-py2.7-linux-i686.egg',
  '/home/vagrant/buildout-cache/eggs/zope.browser-1.3-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.StandardCacheManagers-2.13.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.PythonScripts-2.13.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.MIMETools-2.13.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.ExternalMethod-2.13.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.BTreeFolder2-2.14.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.testbrowser-3.11.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.size-3.4.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.sequencesort-3.4.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.ptresource-3.9.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.processlifetime-1.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.contentprovider-3.7.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.browsermenu-3.9.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zLOG-2.11.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zExceptions-2.13.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zdaemon-2.0.7-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/tempstorage-2.12.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/initgroups-2.13.0-py2.7-linux-i686.egg',
  '/home/vagrant/buildout-cache/eggs/ZopeUndo-2.12.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/RestrictedPython-3.6.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Record-2.13.0-py2.7-linux-i686.egg',
  '/home/vagrant/buildout-cache/eggs/Products.ZCTextIndex-2.13.5-py2.7-linux-i686.egg',
  '/home/vagrant/buildout-cache/eggs/Products.OFSP-2.13.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/MultiMapping-2.13.0-py2.7-linux-i686.egg',
  '/home/vagrant/buildout-cache/eggs/Missing-2.13.1-py2.7-linux-i686.egg',
  '/home/vagrant/buildout-cache/eggs/plone.keyring-3.0.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/collective.monkeypatcher-1.1.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Unidecode-0.4.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.broken-3.6.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.filerepresentation-3.6.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/ply-3.4-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.componentvocabulary-1.0.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.imaging-2.0.5-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/feedparser-5.2.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.app.intid-1.1.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/z3c.relationfield-0.7-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/archetypes.multilingual-3.0.3-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.stringinterp-1.1.4-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Chameleon-2.24-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/z3c.pt-3.0.0a1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/sourcecodegen-0.6.14-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zc.lockfile-1.0.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Markdown-2.6.6-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/python_gettext-3.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.ZopeVersionControl-1.1.3-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.copy-3.5.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.error-3.7.4-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.authentication-3.7.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/z3c.formwidget.query-0.12-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.app.file-3.6.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/five.intid-1.1.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.intid-3.7.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.synchronize-1.0.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.alterego-1.0.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.formwidget.recurrence-2.1.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.event-1.3.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/icalendar-3.10-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/collective.elephantvocabulary-0.2.5-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/Products.DateRecurringIndex-2.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/z3c.caching-2.0a1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/future-0.15.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/cssselect-0.9.2-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/python_openid-2.2.5-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/plone.scale-1.4.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/archetypes.schemaextender-2.1.6-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/mechanize-0.2.5-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zc.relation-1.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/z3c.objpath-1.1-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.dublincore-3.7.0-py2.7.egg',
  '/home/vagrant/buildout-cache/eggs/zope.keyreference-3.6.4-py2.7.egg',
  ]


import getopt
import string
import sys

from PIL import Image


def usage():
    print("PIL Convert 0.5/1998-12-30 -- convert image files")
    print("Usage: pilconvert [option] infile outfile")
    print()
    print("Options:")
    print()
    print("  -c <format>  convert to format (default is given by extension)")
    print()
    print("  -g           convert to greyscale")
    print("  -p           convert to palette image (using standard palette)")
    print("  -r           convert to rgb")
    print()
    print("  -o           optimize output (trade speed for size)")
    print("  -q <value>   set compression quality (0-100, JPEG only)")
    print()
    print("  -f           list supported file formats")
    sys.exit(1)

if len(sys.argv) == 1:
    usage()

try:
    opt, argv = getopt.getopt(sys.argv[1:], "c:dfgopq:r")
except getopt.error as v:
    print(v)
    sys.exit(1)

output_format = None
convert = None

options = {}

for o, a in opt:

    if o == "-f":
        Image.init()
        id = sorted(Image.ID)
        print("Supported formats (* indicates output format):")
        for i in id:
            if i in Image.SAVE:
                print(i+"*", end=' ')
            else:
                print(i, end=' ')
        sys.exit(1)

    elif o == "-c":
        output_format = a

    if o == "-g":
        convert = "L"
    elif o == "-p":
        convert = "P"
    elif o == "-r":
        convert = "RGB"

    elif o == "-o":
        options["optimize"] = 1
    elif o == "-q":
        options["quality"] = string.atoi(a)

if len(argv) != 2:
    usage()

try:
    im = Image.open(argv[0])
    if convert and im.mode != convert:
        im.draft(convert, im.size)
        im = im.convert(convert)
    if output_format:
        im.save(argv[1], output_format, **options)
    else:
        im.save(argv[1], **options)
except:
    print("cannot convert image", end=' ')
    print("(%s:%s)" % (sys.exc_info()[0], sys.exc_info()[1]))
