# exporters/csv_exporter.py

import csv

def flatten(record, parent_key="", sep="."):
    items = {}
    for k, v in record.items():
        new_key = f"{parent_key}{sep}{k}" if parent_key else k
        if isinstance(v, dict):
            items.update(flatten(v, new_key, sep=sep))
        elif isinstance(v, list):
            items[new_key] = ",".join(map(str, v))
        else:
            items[new_key] = v
    return items


def export_csv(records, output_path):
    flat_records = [flatten(r) for r in records]
    fieldnames = sorted({k for r in flat_records for k in r})

    with open(output_path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(flat_records)
