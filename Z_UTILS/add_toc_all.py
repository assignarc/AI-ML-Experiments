import json
import re
import os
from pathlib import Path

def generate_toc_cell(nb):
    toc_lines = ["## Table of Contents", ""]
    for cell in nb.get("cells", []):
        if cell.get("cell_type") == "markdown":
            for line in cell.get("source", []):
                line = line.strip()
                if line.startswith("#"):
                    # Count leading '#'
                    level = len(line) - len(line.lstrip('#'))
                    title = line[level:].strip()
                    if title.lower() == "table of contents":
                        continue
                    # Anchor generation for jupyter
                    anchor = re.sub(r'[^a-zA-Z0-9 -]', '', title).strip().replace(' ', '-').lower()
                    indent = "  " * max(0, level - 2)
                    toc_lines.append(f"{indent}- [{title}](#{anchor})")

    if len(toc_lines) <= 2:
        return None  # No headers found

    source = [line + "\n" for line in toc_lines[:-1]] + [toc_lines[-1]]
    
    return {
        "cell_type": "markdown",
        "metadata": {"id": "table-of-contents"},
        "source": source
    }

def process_notebook(filepath):
    print(f"Processing {filepath}...")
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            nb = json.load(f)
    except Exception as e:
        print(f"  Error reading {filepath}: {e}")
        return

    if "cells" not in nb:
        return

    toc_cell = generate_toc_cell(nb)
    if not toc_cell:
        print("  No headers found, skipping.")
        return

    existing_toc_idx = -1
    problem_statement_idx = -1
    
    for i, cell in enumerate(nb["cells"]):
        if cell.get("cell_type") == "markdown":
            text = "".join(cell.get("source", []))
            if "## Table of Contents" in text:
                existing_toc_idx = i
            # Look for Problem Statement or a suitable insertion point
            if "Problem Statement" in text and problem_statement_idx == -1:
                problem_statement_idx = i

    modified = False
    if existing_toc_idx != -1:
        # Check if identical
        old_source = "".join(nb["cells"][existing_toc_idx].get("source", []))
        new_source = "".join(toc_cell["source"])
        if old_source != new_source:
            nb["cells"][existing_toc_idx] = toc_cell
            modified = True
            print("  Updated existing ToC.")
        else:
            print("  ToC is already up-to-date.")
    else:
        # Insert ToC
        # Default to after first cell or 0 if no Problem Statement exists
        insert_idx = problem_statement_idx
        if insert_idx == -1:
             insert_idx = 1 if len(nb["cells"]) > 0 else 0
        
        nb["cells"].insert(insert_idx, toc_cell)
        modified = True
        print(f"  Inserted ToC at cell index {insert_idx}.")

    if modified:
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(nb, f, indent=2, ensure_ascii=False)
        print("  Saved modified notebook.")

def main():
    repo_dir = Path("/Users/vishalkhapre/Documents/Code/AI-ML-Experiments")
    for path in repo_dir.rglob("*.ipynb"):
        parts = path.parts
        if ".ipynb_checkpoints" in parts or ".venv" in parts or "venv" in parts or ".venv-metal" in parts:
            continue
        process_notebook(path)

if __name__ == "__main__":
    main()
