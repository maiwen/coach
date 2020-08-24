#
# Copyright (c) 2020 maiwen
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from enum import Enum
from typing import Union, List
import numpy as np
from rl_coach.environments.army_match.env_framework.env import *
from rl_coach.filters.observation.observation_move_axis_filter import ObservationMoveAxisFilter

from rl_coach.environments.environment import Environment, EnvironmentParameters, LevelSelection
from rl_coach.base_parameters import VisualizationParameters
from rl_coach.spaces import BoxActionSpace, VectorObservationSpace, PlanarMapsObservationSpace, StateSpace, CompoundActionSpace, \
    DiscreteActionSpace
from rl_coach.filters.filter import InputFilter, OutputFilter
from rl_coach.filters.observation.observation_rescale_to_size_filter import ObservationRescaleToSizeFilter
from rl_coach.filters.action.linear_box_to_box_map import LinearBoxToBoxMap
from rl_coach.filters.observation.observation_to_uint8_filter import ObservationToUInt8Filter


# Environment
class ArmyMatchEnvironment(Environment):
    def __init__(self, name):
        self.name = name
        self.env_id = "0"

