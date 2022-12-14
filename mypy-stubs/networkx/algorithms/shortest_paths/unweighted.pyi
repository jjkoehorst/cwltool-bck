# Stubs for networkx.algorithms.shortest_paths.unweighted (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def single_source_shortest_path_length(G, source, cutoff: Optional[Any] = ...): ...
def single_target_shortest_path_length(G, target, cutoff: Optional[Any] = ...): ...
def all_pairs_shortest_path_length(G, cutoff: Optional[Any] = ...): ...
def bidirectional_shortest_path(G, source, target): ...
def single_source_shortest_path(G, source, cutoff: Optional[Any] = ...): ...
def single_target_shortest_path(G, target, cutoff: Optional[Any] = ...): ...
def all_pairs_shortest_path(G, cutoff: Optional[Any] = ...): ...
def predecessor(
    G,
    source,
    target: Optional[Any] = ...,
    cutoff: Optional[Any] = ...,
    return_seen: Optional[Any] = ...,
): ...
