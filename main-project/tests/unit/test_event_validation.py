import pytest
from app.domain.events import parse_event


def test_empty_identifier():
    event = {
        "external_id": "", 
        "event_type": "invoice.paid",
        "payload": {"invoice_id":123}
    }
    with pytest.raises(ValueError) as excinfo:
        parse_event(event)

    assert "external_id can't be empty" in str(excinfo.value)

def test_identifier_with():
    event = {
        "external_id": "too-long-external-id"*7, 
        "event_type": "invoice.paid",
        "payload": {"invoice_id":123}
    }
    with pytest.raises(ValueError) as excinfo:
        parse_event(event)

    assert "external_id is more than 128 length" in str(excinfo.value)

def test_list_payload():
    event = {
        "external_id": "invoice-01", 
        "event_type": "invoice.paid",
        "payload": ["invoice_id", 123]
    }
    with pytest.raises(TypeError) as excinfo:
        parse_event(event)

    assert "payload needs to be a dictionary" in str(excinfo.value)

def test_unknown_field():
    event = {
        "external_id": "invoice-01", 
        "event_type": "invoice.paid",
        "extra": 123, 
        "payload": {"invoice_id":123}
    }
    with pytest.raises(ValueError) as excinfo:
        parse_event(event)

    assert "unknown keys are not allowed in the data dictionary" in str(excinfo.value)

def test_caller_mutation():
    event = {
        "external_id": "invoice-01", 
        "event_type": "invoice.paid",
        "payload": {"invoice_id":123,"price":100}
    }
    event_input = parse_event(event)
    payload_bytes_before = event_input.payload_bytes

    event["payload"]["price"] = 200
    payload_bytes_after = event_input.payload_bytes

    assert payload_bytes_before == payload_bytes_after
