# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import sys
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
if sys.version_info >= (3, 11):
    from typing import NotRequired, TypedDict, TypeAlias
else:
    from typing_extensions import NotRequired, TypedDict, TypeAlias
from . import _utilities

__all__ = ['PurrlArgs', 'Purrl']

@pulumi.input_type
class PurrlArgs:
    def __init__(__self__, *,
                 method: pulumi.Input[str],
                 name: pulumi.Input[str],
                 response_codes: pulumi.Input[Sequence[pulumi.Input[str]]],
                 url: pulumi.Input[str],
                 body: Optional[pulumi.Input[str]] = None,
                 ca_cert: Optional[pulumi.Input[str]] = None,
                 cert: Optional[pulumi.Input[str]] = None,
                 delete_body: Optional[pulumi.Input[str]] = None,
                 delete_ca_cert: Optional[pulumi.Input[str]] = None,
                 delete_cert: Optional[pulumi.Input[str]] = None,
                 delete_headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 delete_insecure_skip_tls_verify: Optional[pulumi.Input[bool]] = None,
                 delete_key: Optional[pulumi.Input[str]] = None,
                 delete_method: Optional[pulumi.Input[str]] = None,
                 delete_response_codes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 delete_url: Optional[pulumi.Input[str]] = None,
                 headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 insecure_skip_tls_verify: Optional[pulumi.Input[bool]] = None,
                 key: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Purrl resource.
        :param pulumi.Input[str] method: The HTTP method to use.
        :param pulumi.Input[str] name: The name for this API call.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] response_codes: The expected response code.
        :param pulumi.Input[str] url: The API endpoint to call.
        :param pulumi.Input[str] body: The body of the request.
        :param pulumi.Input[str] ca_cert: The CA certificate if server cert is not signed by a trusted CA.
        :param pulumi.Input[str] cert: The client certificate to use for TLS verification.
        :param pulumi.Input[str] delete_body: The body of the request.
        :param pulumi.Input[str] delete_ca_cert: The CA certificate if server cert is not signed by a trusted CA.
        :param pulumi.Input[str] delete_cert: The client certificate to use for TLS verification.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] delete_headers: The headers to send with the request.
        :param pulumi.Input[bool] delete_insecure_skip_tls_verify: Skip TLS verification.
        :param pulumi.Input[str] delete_key: The client key to use for TLS verification.
        :param pulumi.Input[str] delete_method: The HTTP method to use.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] delete_response_codes: The expected response code.
        :param pulumi.Input[str] delete_url: The API endpoint to call.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] headers: The headers to send with the request.
        :param pulumi.Input[bool] insecure_skip_tls_verify: Skip TLS verification.
        :param pulumi.Input[str] key: The client key to use for TLS verification.
        """
        pulumi.set(__self__, "method", method)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "response_codes", response_codes)
        pulumi.set(__self__, "url", url)
        if body is not None:
            pulumi.set(__self__, "body", body)
        if ca_cert is not None:
            pulumi.set(__self__, "ca_cert", ca_cert)
        if cert is not None:
            pulumi.set(__self__, "cert", cert)
        if delete_body is not None:
            pulumi.set(__self__, "delete_body", delete_body)
        if delete_ca_cert is not None:
            pulumi.set(__self__, "delete_ca_cert", delete_ca_cert)
        if delete_cert is not None:
            pulumi.set(__self__, "delete_cert", delete_cert)
        if delete_headers is not None:
            pulumi.set(__self__, "delete_headers", delete_headers)
        if delete_insecure_skip_tls_verify is not None:
            pulumi.set(__self__, "delete_insecure_skip_tls_verify", delete_insecure_skip_tls_verify)
        if delete_key is not None:
            pulumi.set(__self__, "delete_key", delete_key)
        if delete_method is not None:
            pulumi.set(__self__, "delete_method", delete_method)
        if delete_response_codes is not None:
            pulumi.set(__self__, "delete_response_codes", delete_response_codes)
        if delete_url is not None:
            pulumi.set(__self__, "delete_url", delete_url)
        if headers is not None:
            pulumi.set(__self__, "headers", headers)
        if insecure_skip_tls_verify is not None:
            pulumi.set(__self__, "insecure_skip_tls_verify", insecure_skip_tls_verify)
        if key is not None:
            pulumi.set(__self__, "key", key)

    @property
    @pulumi.getter
    def method(self) -> pulumi.Input[str]:
        """
        The HTTP method to use.
        """
        return pulumi.get(self, "method")

    @method.setter
    def method(self, value: pulumi.Input[str]):
        pulumi.set(self, "method", value)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name for this API call.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="responseCodes")
    def response_codes(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The expected response code.
        """
        return pulumi.get(self, "response_codes")

    @response_codes.setter
    def response_codes(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "response_codes", value)

    @property
    @pulumi.getter
    def url(self) -> pulumi.Input[str]:
        """
        The API endpoint to call.
        """
        return pulumi.get(self, "url")

    @url.setter
    def url(self, value: pulumi.Input[str]):
        pulumi.set(self, "url", value)

    @property
    @pulumi.getter
    def body(self) -> Optional[pulumi.Input[str]]:
        """
        The body of the request.
        """
        return pulumi.get(self, "body")

    @body.setter
    def body(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "body", value)

    @property
    @pulumi.getter(name="caCert")
    def ca_cert(self) -> Optional[pulumi.Input[str]]:
        """
        The CA certificate if server cert is not signed by a trusted CA.
        """
        return pulumi.get(self, "ca_cert")

    @ca_cert.setter
    def ca_cert(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ca_cert", value)

    @property
    @pulumi.getter
    def cert(self) -> Optional[pulumi.Input[str]]:
        """
        The client certificate to use for TLS verification.
        """
        return pulumi.get(self, "cert")

    @cert.setter
    def cert(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cert", value)

    @property
    @pulumi.getter(name="deleteBody")
    def delete_body(self) -> Optional[pulumi.Input[str]]:
        """
        The body of the request.
        """
        return pulumi.get(self, "delete_body")

    @delete_body.setter
    def delete_body(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delete_body", value)

    @property
    @pulumi.getter(name="deleteCaCert")
    def delete_ca_cert(self) -> Optional[pulumi.Input[str]]:
        """
        The CA certificate if server cert is not signed by a trusted CA.
        """
        return pulumi.get(self, "delete_ca_cert")

    @delete_ca_cert.setter
    def delete_ca_cert(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delete_ca_cert", value)

    @property
    @pulumi.getter(name="deleteCert")
    def delete_cert(self) -> Optional[pulumi.Input[str]]:
        """
        The client certificate to use for TLS verification.
        """
        return pulumi.get(self, "delete_cert")

    @delete_cert.setter
    def delete_cert(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delete_cert", value)

    @property
    @pulumi.getter(name="deleteHeaders")
    def delete_headers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The headers to send with the request.
        """
        return pulumi.get(self, "delete_headers")

    @delete_headers.setter
    def delete_headers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "delete_headers", value)

    @property
    @pulumi.getter(name="deleteInsecureSkipTLSVerify")
    def delete_insecure_skip_tls_verify(self) -> Optional[pulumi.Input[bool]]:
        """
        Skip TLS verification.
        """
        return pulumi.get(self, "delete_insecure_skip_tls_verify")

    @delete_insecure_skip_tls_verify.setter
    def delete_insecure_skip_tls_verify(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "delete_insecure_skip_tls_verify", value)

    @property
    @pulumi.getter(name="deleteKey")
    def delete_key(self) -> Optional[pulumi.Input[str]]:
        """
        The client key to use for TLS verification.
        """
        return pulumi.get(self, "delete_key")

    @delete_key.setter
    def delete_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delete_key", value)

    @property
    @pulumi.getter(name="deleteMethod")
    def delete_method(self) -> Optional[pulumi.Input[str]]:
        """
        The HTTP method to use.
        """
        return pulumi.get(self, "delete_method")

    @delete_method.setter
    def delete_method(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delete_method", value)

    @property
    @pulumi.getter(name="deleteResponseCodes")
    def delete_response_codes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The expected response code.
        """
        return pulumi.get(self, "delete_response_codes")

    @delete_response_codes.setter
    def delete_response_codes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "delete_response_codes", value)

    @property
    @pulumi.getter(name="deleteUrl")
    def delete_url(self) -> Optional[pulumi.Input[str]]:
        """
        The API endpoint to call.
        """
        return pulumi.get(self, "delete_url")

    @delete_url.setter
    def delete_url(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "delete_url", value)

    @property
    @pulumi.getter
    def headers(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The headers to send with the request.
        """
        return pulumi.get(self, "headers")

    @headers.setter
    def headers(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "headers", value)

    @property
    @pulumi.getter(name="insecureSkipTLSVerify")
    def insecure_skip_tls_verify(self) -> Optional[pulumi.Input[bool]]:
        """
        Skip TLS verification.
        """
        return pulumi.get(self, "insecure_skip_tls_verify")

    @insecure_skip_tls_verify.setter
    def insecure_skip_tls_verify(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "insecure_skip_tls_verify", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        The client key to use for TLS verification.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)


class Purrl(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 ca_cert: Optional[pulumi.Input[str]] = None,
                 cert: Optional[pulumi.Input[str]] = None,
                 delete_body: Optional[pulumi.Input[str]] = None,
                 delete_ca_cert: Optional[pulumi.Input[str]] = None,
                 delete_cert: Optional[pulumi.Input[str]] = None,
                 delete_headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 delete_insecure_skip_tls_verify: Optional[pulumi.Input[bool]] = None,
                 delete_key: Optional[pulumi.Input[str]] = None,
                 delete_method: Optional[pulumi.Input[str]] = None,
                 delete_response_codes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 delete_url: Optional[pulumi.Input[str]] = None,
                 headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 insecure_skip_tls_verify: Optional[pulumi.Input[bool]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 method: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 response_codes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A Pulumi provider for making API calls

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] body: The body of the request.
        :param pulumi.Input[str] ca_cert: The CA certificate if server cert is not signed by a trusted CA.
        :param pulumi.Input[str] cert: The client certificate to use for TLS verification.
        :param pulumi.Input[str] delete_body: The body of the request.
        :param pulumi.Input[str] delete_ca_cert: The CA certificate if server cert is not signed by a trusted CA.
        :param pulumi.Input[str] delete_cert: The client certificate to use for TLS verification.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] delete_headers: The headers to send with the request.
        :param pulumi.Input[bool] delete_insecure_skip_tls_verify: Skip TLS verification.
        :param pulumi.Input[str] delete_key: The client key to use for TLS verification.
        :param pulumi.Input[str] delete_method: The HTTP method to use.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] delete_response_codes: The expected response code.
        :param pulumi.Input[str] delete_url: The API endpoint to call.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] headers: The headers to send with the request.
        :param pulumi.Input[bool] insecure_skip_tls_verify: Skip TLS verification.
        :param pulumi.Input[str] key: The client key to use for TLS verification.
        :param pulumi.Input[str] method: The HTTP method to use.
        :param pulumi.Input[str] name: The name for this API call.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] response_codes: The expected response code.
        :param pulumi.Input[str] url: The API endpoint to call.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PurrlArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A Pulumi provider for making API calls

        :param str resource_name: The name of the resource.
        :param PurrlArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PurrlArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 body: Optional[pulumi.Input[str]] = None,
                 ca_cert: Optional[pulumi.Input[str]] = None,
                 cert: Optional[pulumi.Input[str]] = None,
                 delete_body: Optional[pulumi.Input[str]] = None,
                 delete_ca_cert: Optional[pulumi.Input[str]] = None,
                 delete_cert: Optional[pulumi.Input[str]] = None,
                 delete_headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 delete_insecure_skip_tls_verify: Optional[pulumi.Input[bool]] = None,
                 delete_key: Optional[pulumi.Input[str]] = None,
                 delete_method: Optional[pulumi.Input[str]] = None,
                 delete_response_codes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 delete_url: Optional[pulumi.Input[str]] = None,
                 headers: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 insecure_skip_tls_verify: Optional[pulumi.Input[bool]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 method: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 response_codes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 url: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PurrlArgs.__new__(PurrlArgs)

            __props__.__dict__["body"] = body
            __props__.__dict__["ca_cert"] = ca_cert
            __props__.__dict__["cert"] = cert
            __props__.__dict__["delete_body"] = delete_body
            __props__.__dict__["delete_ca_cert"] = delete_ca_cert
            __props__.__dict__["delete_cert"] = delete_cert
            __props__.__dict__["delete_headers"] = delete_headers
            __props__.__dict__["delete_insecure_skip_tls_verify"] = delete_insecure_skip_tls_verify
            __props__.__dict__["delete_key"] = delete_key
            __props__.__dict__["delete_method"] = delete_method
            __props__.__dict__["delete_response_codes"] = delete_response_codes
            __props__.__dict__["delete_url"] = delete_url
            __props__.__dict__["headers"] = headers
            __props__.__dict__["insecure_skip_tls_verify"] = insecure_skip_tls_verify
            __props__.__dict__["key"] = key
            if method is None and not opts.urn:
                raise TypeError("Missing required property 'method'")
            __props__.__dict__["method"] = method
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if response_codes is None and not opts.urn:
                raise TypeError("Missing required property 'response_codes'")
            __props__.__dict__["response_codes"] = response_codes
            if url is None and not opts.urn:
                raise TypeError("Missing required property 'url'")
            __props__.__dict__["url"] = url
            __props__.__dict__["delete_response"] = None
            __props__.__dict__["response"] = None
            __props__.__dict__["response_code"] = None
        super(Purrl, __self__).__init__(
            'purrl:index:Purrl',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Purrl':
        """
        Get an existing Purrl resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PurrlArgs.__new__(PurrlArgs)

        __props__.__dict__["body"] = None
        __props__.__dict__["ca_cert"] = None
        __props__.__dict__["cert"] = None
        __props__.__dict__["delete_body"] = None
        __props__.__dict__["delete_ca_cert"] = None
        __props__.__dict__["delete_cert"] = None
        __props__.__dict__["delete_headers"] = None
        __props__.__dict__["delete_insecure_skip_tls_verify"] = None
        __props__.__dict__["delete_key"] = None
        __props__.__dict__["delete_method"] = None
        __props__.__dict__["delete_response"] = None
        __props__.__dict__["delete_response_codes"] = None
        __props__.__dict__["delete_url"] = None
        __props__.__dict__["headers"] = None
        __props__.__dict__["insecure_skip_tls_verify"] = None
        __props__.__dict__["key"] = None
        __props__.__dict__["method"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["response"] = None
        __props__.__dict__["response_code"] = None
        __props__.__dict__["response_codes"] = None
        __props__.__dict__["url"] = None
        return Purrl(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def body(self) -> pulumi.Output[Optional[str]]:
        """
        The body of the request.
        """
        return pulumi.get(self, "body")

    @property
    @pulumi.getter(name="caCert")
    def ca_cert(self) -> pulumi.Output[Optional[str]]:
        """
        The CA certificate if server cert is not signed by a trusted CA.
        """
        return pulumi.get(self, "ca_cert")

    @property
    @pulumi.getter
    def cert(self) -> pulumi.Output[Optional[str]]:
        """
        The client certificate to use for TLS verification.
        """
        return pulumi.get(self, "cert")

    @property
    @pulumi.getter(name="deleteBody")
    def delete_body(self) -> pulumi.Output[Optional[str]]:
        """
        The body of the request.
        """
        return pulumi.get(self, "delete_body")

    @property
    @pulumi.getter(name="deleteCaCert")
    def delete_ca_cert(self) -> pulumi.Output[Optional[str]]:
        """
        The CA certificate if server cert is not signed by a trusted CA.
        """
        return pulumi.get(self, "delete_ca_cert")

    @property
    @pulumi.getter(name="deleteCert")
    def delete_cert(self) -> pulumi.Output[Optional[str]]:
        """
        The client certificate to use for TLS verification.
        """
        return pulumi.get(self, "delete_cert")

    @property
    @pulumi.getter(name="deleteHeaders")
    def delete_headers(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The headers to send with the request.
        """
        return pulumi.get(self, "delete_headers")

    @property
    @pulumi.getter(name="deleteInsecureSkipTLSVerify")
    def delete_insecure_skip_tls_verify(self) -> pulumi.Output[Optional[bool]]:
        """
        Skip TLS verification.
        """
        return pulumi.get(self, "delete_insecure_skip_tls_verify")

    @property
    @pulumi.getter(name="deleteKey")
    def delete_key(self) -> pulumi.Output[Optional[str]]:
        """
        The client key to use for TLS verification.
        """
        return pulumi.get(self, "delete_key")

    @property
    @pulumi.getter(name="deleteMethod")
    def delete_method(self) -> pulumi.Output[Optional[str]]:
        """
        The HTTP method to use.
        """
        return pulumi.get(self, "delete_method")

    @property
    @pulumi.getter(name="deleteResponse")
    def delete_response(self) -> pulumi.Output[Optional[str]]:
        """
        The response from the API call.
        """
        return pulumi.get(self, "delete_response")

    @property
    @pulumi.getter(name="deleteResponseCodes")
    def delete_response_codes(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The expected response code.
        """
        return pulumi.get(self, "delete_response_codes")

    @property
    @pulumi.getter(name="deleteUrl")
    def delete_url(self) -> pulumi.Output[Optional[str]]:
        """
        The API endpoint to call.
        """
        return pulumi.get(self, "delete_url")

    @property
    @pulumi.getter
    def headers(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The headers to send with the request.
        """
        return pulumi.get(self, "headers")

    @property
    @pulumi.getter(name="insecureSkipTLSVerify")
    def insecure_skip_tls_verify(self) -> pulumi.Output[Optional[bool]]:
        """
        Skip TLS verification.
        """
        return pulumi.get(self, "insecure_skip_tls_verify")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[Optional[str]]:
        """
        The client key to use for TLS verification.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def method(self) -> pulumi.Output[str]:
        """
        The HTTP method to use.
        """
        return pulumi.get(self, "method")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name for this API call.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def response(self) -> pulumi.Output[str]:
        """
        The response from the API call.
        """
        return pulumi.get(self, "response")

    @property
    @pulumi.getter(name="responseCode")
    def response_code(self) -> pulumi.Output[int]:
        return pulumi.get(self, "response_code")

    @property
    @pulumi.getter(name="responseCodes")
    def response_codes(self) -> pulumi.Output[Sequence[str]]:
        """
        The expected response code.
        """
        return pulumi.get(self, "response_codes")

    @property
    @pulumi.getter
    def url(self) -> pulumi.Output[str]:
        """
        The API endpoint to call.
        """
        return pulumi.get(self, "url")

