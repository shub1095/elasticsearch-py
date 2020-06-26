# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

from typing import List, Any
from ..exceptions import ElasticsearchException

class BulkIndexError(ElasticsearchException):
    @property
    def errors(self) -> List[Any]: ...

class ScanError(ElasticsearchException):
    scroll_id: str
    def __init__(self, scroll_id: str, *args: Any, **kwargs: Any) -> None: ...
