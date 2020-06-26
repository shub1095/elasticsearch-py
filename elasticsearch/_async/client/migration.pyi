# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

from typing import Any, Mapping, Optional, Union, Collection
from .utils import NamespacedClient

class MigrationClient(NamespacedClient):
    async def deprecations(
        self,
        index: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
