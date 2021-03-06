# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from .provisioned_resource_properties import ProvisionedResourceProperties


class NetworkResourcePropertiesBase(ProvisionedResourceProperties):
    """This type describes the properties of a network resource, including its
    kind.

    You probably want to use the sub-classes and not this class directly. Known
    sub-classes are: NetworkResourceProperties

    Variables are only populated by the server, and will be ignored when
    sending a request.

    :ivar provisioning_state: State of the resource.
    :vartype provisioning_state: str
    :param kind: Constant filled by server.
    :type kind: str
    """

    _validation = {
        'provisioning_state': {'readonly': True},
        'kind': {'required': True},
    }

    _attribute_map = {
        'provisioning_state': {'key': 'provisioningState', 'type': 'str'},
        'kind': {'key': 'kind', 'type': 'str'},
    }

    _subtype_map = {
        'kind': {'NetworkResourceProperties': 'NetworkResourceProperties'}
    }

    def __init__(self):
        super(NetworkResourcePropertiesBase, self).__init__()
        self.kind = None
        self.kind = 'NetworkResourcePropertiesBase'
