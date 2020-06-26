import ssl
from typing import Optional, Mapping, Any, Union
import urllib3  # type: ignore
from .base import Connection

def create_ssl_context(
    cafile: Any = ..., capath: Any = ..., cadata: Any = ...,
) -> ssl.SSLContext: ...

class Urllib3HttpConnection(Connection):
    pool: urllib3.HTTPConnectionPool
    def __init__(
        self,
        host: str = ...,
        port: Optional[int] = ...,
        url_prefix: str = ...,
        timeout: Optional[Union[float, int]] = ...,
        http_auth: Any = ...,
        use_ssl: bool = ...,
        verify_certs: bool = ...,
        ssl_show_warn: bool = ...,
        ca_certs: Any = ...,
        client_cert: Any = ...,
        client_key: Any = ...,
        ssl_version: Any = ...,
        ssl_assert_hostname: Any = ...,
        ssl_assert_fingerprint: Any = ...,
        maxsize: int = ...,
        headers: Optional[Mapping[str, str]] = ...,
        ssl_context: Any = ...,
        http_compress: Optional[bool] = ...,
        cloud_id: Optional[str] = ...,
        api_key: Any = ...,
        opaque_id: Optional[str] = ...,
        **kwargs: Any
    ) -> None: ...
