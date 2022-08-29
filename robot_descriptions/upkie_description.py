#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Copyright 2022 Stéphane Caron
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

"""
Upkie description.
"""

import os as _os

from .git import git_clone_description as _git_clone_description

__version__ = "0.1.0"


def _get_repository():
    """
    Get git repository for the robot description.
    """
    return _git_clone_description(
        "https://github.com/tasts-robots/upkie_description.git"
    )


MESHES_PATH: str = ""
PATH: str = ""
URDF_PATH: str = ""

__repo__ = _get_repository()
if __repo__.working_dir is not None:
    MESHES_PATH = _os.path.join(__repo__.working_dir, "meshes")
    PATH = __repo__.working_dir
    URDF_PATH = _os.path.join(__repo__.working_dir, "urdf", "upkie.urdf")
else:  # __repo__.working_dir is None
    raise ImportError("Git repository for the robot description is empty")


__all__ = [
    "MESHES_PATH",
    "PATH",
    "URDF_PATH",
]