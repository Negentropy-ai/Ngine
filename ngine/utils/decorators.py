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

def rl_on(task=None, embodiment=None):
    from ngine.engine.tasks.base import TaskBase
    from ngine.engine.embodiments.robot_arena_base import RobotBase

    if task is not None:
        if not issubclass(task, TaskBase):
            raise TypeError(f"task must be a subclass of TaskBase, got {type(task)}")

    if embodiment is not None:
        if not issubclass(embodiment, RobotBase):
            raise TypeError(f"embodiment must be a subclass of RobotBase, got {type(embodiment)}")

    def wrapper(cls):
        if task:
            cls._rl_on_tasks.append(task)
        if embodiment:
            cls._rl_on_embodiments.append(embodiment)
        return cls

    return wrapper
