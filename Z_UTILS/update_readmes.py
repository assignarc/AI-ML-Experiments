import os
import re
import json
import argparse
import shutil
from pathlib import Path
import nbformat

# Configuration for Section Mapping (Formal -> Casual)
SECTION_MAP = {
    "Objectives": "## What was the goal?",
    "Business Context": "## Why does this matter? (Business Context)",
    "Techs": "## Tech Stack",
    "Packages": "## Stuff I used (Libraries)",
    "Observations": "## What did I notice?",
    "Insights": "## What I Found (Insights)",
    "Learnings": "## What I Learned",
    "Results": "## How did it do? (Results)",
    "Conclusions": "## Wrapping up"
}

ORDER = ["Objectives", "Business Context", "Techs", "Packages", "Observations", "Insights", "Learnings", "Results", "Conclusions"]

ROOT_DIR = Path("/Users/vishalkhapre/Documents/Code/AI-ML-Experiments")

def extract_from_notebook(nb_path):
    """Robustly extracts metadata by tracking context across cells."""
    metadata = {
        "title": "",
        "objectives": "",
        "business_context": "",
        "insights": "",
        "observations": "",
        "techs": set(),
        "packages": set()
    }
    
    try:
        with open(nb_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
            
        current_section = None
        
        for cell in nb.cells:
            if cell.cell_type == 'markdown':
                source = cell.source.strip()
                if not source: continue
                
                # Skip Table of Contents
                if "Table of Contents" in source or "(#" in source:
                    continue
                
                # Handle Headers
                if source.startswith('#'):
                    # Check for Title
                    if source.startswith('# ') and not metadata["title"]:
                        metadata["title"] = source.lstrip('#').split('\n')[0].strip('* ')
                    
                    # Section detection
                    low_source = source.lower()
                    if "objective" in low_source or "goal" in low_source or "problem statement" in low_source:
                        current_section = "objectives"
                    elif "business context" in low_source:
                        current_section = "business_context"
                    elif "insights" in low_source:
                        current_section = "insights"
                    elif "data description" in low_source or "overview" in low_source:
                        current_section = "observations"
                    else:
                        # If it's some other header, stop collecting for the previous section
                        if current_section and not source.startswith('###'): # Allow subheaders within section
                            current_section = None
                            
                    # If there's content in the same cell as the header
                    lines = source.split('\n')
                    if len(lines) > 1 and current_section:
                        content = "\n".join(lines[1:]).strip()
                        if content:
                            metadata[current_section] += content + "\n"
                
                elif current_section:
                    # Append non-header content to the active section
                    metadata[current_section] += source + "\n"

            elif cell.cell_type == 'code':
                # Extract libraries from imports
                imports = re.findall(r'^\s*(?:import|from)\s+([a-zA-Z0-9_]+)', cell.source, re.MULTILINE)
                for imp in imports:
                    if imp not in ['os', 'sys', 're', 'json', 'math', 'time', 'datetime', 'warnings', 'Path', 'abc', 'collections', 'copy', 'functools', 'itertools', 'pickle', 'string', 'threading']:
                        metadata["packages"].add(imp)
                        
        # Clean up strings
        for key in ["objectives", "business_context", "insights", "observations"]:
            metadata[key] = metadata[key].split('\n\n')[0].strip() # Limit to first block or just strip

        tech_map = {
            'pandas': 'Pandas', 'numpy': 'NumPy', 'sklearn': 'Scikit-learn', 'tensorflow': 'TensorFlow', 
            'keras': 'Keras', 'torch': 'PyTorch', 'seaborn': 'Seaborn', 'matplotlib': 'Matplotlib',
            'scipy': 'SciPy', 'statsmodels': 'Statsmodels', 'nltk': 'NLTK', 'spacy': 'spaCy',
            'transformers': 'Transformers', 'cv2': 'OpenCV', 'plotly': 'Plotly', 'pil': 'PIL', 'dill': 'Dill'
        }
        for p in metadata["packages"]:
            low_p = p.lower()
            if low_p in tech_map:
                metadata["techs"].add(tech_map[low_p])
            elif "vkpykit" in low_p:
                metadata["techs"].add("VKPyKit")
            else:
                metadata["techs"].add(p.capitalize())

    except Exception as e:
        print(f"  Warning: Error reading notebook {nb_path}: {e}")
        
    return metadata

def get_folder_metadata(folder_path):
    aggregated = {
        "title": folder_path.name,
        "objectives": "",
        "business_context": "",
        "insights": "",
        "observations": "",
        "techs": set(),
        "packages": set()
    }
    
    nbs = sorted(list(folder_path.glob("*.ipynb")))
    for nb in nbs:
        if ".ipynb_checkpoints" in str(nb): continue
        m = extract_from_notebook(nb)
        if m["title"] and (aggregated["title"] == folder_path.name or not aggregated["title"]):
            aggregated["title"] = m["title"]
        if not aggregated["objectives"]: aggregated["objectives"] = m["objectives"]
        if not aggregated["business_context"]: aggregated["business_context"] = m["business_context"]
        if not aggregated["insights"]: aggregated["insights"] = m["insights"]
        if not aggregated["observations"]: aggregated["observations"] = m["observations"]
        aggregated["techs"].update(m["techs"])
        aggregated["packages"].update(m["packages"])
        
    readme_path = folder_path / "README.md"
    if readme_path.exists():
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
            if not aggregated["objectives"]:
                match = re.search(r'##\s*(?:The Goal|What was the goal\?)\s*\n+(.*?)(?=\n##|$)', content, re.IGNORECASE | re.DOTALL)
                if match: aggregated["objectives"] = match.group(1).strip()
    
    return aggregated

def generate_readme(folder_path, metadata, exercises=None):
    lines = [f"# {metadata['title']}\n"]
    lines.append("> Learning through experiments and data!\n\n")
    
    content_map = {
        "Objectives": metadata["objectives"] or "Placeholder: Describe the goal here.",
        "Business Context": metadata["business_context"] or "Placeholder: Why does this analysis matter for a business?",
        "Techs": ", ".join(sorted(metadata["techs"])) or "Python",
        "Packages": ", ".join(sorted(metadata["packages"])) or "Standard Libraries",
        "Observations": metadata["observations"] or "Placeholder: What interesting things popped up in the data?",
        "Insights": metadata["insights"] or "Placeholder: What did you find out?",
        "Learnings": "Placeholder: What was the biggest takeaway?",
        "Results": "Placeholder: Final model scores or summary.",
        "Conclusions": "Placeholder: Final thoughts."
    }
    
    # Update content from existing README if present
    readme_path = folder_path / "README.md"
    if readme_path.exists():
        with open(readme_path, 'r', encoding='utf-8') as f:
            old_content = f.read()
            for formal, casual in SECTION_MAP.items():
                pattern = re.escape(casual) + r'\s*\n+(.*?)(?=\n##|$)'
                match = re.search(pattern, old_content, re.DOTALL)
                if match:
                    val = match.group(1).strip()
                    if val and "Placeholder" not in val:
                        content_map[formal] = val

    for key in ORDER:
        lines.append(f"{SECTION_MAP[key]}\n")
        lines.append(f"{content_map[key]}\n\n")
        
    if exercises:
        lines.append("## Exercises\n")
        for name, rel_path in exercises.items():
            lines.append(f"- [{name}]({rel_path})\n")
        lines.append("\n")
        
    return "".join(lines)

def process_weeks():
    week_dirs = [d for d in ROOT_DIR.glob("W*") if d.is_dir()]
    def get_sort_key(d):
        num = re.search(r'\d+', d.name)
        return int(num.group()) if num else 999
    week_folders = sorted(week_dirs, key=get_sort_key)
    summaries = []
    for week in week_folders:
        print(f"Processing {week.name}...")
        exercises = {}
        sub_dirs = sorted([d for d in week.iterdir() if d.is_dir() and d.name != ".ipynb_checkpoints"])
        for sub in sub_dirs:
            if list(sub.glob("*.ipynb")) or list(sub.glob("*.py")):
                ex_meta = get_folder_metadata(sub)
                ex_readme = generate_readme(sub, ex_meta)
                write_file(sub / "README.md", ex_readme)
                exercises[ex_meta['title']] = f"./{sub.name}/README.md"
        week_meta = get_folder_metadata(week)
        week_readme = generate_readme(week, week_meta, exercises)
        write_file(week / "README.md", week_readme)
        summaries.append({
            "id": week.name, "title": week_meta['title'], "obj": week_meta['objectives'], "path": f"./{week.name}"
        })
    return summaries

def process_projects():
    project_folders = sorted([f for f in ROOT_DIR.glob("P*") if f.is_dir()])
    summaries = []
    for proj in project_folders:
        print(f"Processing {proj.name}...")
        meta = get_folder_metadata(proj)
        readme = generate_readme(proj, meta)
        write_file(proj / "README.md", readme)
        summaries.append({
            "id": proj.name, "title": meta['title'], "obj": meta['objectives'], "path": f"./{proj.name}"
        })
    return summaries

def write_file(path, content):
    if args.dry_run:
        print(f"  [Dry Run] Would write {path.relative_to(ROOT_DIR)}")
        return
    if args.backup and path.exists():
        backup_path = path.with_suffix(".md.bak")
        shutil.copy(path, backup_path)
    with open(path, 'w', encoding='utf-8') as f:
        f.write(content)

def update_root_readme(projs, weeks):
    print("Updating Root README with Markers...")
    root_path = ROOT_DIR / "README.md"
    if not root_path.exists(): return
    with open(root_path, 'r', encoding='utf-8') as f:
        content = f.read()
    proj_lines = []
    for p in projs:
        proj_lines.append(f"### [{p['title']}]({p['path']})\n")
        proj_lines.append(f"- **ID:** {p['id']}\n")
        if p['obj']:
            obj = p['obj'].split('\n')[0][:200] + "..." if len(p['obj']) > 200 else p['obj']
            proj_lines.append(f"- **Goal:** {obj}\n")
        proj_lines.append(f"- 📖 [Detailed README]({p['path']}/README.md)\n\n")
        proj_lines.append("---\n\n")
    week_lines = []
    for w in weeks:
        week_lines.append(f"### [{w['title']}]({w['path']})\n")
        week_lines.append(f"- **Module:** {w['id']}\n")
        if w['obj']:
            obj = w['obj'].split('\n')[0][:200] + "..." if len(w['obj']) > 200 else w['obj']
            week_lines.append(f"- **Summary:** {obj}\n")
        week_lines.append(f"- 📖 [Module README]({w['path']}/README.md)\n\n")
    def replace_between(full, start_marker, end_marker, new_inner):
        pattern = re.escape(start_marker) + r'.*?' + re.escape(end_marker)
        replacement = f"{start_marker}\n\n" + new_inner + f"\n{end_marker}"
        return re.sub(pattern, replacement, full, flags=re.DOTALL)
    new_content = replace_between(content, "<!-- AUTO_PROJECTS_START -->", "<!-- AUTO_PROJECTS_END -->", "".join(proj_lines))
    new_content = replace_between(new_content, "<!-- AUTO_WEEKS_START -->", "<!-- AUTO_WEEKS_END -->", "".join(week_lines))
    write_file(root_path, new_content)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--backup", action="store_true")
    args = parser.parse_args()
    projs = process_projects()
    weeks = process_weeks()
    update_root_readme(projs, weeks)
    print("All done!")
