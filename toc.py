import re

# Load your markdown content from a file or a string
with open("README.md", encoding="UTF-8") as f:
    markdown_content = f.read()

# Find headers that match the "Session" pattern
headers = re.findall(r"^\s*# (Session \d+ - .+)$", markdown_content, re.MULTILINE)

# Generate a table of contents with GitHub-compatible links
toc = []
for header in headers:
    title = header.strip()
    # Generate GitHub-compatible anchor by lowercasing and replacing spaces and special characters
    anchor = title.lower().replace(" ", "-")
    anchor = re.sub(r"[^\w-]", "", anchor)  # Remove any special characters
    toc.append(f"- [{title}](#{anchor})")

# Combine TOC and original content
toc_content = "\n".join(toc)
final_content = f"## Table of Contents\n{toc_content}\n\n{markdown_content}"

print("Generated Markdown Content:")

with open("README.md", "w", encoding="UTF-8") as f:
    f.write(final_content)
