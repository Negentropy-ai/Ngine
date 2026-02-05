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
from ngine.engine.tasks.base import TaskBase
from ngine.engine.models.fixtures import FixtureType


class PutOnStoveBase(TaskBase):
    task_name: str = "PutOnStoveBase"

    enable_fixtures = ['mokapot_1', 'stovetop']
    movable_fixtures = ['mokapot_1']


class PutMokaPotOnStoveBase(TaskBase):
    task_name: str = "PutMokaPotOnStoveBase"

    enable_fixtures = ['mokapot_1', 'mokapot_2', 'stovetop']
    movable_fixtures = ['mokapot_1', 'mokapot_2']

    def _setup_kitchen_references(self, scene):
        super()._setup_kitchen_references(scene)
        self.counter = self.register_fixture_ref("table", dict(id=FixtureType.TABLE))
        self.stove = self.register_fixture_ref("stovetop", dict(id=FixtureType.STOVE))
        self.mokapot_1 = self.register_fixture_ref("mokapot_1", dict(id="mokapot_1"))
        self.mokapot_2 = self.register_fixture_ref("mokapot_2", dict(id="mokapot_2"))
        self.init_robot_base_ref = self.counter
        self.frying_pan = "chefmate_8_frypan"

    def _get_obj_cfgs(self):
        cfgs = []

        pan_pl = dict(
            fixture=self.counter,
            size=(0.5, 0.5),
            pos=(1.0, -0.75),
            rotation=-np.pi / 2,
            margin=0.02,
            ensure_valid_placement=True,
        )

        cfgs.append(
            dict(
                name=self.frying_pan,
                obj_groups="pot",
                graspable=True,
                placement=pan_pl,
                asset_name="Pot086.usd",
            )
        )

        return cfgs
