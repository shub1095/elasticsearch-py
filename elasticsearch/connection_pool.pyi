# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

import logging
from typing import Sequence, Optional, Type, Any, Union, List, Tuple, Dict
from .connection import Connection

try:
    from Queue import PriorityQueue  # type: ignore
except ImportError:
    from queue import PriorityQueue

logger: logging.Logger

class ConnectionSelector(object):
    connection_opts: Sequence[Tuple[Connection, Any]]
    def __init__(self, opts: Sequence[Tuple[Connection, Any]]) -> None: ...
    def select(self, connections: Sequence[Connection]) -> Connection: ...

class RandomSelector(ConnectionSelector): ...
class RoundRobinSelector(ConnectionSelector): ...

class ConnectionPool(object):
    connections_opts: Sequence[Tuple[Connection, Any]]
    connections: Sequence[Connection]
    orig_connections: Tuple[Connection, ...]
    dead: PriorityQueue
    dead_count: Dict[Connection, int]
    dead_timeout: Union[float, int]
    timeout_cutoff: Union[float, int]
    selector: ConnectionSelector
    def __init__(
        self,
        connections: Sequence[Tuple[Connection, Any]],
        dead_timeout: int = ...,
        timeout_cutoff: int = ...,
        selector_class: Type[ConnectionSelector] = ...,
        randomize_hosts: bool = ...,
        **kwargs: Any
    ) -> None: ...
    def mark_dead(self, connection: Connection, now: Optional[float] = ...) -> None: ...
    def mark_live(self, connection: Connection) -> None: ...
    def resurrect(self, force: bool = ...) -> Optional[Connection]: ...
    def get_connection(self) -> Connection: ...
    def close(self) -> None: ...
    def __repr__(self) -> str: ...

class DummyConnectionPool(ConnectionPool):
    def __init__(
        self, connections: Sequence[Tuple[Connection, Any]], **kwargs: Any
    ) -> None: ...
    def get_connection(self) -> Connection: ...
    def close(self) -> None: ...
    def _noop(self, *args: Any, **kwargs: Any) -> Any: ...
    mark_dead = mark_live = resurrect = _noop

class EmptyConnectionPool(ConnectionPool):
    def __init__(self, *_: Any, **__: Any) -> None: ...
    def get_connection(self) -> Connection: ...
    def _noop(self, *args: Any, **kwargs: Any) -> Any: ...
    close = mark_dead = mark_live = resurrect = _noop
