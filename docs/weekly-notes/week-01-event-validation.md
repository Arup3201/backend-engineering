# Week 01 - Validate webhook event from a file

## Contract

Fields: `external_id`, `event_type` and `payload_byte`

`payload_byte` field is derived from the `payload` field in the data passed to the `parse_event` function in `app/domain/events.py`.

`external_id` is mandatory and should be less than or equal to 128 bytes.

`event_type` is mandatory and should be less than or equal to 100 bytes.

`payload` is a dictionary type in Python and should be less than or equal to 64 KB after serialization.

## Failure Reproduced

## Tests and Decisions

I am testing for the following primary cases:

- Empty `external_id` and `event_type` raise `ValueError` with proper message.
- Payload type validation is working as expected.
- Payload mutation will not change the internal `payload_bytes` field.
- Payload size limit should not exceed 64 KB.
- Event data won't contain any unknown field out of the contract.
- Reordering the payload fields won't change the end payload bytes derived.

To make sure the payload bytes remain same even if the payload fields are reordered, I have used `separators=(',',':')` and `sort_keys=True` arguments. This will make the payload compact and sort the fields based on the key before serializing it into bytes.

## Questions

