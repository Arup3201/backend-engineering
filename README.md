# Setup

In Linux based systems.

> Version: Python >= 3.10

```
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev]'
```

# Validate an event

Event

```json
{"external_id":"invoice-001","event_type":"invoice.paid","payload":{"invoice_id":123}}
```

Validate

```
python -m scripts.validate_event examples/event.json
```

Output

```
external_id: invoice-001
event_type: invoice.paid
payload byte count: 18
0
```

At the end, 0 means success and 2 means failure.


