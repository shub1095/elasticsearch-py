# Licensed to Elasticsearch B.V under one or more agreements.
# Elasticsearch B.V licenses this file to you under the Apache 2.0 License.
# See the LICENSE file in the project root for more information

from typing import Any, Mapping, Optional, Union, Collection
from .utils import NamespacedClient

class CcrClient(NamespacedClient):
    def delete_auto_follow_pattern(
        self,
        name: Any,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
    def follow(
        self,
        index: Any,
        body: Any,
        wait_for_active_shards: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
    def follow_info(
        self,
        index: Any,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
    def follow_stats(
        self,
        index: Any,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
    def forget_follower(
        self,
        index: Any,
        body: Any,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
    def get_auto_follow_pattern(
        self,
        name: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
    def pause_follow(
        self,
        index: Any,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
    def put_auto_follow_pattern(
        self,
        name: Any,
        body: Any,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
    def resume_follow(
        self,
        index: Any,
        body: Optional[Any] = ...,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
    def stats(
        self,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
    def unfollow(
        self,
        index: Any,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
    def pause_auto_follow_pattern(
        self,
        name: Any,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
    def resume_auto_follow_pattern(
        self,
        name: Any,
        pretty: Optional[bool] = ...,
        human: Optional[bool] = ...,
        error_trace: Optional[bool] = ...,
        format: Optional[str] = ...,
        filter_path: Optional[Union[str, Collection[str]]] = ...,
        request_timeout: Optional[Union[int, float]] = ...,
        params: Optional[Mapping[str, Any]] = ...,
        headers: Optional[Mapping[str, str]] = ...,
    ) -> Any: ...
