from typing import Any, Iterator

from rdflib.graph import Graph
from rdflib.term import Node

class Collection:
    graph: Graph
    uri: Node
    def __init__(self, graph: Graph, uri: Node, seq: Any = ...) -> None: ...
    def n3(self) -> str: ...
    def __len__(self) -> int: ...
    def index(self, item: Any) -> int: ...
    def __getitem__(self, key: str) -> Any: ...
    def __setitem__(self, key: str, value: Any) -> None: ...
    def __delitem__(self, key: str) -> None: ...
    def __iter__(self) -> Iterator[Any]: ...
    def append(self, item: Any) -> Collection: ...
    def __iadd__(self, other: Any) -> Collection: ...
    def clear(self) -> Collection: ...
