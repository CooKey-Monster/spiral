# Copyright 2020 The TensorFlow Authors. All Rights Reserved.
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
# ==============================================================================
"""common types for the dtdg package.

This file define the types required for dtdg package
"""

from nptyping import Float64, NDArray


class Edge:
    """An edge in the source data."""

    def __init__(self, src: int, dst: int, index: int, feature: NDArray[Float64]):
        """An edge in the source data."""
        self.src = src
        self.dst = dst
        self.id = index
        self.feature = feature


class Snapshot:
    """A snapshot of a dynamic graph.

    The snapshot is usually a tuple (A,X,E,t) where X is the node feature table,
    A is the adjacency matrix, E is the edge feature table
    and t is the timestamp. In this implementation, A is represented by DGL.graph,
    X and E is nullable two - D matrix, with row id to be the node or edge index,
    corresponding to the one use in constructing the DGL.graph.

    When designing this class, our primary goal is to support the loading of dynamic graph data
    in 'https://snap.stanford.edu/data/',
    """

    def __init__(self, edges):
        """An edge in the source data."""
        self.edges = edges