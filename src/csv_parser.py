import csv
from budget_obj import CSVNode
from pathlib import Path

def node_create(file_name):
    current_dir = Path.cwd()
    csv_file = current_dir / "content" / file_name

    csv_nodes = []

    with open(csv_file, "r") as file:
        csv_reader = csv.reader(file)
        next(csv_reader)
        for line in csv_reader:
            csv_nodes.append(CSVNode(line))

    return csv_nodes
