# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

import sys
from .errors import BulkIndexError as BulkIndexError, ScanError as ScanError
from .actions import (
    expand_action as expand_action,
    streaming_bulk as streaming_bulk,
    bulk as bulk,
    parallel_bulk as parallel_bulk,
    scan as scan,
    reindex as reindex,
    _chunk_actions as _chunk_actions,
    _process_bulk_chunk as _process_bulk_chunk,
)

try:
    # Asyncio only supported on Python 3.6+
    if sys.version_info < (3, 6):
        raise ImportError

    from .._async.helpers import (
        async_scan as async_scan,
        async_bulk as async_bulk,
        async_reindex as async_reindex,
        async_streaming_bulk as async_streaming_bulk,
    )
except (ImportError, SyntaxError):
    pass
