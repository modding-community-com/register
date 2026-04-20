import json
import os
import sys
import glob

def validate_domains():
    folder = "domains/"
    files = glob.glob(f"{folder}/*.json")
    
    subdomains = {}
    targets = {}
    errors = []

    for file_path in files:
        filename = os.path.basename(file_path).lower()
        
        try:
            with open(file_path, 'r') as f:
                data = json.load(f)
        except json.JSONDecodeError:
            errors.append(f"❌ {file_path}: Invalid JSON format.")
            continue

        subdomain = data.get("subdomain", "").lower()
        target = data.get("target", "").lower()

        if f"{subdomain}.json" != filename:
            errors.append(f"❌ {file_path}: Subdomain '{subdomain}' must match filename '{filename}'.")

        if subdomain in subdomains:
            errors.append(f"❌ Duplicate Subdomain: '{subdomain}' found in {file_path} and {subdomains[subdomain]}.")
        else:
            subdomains[subdomain] = file_path

        if target in targets:
            errors.append(f"❌ Duplicate Target: '{target}' found in {file_path} and {targets[target]}.")
        else:
            targets[target] = file_path

    if errors:
        print("\n".join(errors))
        sys.exit(1)
    else:
        print("✅ All domain files are valid and unique!")
        sys.exit(0)

if __name__ == "__main__":
    validate_domains()