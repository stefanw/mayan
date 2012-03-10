"""Configuration options for the sources app"""
import os

from django.utils.translation import ugettext_lazy as _
from django.conf import settings

from smart_settings.api import Setting, SettingNamespace

namespace = SettingNamespace('sources', _(u'Sources'), module='sources.conf.settings')

POP3_DEFAULT_TIMEOUT = 10 # POP3 only not SSL
POP3_DEFAULT_EMAIL_PROCESSING_INTERVAL = 15 * 60 # 15 minutes

Setting(
    namespace=namespace,
    name='POP3_TIMEOUT',
    global_name='SOURCES_POP3_TIMEOUT',
    default=POP3_DEFAULT_TIMEOUT,
)

Setting(
    namespace=namespace,
    name='POP3_EMAIL_PROCESSING_INTERVAL',
    global_name='SOURCES_POP3_EMAIL_PROCESSING_INTERVAL',
    default=POP3_DEFAULT_EMAIL_PROCESSING_INTERVAL,
)

