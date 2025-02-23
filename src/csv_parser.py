import csv
from budget_obj import CSVNode
from pathlib import Path

def path_create(file_name: str):
    current_dir = Path.cwd()
    return current_dir / "content" / file_name

def node_create(file_path):
    csv_nodes = []

    with open(file_path, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for line in csv_reader:
            csv_nodes.append(CSVNode(line))

    return csv_nodes
