# Copyright 2017 The Nuclio Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import nuclio_sdk
import nuclio_sdk.event


class Context(object):

    def __init__(self, logger=None, platform=None, worker_id=None, trigger=None):
        self.platform = platform or nuclio_sdk.Platform('test')
        self.logger = logger
        self.user_data = lambda: None
        self.Response = nuclio_sdk.Response
        self.worker_id = worker_id
        self.trigger = trigger

        # for backwards compatibility
        if self.trigger is not None:
            self.trigger_name = self.trigger.name
