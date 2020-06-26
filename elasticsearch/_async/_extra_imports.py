# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

# type: ignore

# This file exists for the sole reason of making mypy not
# complain about type issues to do with 'aiohttp' and 'yarl'.
# We're in a catch-22 situation:
# - If we use 'type: ignore' on 'import aiohttp' and it's not installed
#   mypy will complain that the annotation is unnecessary.
# - If we don't use 'type: ignore' on 'import aiohttp' and it
#   it's not installed mypy will complain that it can't find
#   type hints for aiohttp.
# So to make mypy happy we move all our 'extra' imports here
# and add a global 'type: ignore' which mypy never complains
# about being unnecessary.

import aiohttp
import aiohttp.client_exceptions as aiohttp_exceptions
import yarl

__all__ = ["aiohttp", "aiohttp_exceptions", "yarl"]
