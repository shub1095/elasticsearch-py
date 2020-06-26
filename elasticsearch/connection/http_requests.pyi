from typing import Optional, Any, Mapping
import requests
from .base import Connection

class RequestsHttpConnection(Connection):
    session: requests.Session
    def __init__(
        self,
        host: str = ...,
        port: Optional[int] = ...,
        http_auth: Any = ...,
        use_ssl: bool = ...,
        verify_certs: bool = ...,
        ssl_show_warn: bool = ...,
        ca_certs: Any = ...,
        client_cert: Any = ...,
        client_key: Any = ...,
        headers: Optional[Mapping[str, str]] = ...,
        http_compress: Optional[bool] = ...,
        cloud_id: Optional[str] = ...,
        api_key: Any = ...,
        opaque_id: Optional[str] = ...,
        **kwargs: Any
    ) -> None: ...
