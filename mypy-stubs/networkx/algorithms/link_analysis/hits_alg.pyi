# Stubs for networkx.algorithms.link_analysis.hits_alg (Python 3.5)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional

def hits(
    G,
    max_iter: int = ...,
    tol: float = ...,
    nstart: Optional[Any] = ...,
    normalized: bool = ...,
): ...
def authority_matrix(G, nodelist: Optional[Any] = ...): ...
def hub_matrix(G, nodelist: Optional[Any] = ...): ...
def hits_numpy(G, normalized: bool = ...): ...
def hits_scipy(G, max_iter: int = ..., tol: float = ..., normalized: bool = ...): ...
