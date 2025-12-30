# exporters/json_exporter.py

import json

def export_json(records, output_path):
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(records, f, indent=2, ensure_ascii=False)
