from ._extra_imports import aiohttp  # type: ignore
from typing import Optional, Mapping, Collection, Union, Any, Tuple
from ..connection import Connection

class AsyncConnection(Connection):
    async def perform_request(  # type: ignore
        self,
        method: str,
        url: str,
        params: Optional[Mapping[str, Any]] = ...,
        body: Optional[bytes] = ...,
        timeout: Optional[Union[int, float]] = ...,
        ignore: Collection[int] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Tuple[int, Mapping[str, str], str]: ...
    async def close(self) -> None: ...

class AIOHttpConnection(AsyncConnection):
    session: Optional[aiohttp.ClientSession]
    ssl_assert_fingerprint: Optional[str]
