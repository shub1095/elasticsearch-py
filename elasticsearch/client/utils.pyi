# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

from __future__ import unicode_literals

from typing import (
    Collection,
    Any,
    Optional,
    Union,
    Dict,
    List,
    Tuple,
    Callable,
    TypeVar,
)
from ..client import Elasticsearch
from ..serializer import Serializer
from ..transport import Transport

T = TypeVar("T")
SKIP_IN_PATH: Collection[Any]

def _normalize_hosts(
    hosts: Optional[Union[str, Collection[Union[str, Dict[str, Any]]]]]
) -> List[Dict[str, Any]]: ...
def _escape(value: Any) -> str: ...
def _make_path(*parts: Any) -> str: ...

GLOBAL_PARAMS: Tuple[str, ...]

def query_params(
    *es_query_params: str,
) -> Callable[[Callable[..., T]], Callable[..., T]]: ...
def _bulk_body(
    serializer: Serializer, body: Union[str, bytes, Collection[Any]]
) -> str: ...

class NamespacedClient:
    client: Elasticsearch
    def __init__(self, client: Elasticsearch) -> None: ...
    @property
    def transport(self) -> Transport: ...
