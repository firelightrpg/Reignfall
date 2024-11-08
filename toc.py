import re

# Load your markdown content from a file or a string
with open("README.md", encoding="UTF-8") as f:
    markdown_content = f.read()

# Find headers that match the "Session" pattern
headers = re.findall(r"^\s*# (Session \d+ - .+)$", markdown_content, re.MULTILINE)

# Generate a table of contents with <a> links
toc = []
for header in headers:
    title = header.strip()
    # Generate an id-friendly link by removing special characters, replacing spaces, etc.
    anchor_id = re.sub(r"[^\w\s-]", "", title).replace(" ", "-").lower()
    toc.append(f'<a href="#{anchor_id}">{title}</a>')


# Insert custom id anchors directly before each header in the markdown
def insert_anchor(match):
    header_text = match.group(1)
    anchor_id = re.sub(r"[^\w\s-]", "", header_text).replace(" ", "-").lower()
    return f'<a id="{anchor_id}"></a>\n# {header_text}'


content_with_anchors = re.sub(r"^\s*# (Session \d+ - .+)$", insert_anchor, markdown_content, flags=re.MULTILINE)

# Combine TOC and content
toc_content = "\n".join(toc)
final_content = f"## Table of Contents\n{toc_content}\n\n{content_with_anchors}"

print("Generated Markdown Content:")
print(final_content)
