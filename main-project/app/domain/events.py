import json
from dataclasses import dataclass


@dataclass
class EventInput:
    external_id: str
    event_type: str
    payload_bytes: bytes

    @property
    def payload(self):
        return json.loads(self.payload_bytes)

def parse_event(data: dict) -> EventInput:
    external_id = data.get("external_id")
    event_type = data.get("event_type")
    if not external_id:
        raise ValueError("external_id can't be empty")
    if not event_type:
        raise ValueError("event_type can't be empty")

    if len(external_id)>128:
        raise ValueError("external_id is more than 128 length")
    if len(event_type)>100:
        raise ValueError("event_type is more than 100 length")

    allowed_keys = ["external_id", "event_type", "payload"]
    if len(data.keys()) != len(allowed_keys):
        raise ValueError("unknown keys are not allowed in the data dictionary")

    payload = data.get("payload")
    if not isinstance(payload, dict):
        raise TypeError("payload needs to be a dictionary")

    return EventInput(
        external_id=external_id,
        event_type=event_type,
        payload_bytes=canonical_payload(payload)
    )

def canonical_payload(payload) -> bytes:
    return json.dumps(
        payload, 
        sort_keys=True, 
        separators=(',', ':')
    ).encode("UTF-8")
