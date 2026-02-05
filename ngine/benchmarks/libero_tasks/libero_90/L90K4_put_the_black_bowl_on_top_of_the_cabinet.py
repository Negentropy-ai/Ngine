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

import torch
import ngine.utils.object_utils as OU
from ngine.engine.models.fixtures import FixtureType
from ngine.engine.tasks.base import TaskBase
from ngine.benchmarks.libero_tasks.libero_90.L90K4_close_the_bottom_drawer_of_the_cabinet import L90K4CloseTheBottomDrawerOfTheCabinet


class L90K4PutTheBlackBowlOnTopOfTheCabinet(L90K4CloseTheBottomDrawerOfTheCabinet):
    task_name: str = "L90K4PutTheBlackBowlOnTopOfTheCabinet"

    def get_ep_meta(self):
        ep_meta = super().get_ep_meta()
        ep_meta["lang"] = "Put the black bowl on top of the cabinet."
        return ep_meta

    def _check_success(self, env):
        bowl_success = OU.obj_inside_of(env, self.akita_black_bowl, self.drawer)
        return bowl_success & OU.gripper_obj_far(env, self.akita_black_bowl)
