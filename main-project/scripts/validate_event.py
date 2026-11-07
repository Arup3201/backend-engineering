import json
import sys

from app.domain.events import parse_event


def main(argv=None) -> int:
    if not argv:
        return 2
    
    file_path = argv[1]
    if not file_path.endswith(".json"):
        return 2

    json_text = ""
    with open(file_path, "r") as file:
        json_text = file.read()

    event = json.loads(json_text)
    event_input = parse_event(event)
    print(f"external_id: {event_input.external_id}")
    print(f"event_type: {event_input.event_type}")
    print(f"payload byte count: {len(event_input.payload_bytes)}")
    return 0

if __name__=="__main__":
    if len(sys.argv) < 2:
        print("Missing one argument: python -m scripts.validate_event event.json")
        sys.exit(1)
    
    print(main(sys.argv))