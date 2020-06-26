# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

from typing import Any, Mapping, Optional, Union, Collection
from .utils import NamespacedClient

class RemoteClient(NamespacedClient):
    async def info(
        self,
        timeout: Optional[Any] = None,
        pretty: Optional[bool] = None,
        human: Optional[bool] = None,
        error_trace: Optional[bool] = None,
        format: Optional[str] = None,
        filter_path: Optional[Union[str, Collection[str]]] = None,
        params: Optional[Mapping[str, Any]] = None,
        headers: Optional[Mapping[str, str]] = None,
    ) -> Any: ...
