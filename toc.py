import re

# Load your markdown content from the README file
with open("README.md", encoding="UTF-8") as f:
    markdown_content = f.read()

# Find headers that match the "Session" pattern
headers = re.findall(r"^\s*# (Session \d+ - .+)$", markdown_content, re.MULTILINE)

# Generate a table of contents with GitHub-compatible links
toc = []
for header in headers:
    title = header.strip()
    # GitHub-compatible anchor: lowercase, replace spaces with hyphens, remove special characters and underscores
    anchor = title.lower().replace(" ", "-")
    anchor = re.sub(r"[^\w-]", "", anchor).replace("_", "")  # Remove any special characters and underscores
    toc.append(f"- [{title}](#{anchor})")

# Combine TOC and original content
toc_content = "\n".join(toc)
final_content = f"## Table of Contents\n{toc_content}\n\n{markdown_content}"

# Output the final content to README.md
with open("README.md", "w", encoding="UTF-8") as f:
    f.write(final_content)

print("Generated and saved Markdown Content with updated Table of Contents.")
