import os
import re

# Set your working directory (modify if needed)
root_dir = "web"

# Regex to extract href/src values
link_pattern = re.compile(r'(?:href|src)="([^"]+)"')

# Collect all HTML files
html_files = []
for root, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".html"):
            html_files.append(os.path.join(root, file))

missing_links = []

# Scan all HTML files
for html_file in html_files:
    with open(html_file, "r", encoding="utf-8") as f:
        content = f.read()
        matches = link_pattern.findall(content)

        for match in matches:
            # Ignore external links
            if match.startswith("http") or match.startswith("//"):
                continue
            # Resolve relative path
            full_path = os.path.join(os.path.dirname(html_file), match)
            if not os.path.exists(full_path):
                missing_links.append((html_file, match))

# Print results
if missing_links:
    print("❌ Broken Links Found:\n")
    for file, link in missing_links:
        print(f"In {file} → missing: {link}")
else:
    print("✅ All internal links are valid!")
