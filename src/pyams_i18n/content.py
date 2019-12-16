#
# Copyright (c) 2008-2015 Thierry Florac <tflorac AT ulthar.net>
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#

"""PyAMS_i18n.content module

"""

from zope.interface import implementer
from zope.schema.fieldproperty import FieldProperty

from pyams_i18n.interfaces import II18nManager, INegotiator
from pyams_utils.registry import query_utility


__docformat__ = 'restructuredtext'


@implementer(II18nManager)
class I18nManagerMixin(object):
    """I18n manager class mixin"""

    languages = FieldProperty(II18nManager['languages'])

    def get_languages(self):
        langs = []
        negotiator = query_utility(INegotiator)
        if negotiator is not None:
            langs.append(negotiator.server_language)
        langs.extend(sorted(filter(lambda x: x not in langs, self.languages or ())))
        return langs
