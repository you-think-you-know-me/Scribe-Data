import os
import shutil

CONTRACTS_DIR = "src/scribe_data/wikidata/data-contracts"


def export_contracts(output_dir):
    """Exports contract JSON files to a specified directory."""
    os.makedirs(output_dir, exist_ok=True)

    for contract_file in os.listdir(CONTRACTS_DIR):
        if contract_file.endswith(".json"):
            source_path = os.path.join(CONTRACTS_DIR, contract_file)
            destination_path = os.path.join(output_dir, contract_file)
            shutil.copy(source_path, destination_path)
            print(f"Exported {contract_file} to {output_dir}")
    print(f"Exported all data-contracts to {output_dir}")
