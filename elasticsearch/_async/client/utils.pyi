# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

from ...client.utils import (  # noqa
    _make_path as _make_path,
    _normalize_hosts as _normalize_hosts,
    _escape as _escape,
    _bulk_body as _bulk_body,
    query_params as query_params,
    SKIP_IN_PATH as SKIP_IN_PATH,
)
from ..transport import AsyncTransport
from ..client import AsyncElasticsearch

class NamespacedClient:
    client: AsyncElasticsearch
    def __init__(self, client: AsyncElasticsearch) -> None: ...
    @property
    def transport(self) -> AsyncTransport: ...
