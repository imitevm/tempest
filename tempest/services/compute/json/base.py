# Copyright 2015 NEC Corporation.  All rights reserved.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

from tempest_lib.common import rest_client


class BaseComputeClient(rest_client.RestClient):
    api_microversion = None

    def get_headers(self):
        headers = super(BaseComputeClient, self).get_headers()
        if self.api_microversion:
            headers['X-OpenStack-Nova-API-Version'] = self.api_microversion
        return headers

    def set_api_microversion(self, microversion):
        self.api_microversion = microversion