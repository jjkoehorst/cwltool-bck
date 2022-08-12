# Stubs for networkx.algorithms.connectivity.edge_kcomponents (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any

def k_edge_components(G, k): ...
def k_edge_subgraphs(G, k): ...
def bridge_components(G): ...

class EdgeComponentAuxGraph:
    @classmethod
    A: Any = ...
    H: Any = ...
    def construct(EdgeComponentAuxGraph, G): ...
    def k_edge_components(self, k): ...
    def k_edge_subgraphs(self, k): ...
