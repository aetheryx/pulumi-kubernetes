# coding=utf-8
# *** WARNING: this file was generated by pulumigen. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ... import core as _core
from ... import meta as _meta

__all__ = [
    'EndpointConditionsArgs',
    'EndpointHintsArgs',
    'EndpointPortArgs',
    'EndpointSliceArgs',
    'EndpointArgs',
    'ForZoneArgs',
]

@pulumi.input_type
class EndpointConditionsArgs:
    def __init__(__self__, *,
                 ready: Optional[pulumi.Input[bool]] = None,
                 serving: Optional[pulumi.Input[bool]] = None,
                 terminating: Optional[pulumi.Input[bool]] = None):
        """
        EndpointConditions represents the current condition of an endpoint.
        :param pulumi.Input[bool] ready: ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. A nil value indicates an unknown state. In most cases consumers should interpret this unknown state as ready. For compatibility reasons, ready should never be "true" for terminating endpoints.
        :param pulumi.Input[bool] serving: serving is identical to ready except that it is set regardless of the terminating state of endpoints. This condition should be set to true for a ready endpoint that is terminating. If nil, consumers should defer to the ready condition. This field can be enabled with the EndpointSliceTerminatingCondition feature gate.
        :param pulumi.Input[bool] terminating: terminating indicates that this endpoint is terminating. A nil value indicates an unknown state. Consumers should interpret this unknown state to mean that the endpoint is not terminating. This field can be enabled with the EndpointSliceTerminatingCondition feature gate.
        """
        if ready is not None:
            pulumi.set(__self__, "ready", ready)
        if serving is not None:
            pulumi.set(__self__, "serving", serving)
        if terminating is not None:
            pulumi.set(__self__, "terminating", terminating)

    @property
    @pulumi.getter
    def ready(self) -> Optional[pulumi.Input[bool]]:
        """
        ready indicates that this endpoint is prepared to receive traffic, according to whatever system is managing the endpoint. A nil value indicates an unknown state. In most cases consumers should interpret this unknown state as ready. For compatibility reasons, ready should never be "true" for terminating endpoints.
        """
        return pulumi.get(self, "ready")

    @ready.setter
    def ready(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "ready", value)

    @property
    @pulumi.getter
    def serving(self) -> Optional[pulumi.Input[bool]]:
        """
        serving is identical to ready except that it is set regardless of the terminating state of endpoints. This condition should be set to true for a ready endpoint that is terminating. If nil, consumers should defer to the ready condition. This field can be enabled with the EndpointSliceTerminatingCondition feature gate.
        """
        return pulumi.get(self, "serving")

    @serving.setter
    def serving(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "serving", value)

    @property
    @pulumi.getter
    def terminating(self) -> Optional[pulumi.Input[bool]]:
        """
        terminating indicates that this endpoint is terminating. A nil value indicates an unknown state. Consumers should interpret this unknown state to mean that the endpoint is not terminating. This field can be enabled with the EndpointSliceTerminatingCondition feature gate.
        """
        return pulumi.get(self, "terminating")

    @terminating.setter
    def terminating(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "terminating", value)


@pulumi.input_type
class EndpointHintsArgs:
    def __init__(__self__, *,
                 for_zones: Optional[pulumi.Input[Sequence[pulumi.Input['ForZoneArgs']]]] = None):
        """
        EndpointHints provides hints describing how an endpoint should be consumed.
        :param pulumi.Input[Sequence[pulumi.Input['ForZoneArgs']]] for_zones: forZones indicates the zone(s) this endpoint should be consumed by to enable topology aware routing.
        """
        if for_zones is not None:
            pulumi.set(__self__, "for_zones", for_zones)

    @property
    @pulumi.getter(name="forZones")
    def for_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ForZoneArgs']]]]:
        """
        forZones indicates the zone(s) this endpoint should be consumed by to enable topology aware routing.
        """
        return pulumi.get(self, "for_zones")

    @for_zones.setter
    def for_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ForZoneArgs']]]]):
        pulumi.set(self, "for_zones", value)


@pulumi.input_type
class EndpointPortArgs:
    def __init__(__self__, *,
                 app_protocol: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None,
                 protocol: Optional[pulumi.Input[str]] = None):
        """
        EndpointPort represents a Port used by an EndpointSlice
        :param pulumi.Input[str] app_protocol: The application protocol for this port. This field follows standard Kubernetes label syntax. Un-prefixed names are reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names). Non-standard protocols should use prefixed names such as mycompany.com/my-custom-protocol.
        :param pulumi.Input[str] name: The name of this port. All ports in an EndpointSlice must have a unique name. If the EndpointSlice is dervied from a Kubernetes service, this corresponds to the Service.ports[].name. Name must either be an empty string or pass DNS_LABEL validation: * must be no more than 63 characters long. * must consist of lower case alphanumeric characters or '-'. * must start and end with an alphanumeric character. Default is empty string.
        :param pulumi.Input[int] port: The port number of the endpoint. If this is not specified, ports are not restricted and must be interpreted in the context of the specific consumer.
        :param pulumi.Input[str] protocol: The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.
        """
        if app_protocol is not None:
            pulumi.set(__self__, "app_protocol", app_protocol)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if port is not None:
            pulumi.set(__self__, "port", port)
        if protocol is not None:
            pulumi.set(__self__, "protocol", protocol)

    @property
    @pulumi.getter(name="appProtocol")
    def app_protocol(self) -> Optional[pulumi.Input[str]]:
        """
        The application protocol for this port. This field follows standard Kubernetes label syntax. Un-prefixed names are reserved for IANA standard service names (as per RFC-6335 and https://www.iana.org/assignments/service-names). Non-standard protocols should use prefixed names such as mycompany.com/my-custom-protocol.
        """
        return pulumi.get(self, "app_protocol")

    @app_protocol.setter
    def app_protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "app_protocol", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of this port. All ports in an EndpointSlice must have a unique name. If the EndpointSlice is dervied from a Kubernetes service, this corresponds to the Service.ports[].name. Name must either be an empty string or pass DNS_LABEL validation: * must be no more than 63 characters long. * must consist of lower case alphanumeric characters or '-'. * must start and end with an alphanumeric character. Default is empty string.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        The port number of the endpoint. If this is not specified, ports are not restricted and must be interpreted in the context of the specific consumer.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)

    @property
    @pulumi.getter
    def protocol(self) -> Optional[pulumi.Input[str]]:
        """
        The IP protocol for this port. Must be UDP, TCP, or SCTP. Default is TCP.
        """
        return pulumi.get(self, "protocol")

    @protocol.setter
    def protocol(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protocol", value)


@pulumi.input_type
class EndpointSliceArgs:
    def __init__(__self__, *,
                 address_type: pulumi.Input[str],
                 endpoints: pulumi.Input[Sequence[pulumi.Input['EndpointArgs']]],
                 api_version: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input['_meta.v1.ObjectMetaArgs']] = None,
                 ports: Optional[pulumi.Input[Sequence[pulumi.Input['EndpointPortArgs']]]] = None):
        """
        EndpointSlice represents a subset of the endpoints that implement a service. For a given service there may be multiple EndpointSlice objects, selected by labels, which must be joined to produce the full set of endpoints.
        :param pulumi.Input[str] address_type: addressType specifies the type of address carried by this EndpointSlice. All addresses in this slice must be the same type. This field is immutable after creation. The following address types are currently supported: * IPv4: Represents an IPv4 Address. * IPv6: Represents an IPv6 Address. * FQDN: Represents a Fully Qualified Domain Name.
               
               Possible enum values:
                - `"FQDN"` represents a FQDN.
                - `"IPv4"` represents an IPv4 Address.
                - `"IPv6"` represents an IPv6 Address.
        :param pulumi.Input[Sequence[pulumi.Input['EndpointArgs']]] endpoints: endpoints is a list of unique endpoints in this slice. Each slice may include a maximum of 1000 endpoints.
        :param pulumi.Input[str] api_version: APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        :param pulumi.Input[str] kind: Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        :param pulumi.Input['_meta.v1.ObjectMetaArgs'] metadata: Standard object's metadata.
        :param pulumi.Input[Sequence[pulumi.Input['EndpointPortArgs']]] ports: ports specifies the list of network ports exposed by each endpoint in this slice. Each port must have a unique name. When ports is empty, it indicates that there are no defined ports. When a port is defined with a nil port value, it indicates "all ports". Each slice may include a maximum of 100 ports.
        """
        pulumi.set(__self__, "address_type", address_type)
        pulumi.set(__self__, "endpoints", endpoints)
        if api_version is not None:
            pulumi.set(__self__, "api_version", 'discovery.k8s.io/v1')
        if kind is not None:
            pulumi.set(__self__, "kind", 'EndpointSlice')
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if ports is not None:
            pulumi.set(__self__, "ports", ports)

    @property
    @pulumi.getter(name="addressType")
    def address_type(self) -> pulumi.Input[str]:
        """
        addressType specifies the type of address carried by this EndpointSlice. All addresses in this slice must be the same type. This field is immutable after creation. The following address types are currently supported: * IPv4: Represents an IPv4 Address. * IPv6: Represents an IPv6 Address. * FQDN: Represents a Fully Qualified Domain Name.

        Possible enum values:
         - `"FQDN"` represents a FQDN.
         - `"IPv4"` represents an IPv4 Address.
         - `"IPv6"` represents an IPv6 Address.
        """
        return pulumi.get(self, "address_type")

    @address_type.setter
    def address_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "address_type", value)

    @property
    @pulumi.getter
    def endpoints(self) -> pulumi.Input[Sequence[pulumi.Input['EndpointArgs']]]:
        """
        endpoints is a list of unique endpoints in this slice. Each slice may include a maximum of 1000 endpoints.
        """
        return pulumi.get(self, "endpoints")

    @endpoints.setter
    def endpoints(self, value: pulumi.Input[Sequence[pulumi.Input['EndpointArgs']]]):
        pulumi.set(self, "endpoints", value)

    @property
    @pulumi.getter(name="apiVersion")
    def api_version(self) -> Optional[pulumi.Input[str]]:
        """
        APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources
        """
        return pulumi.get(self, "api_version")

    @api_version.setter
    def api_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "api_version", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def metadata(self) -> Optional[pulumi.Input['_meta.v1.ObjectMetaArgs']]:
        """
        Standard object's metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input['_meta.v1.ObjectMetaArgs']]):
        pulumi.set(self, "metadata", value)

    @property
    @pulumi.getter
    def ports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['EndpointPortArgs']]]]:
        """
        ports specifies the list of network ports exposed by each endpoint in this slice. Each port must have a unique name. When ports is empty, it indicates that there are no defined ports. When a port is defined with a nil port value, it indicates "all ports". Each slice may include a maximum of 100 ports.
        """
        return pulumi.get(self, "ports")

    @ports.setter
    def ports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['EndpointPortArgs']]]]):
        pulumi.set(self, "ports", value)


@pulumi.input_type
class EndpointArgs:
    def __init__(__self__, *,
                 addresses: pulumi.Input[Sequence[pulumi.Input[str]]],
                 conditions: Optional[pulumi.Input['EndpointConditionsArgs']] = None,
                 deprecated_topology: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 hints: Optional[pulumi.Input['EndpointHintsArgs']] = None,
                 hostname: Optional[pulumi.Input[str]] = None,
                 node_name: Optional[pulumi.Input[str]] = None,
                 target_ref: Optional[pulumi.Input['_core.v1.ObjectReferenceArgs']] = None,
                 zone: Optional[pulumi.Input[str]] = None):
        """
        Endpoint represents a single logical "backend" implementing a service.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] addresses: addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100. These are all assumed to be fungible and clients may choose to only use the first element. Refer to: https://issue.k8s.io/106267
        :param pulumi.Input['EndpointConditionsArgs'] conditions: conditions contains information about the current status of the endpoint.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] deprecated_topology: deprecatedTopology contains topology information part of the v1beta1 API. This field is deprecated, and will be removed when the v1beta1 API is removed (no sooner than kubernetes v1.24).  While this field can hold values, it is not writable through the v1 API, and any attempts to write to it will be silently ignored. Topology information can be found in the zone and nodeName fields instead.
        :param pulumi.Input['EndpointHintsArgs'] hints: hints contains information associated with how an endpoint should be consumed.
        :param pulumi.Input[str] hostname: hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must be lowercase and pass DNS Label (RFC 1123) validation.
        :param pulumi.Input[str] node_name: nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node. This field can be enabled with the EndpointSliceNodeName feature gate.
        :param pulumi.Input['_core.v1.ObjectReferenceArgs'] target_ref: targetRef is a reference to a Kubernetes object that represents this endpoint.
        :param pulumi.Input[str] zone: zone is the name of the Zone this endpoint exists in.
        """
        pulumi.set(__self__, "addresses", addresses)
        if conditions is not None:
            pulumi.set(__self__, "conditions", conditions)
        if deprecated_topology is not None:
            pulumi.set(__self__, "deprecated_topology", deprecated_topology)
        if hints is not None:
            pulumi.set(__self__, "hints", hints)
        if hostname is not None:
            pulumi.set(__self__, "hostname", hostname)
        if node_name is not None:
            pulumi.set(__self__, "node_name", node_name)
        if target_ref is not None:
            pulumi.set(__self__, "target_ref", target_ref)
        if zone is not None:
            pulumi.set(__self__, "zone", zone)

    @property
    @pulumi.getter
    def addresses(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        addresses of this endpoint. The contents of this field are interpreted according to the corresponding EndpointSlice addressType field. Consumers must handle different types of addresses in the context of their own capabilities. This must contain at least one address but no more than 100. These are all assumed to be fungible and clients may choose to only use the first element. Refer to: https://issue.k8s.io/106267
        """
        return pulumi.get(self, "addresses")

    @addresses.setter
    def addresses(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "addresses", value)

    @property
    @pulumi.getter
    def conditions(self) -> Optional[pulumi.Input['EndpointConditionsArgs']]:
        """
        conditions contains information about the current status of the endpoint.
        """
        return pulumi.get(self, "conditions")

    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input['EndpointConditionsArgs']]):
        pulumi.set(self, "conditions", value)

    @property
    @pulumi.getter(name="deprecatedTopology")
    def deprecated_topology(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        deprecatedTopology contains topology information part of the v1beta1 API. This field is deprecated, and will be removed when the v1beta1 API is removed (no sooner than kubernetes v1.24).  While this field can hold values, it is not writable through the v1 API, and any attempts to write to it will be silently ignored. Topology information can be found in the zone and nodeName fields instead.
        """
        return pulumi.get(self, "deprecated_topology")

    @deprecated_topology.setter
    def deprecated_topology(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "deprecated_topology", value)

    @property
    @pulumi.getter
    def hints(self) -> Optional[pulumi.Input['EndpointHintsArgs']]:
        """
        hints contains information associated with how an endpoint should be consumed.
        """
        return pulumi.get(self, "hints")

    @hints.setter
    def hints(self, value: Optional[pulumi.Input['EndpointHintsArgs']]):
        pulumi.set(self, "hints", value)

    @property
    @pulumi.getter
    def hostname(self) -> Optional[pulumi.Input[str]]:
        """
        hostname of this endpoint. This field may be used by consumers of endpoints to distinguish endpoints from each other (e.g. in DNS names). Multiple endpoints which use the same hostname should be considered fungible (e.g. multiple A values in DNS). Must be lowercase and pass DNS Label (RFC 1123) validation.
        """
        return pulumi.get(self, "hostname")

    @hostname.setter
    def hostname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname", value)

    @property
    @pulumi.getter(name="nodeName")
    def node_name(self) -> Optional[pulumi.Input[str]]:
        """
        nodeName represents the name of the Node hosting this endpoint. This can be used to determine endpoints local to a Node. This field can be enabled with the EndpointSliceNodeName feature gate.
        """
        return pulumi.get(self, "node_name")

    @node_name.setter
    def node_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "node_name", value)

    @property
    @pulumi.getter(name="targetRef")
    def target_ref(self) -> Optional[pulumi.Input['_core.v1.ObjectReferenceArgs']]:
        """
        targetRef is a reference to a Kubernetes object that represents this endpoint.
        """
        return pulumi.get(self, "target_ref")

    @target_ref.setter
    def target_ref(self, value: Optional[pulumi.Input['_core.v1.ObjectReferenceArgs']]):
        pulumi.set(self, "target_ref", value)

    @property
    @pulumi.getter
    def zone(self) -> Optional[pulumi.Input[str]]:
        """
        zone is the name of the Zone this endpoint exists in.
        """
        return pulumi.get(self, "zone")

    @zone.setter
    def zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "zone", value)


@pulumi.input_type
class ForZoneArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str]):
        """
        ForZone provides information about which zones should consume this endpoint.
        :param pulumi.Input[str] name: name represents the name of the zone.
        """
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        name represents the name of the zone.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)


