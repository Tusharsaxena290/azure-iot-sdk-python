# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Twin(Model):
    """Twin Representation.

    :param device_id: The deviceId uniquely identifies the device in the IoT
     hub's identity registry. A case-sensitive string (up to 128 char long) of
     ASCII 7-bit alphanumeric chars + {'-', ':', '.', '+', '%', '_', '#', '*',
     '?', '!', '(', ')', ',', '=', '@', ';', '$', '''}.
    :type device_id: str
    :param module_id: Gets and sets the Module Id.
    :type module_id: str
    :param tags: A JSON document read and written by the solution back end.
     Tags are not visible to device apps.
    :type tags: dict[str, object]
    :param properties: Gets and sets the Twin properties.
    :type properties: ~protocol.models.TwinProperties
    :param etag: Twin's ETag
    :type etag: str
    :param version: Version for device twin, including tags and desired
     properties
    :type version: long
    :param device_etag: Device's ETag
    :type device_etag: str
    :param status: Gets the corresponding Device's Status. Possible values
     include: 'enabled', 'disabled'
    :type status: str or ~protocol.models.enum
    :param status_reason: Reason, if any, for the corresponding Device to be
     in specified Status
    :type status_reason: str
    :param status_update_time: Time when the corresponding Device's Status was
     last updated
    :type status_update_time: datetime
    :param connection_state: Corresponding Device's ConnectionState. Possible
     values include: 'Disconnected', 'Connected'
    :type connection_state: str or ~protocol.models.enum
    :param last_activity_time: The last time the device connected, received or
     sent a message. In ISO8601 datetime format in UTC, for example,
     2015-01-28T16:24:48.789Z. This does not update if the device uses the
     HTTP/1 protocol to perform messaging operations.
    :type last_activity_time: datetime
    :param cloud_to_device_message_count: Number of messages sent to the
     corresponding Device from the Cloud
    :type cloud_to_device_message_count: int
    :param authentication_type: Corresponding Device's authentication type.
     Possible values include: 'sas', 'selfSigned', 'certificateAuthority',
     'none'
    :type authentication_type: str or ~protocol.models.enum
    :param x509_thumbprint: Corresponding Device's X509 thumbprint
    :type x509_thumbprint: ~protocol.models.X509Thumbprint
    :param capabilities:
    :type capabilities: ~protocol.models.DeviceCapabilities
    :param device_scope:
    :type device_scope: str
    """

    _attribute_map = {
        "device_id": {"key": "deviceId", "type": "str"},
        "module_id": {"key": "moduleId", "type": "str"},
        "tags": {"key": "tags", "type": "{object}"},
        "properties": {"key": "properties", "type": "TwinProperties"},
        "etag": {"key": "etag", "type": "str"},
        "version": {"key": "version", "type": "long"},
        "device_etag": {"key": "deviceEtag", "type": "str"},
        "status": {"key": "status", "type": "str"},
        "status_reason": {"key": "statusReason", "type": "str"},
        "status_update_time": {"key": "statusUpdateTime", "type": "iso-8601"},
        "connection_state": {"key": "connectionState", "type": "str"},
        "last_activity_time": {"key": "lastActivityTime", "type": "iso-8601"},
        "cloud_to_device_message_count": {"key": "cloudToDeviceMessageCount", "type": "int"},
        "authentication_type": {"key": "authenticationType", "type": "str"},
        "x509_thumbprint": {"key": "x509Thumbprint", "type": "X509Thumbprint"},
        "capabilities": {"key": "capabilities", "type": "DeviceCapabilities"},
        "device_scope": {"key": "deviceScope", "type": "str"},
    }

    def __init__(self, **kwargs):
        super(Twin, self).__init__(**kwargs)
        self.device_id = kwargs.get("device_id", None)
        self.module_id = kwargs.get("module_id", None)
        self.tags = kwargs.get("tags", None)
        self.properties = kwargs.get("properties", None)
        self.etag = kwargs.get("etag", None)
        self.version = kwargs.get("version", None)
        self.device_etag = kwargs.get("device_etag", None)
        self.status = kwargs.get("status", None)
        self.status_reason = kwargs.get("status_reason", None)
        self.status_update_time = kwargs.get("status_update_time", None)
        self.connection_state = kwargs.get("connection_state", None)
        self.last_activity_time = kwargs.get("last_activity_time", None)
        self.cloud_to_device_message_count = kwargs.get("cloud_to_device_message_count", None)
        self.authentication_type = kwargs.get("authentication_type", None)
        self.x509_thumbprint = kwargs.get("x509_thumbprint", None)
        self.capabilities = kwargs.get("capabilities", None)
        self.device_scope = kwargs.get("device_scope", None)
