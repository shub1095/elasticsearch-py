# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

import sys
from typing import Tuple

PY2: bool
string_types: Tuple[type, ...]

if sys.version_info[0] == 2:
    from urllib import (
        quote_plus as quote_plus,
        quote as quote,
        urlencode as urlencode,
        unquote as unquote,
    )
    from urlparse import urlparse as urlparse
    from itertools import imap as map
    from Queue import Queue as Queue
else:
    from urllib.parse import (
        quote as quote,
        quote_plus as quote_plus,
        urlencode as urlencode,
        urlparse as urlparse,
        unquote as unquote,
    )

    map = map
    from queue import Queue as Queue
