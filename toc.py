import re

# Load your markdown content from a file or a string
with open("README.md", encoding="UTF-8") as f:
    markdown_content = f.read()

# Regular expression to match headers that start with "Session" and to ensure no preceding whitespace.
headers = re.findall(r"^\s*# (Session \d+ - .+)$", markdown_content, re.MULTILINE)

# Generate a table of contents
toc = []
for header in headers:
    title = header.strip()  # Remove any extra whitespace
    # Generate the GitHub-friendly link
    anchor = re.sub(r"[^\w\s-]", "", title).replace(" ", "-").lower()
    toc.append(f"- [{title}](#{anchor})")

# Join the list to create the final TOC string
toc_content = "\n".join(toc)

print("Table of Contents:")
print(toc_content)
