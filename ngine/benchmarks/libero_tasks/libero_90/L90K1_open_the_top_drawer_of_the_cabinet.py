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

import ngine.utils.object_utils as OU
from ngine.engine.models.fixtures import FixtureType
from ngine.engine.tasks.base import TaskBase
from ngine.benchmarks.libero_tasks.libero_90.L90K1_open_the_bottom_drawer_of_the_cabinet import L90K1OpenTheBottomDrawerOfTheCabinet


class L90K1OpenTheTopDrawerOfTheCabinet(L90K1OpenTheBottomDrawerOfTheCabinet):
    task_name: str = "L90K1OpenTheTopDrawerOfTheCabinet"

    def get_ep_meta(self):
        ep_meta = super().get_ep_meta()
        ep_meta[
            "lang"
        ] = f"open the top drawer of the cabinet."
        return ep_meta

    def _check_success(self, env):
        return self.drawer.is_open(env, [self.top_joint_name], th=0.5) & OU.gripper_obj_far(env, self.drawer.name, th=0.5)
