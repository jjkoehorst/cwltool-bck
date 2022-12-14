# Stubs for networkx.algorithms.assortativity.correlation (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def degree_assortativity_coefficient(
    G,
    x: str = ...,
    y: str = ...,
    weight: Optional[Any] = ...,
    nodes: Optional[Any] = ...,
): ...
def degree_pearson_correlation_coefficient(
    G,
    x: str = ...,
    y: str = ...,
    weight: Optional[Any] = ...,
    nodes: Optional[Any] = ...,
): ...
def attribute_assortativity_coefficient(G, attribute, nodes: Optional[Any] = ...): ...
def numeric_assortativity_coefficient(G, attribute, nodes: Optional[Any] = ...): ...
