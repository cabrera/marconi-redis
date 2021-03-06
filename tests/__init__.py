# Copyright (c) 2013 Red Hat, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
# implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import os

tests_dir = os.path.abspath(os.path.dirname(__file__))
os.environ.setdefault("MARCONI_TESTS_DIR", tests_dir)

if "MARCONI_TESTS_CONFIGS_DIR" not in os.environ:
    os.environ["MARCONI_TESTS_CONFIGS_DIR"] = os.path.join(tests_dir, "etc")
