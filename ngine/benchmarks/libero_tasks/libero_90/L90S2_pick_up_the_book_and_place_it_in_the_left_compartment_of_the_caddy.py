# Copyright 2025 ngine Contributors
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

import numpy as np
import ngine.utils.object_utils as OU
from ngine.engine.models.fixtures import FixtureType
from ngine.engine.tasks.base import TaskBase
from ngine.benchmarks.libero_tasks.base.libero_book_in_caddy_base import BookInCaddyBase


class L90S2PickUpTheBookAndPlaceItInTheLeftCompartmentOfTheCaddy(BookInCaddyBase):
    task_name: str = "L90S2PickUpTheBookAndPlaceItInTheLeftCompartmentOfTheCaddy"

    def get_ep_meta(self):
        ep_meta = super().get_ep_meta()
        ep_meta["lang"] = "Pick up the book and place it in the left compartment of the caddy."
        return ep_meta

    def _check_success(self, env):
        # TODO: add compartment-level check (left half of caddy) when utility is available
        return self._success_common(env)
