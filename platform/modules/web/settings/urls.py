#
# Copyright 2017 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS-IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

"""Django Url Configuration."""

__author__ = 'Pavel Simakov (psimakov@google.com)'

from common import rest
from django.conf import urls
from django.contrib import admin
from modules.web.cms import admin as cms_admin

urlpatterns = [
    # REST API
    urls.url(r'^api/v1/ping', rest.PingHandler.as_view()),
    # Admin App
    urls.url(r'', urls.include(admin.site.urls)),
]

handler500 = cms_admin.server_error
