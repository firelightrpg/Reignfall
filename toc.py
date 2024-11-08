import re

# Load your markdown content from a file or a string
with open("README.md", encoding="UTF-8") as f:
    markdown_content = f.read()

# Use a regular expression to find only headers that start with "# Session"
headers = re.findall(r"^(# Session \d+ - .+)$", markdown_content, re.MULTILINE)

# Generate a table of contents
toc = []
for header in headers:
    # Clean up the title for the link
    title = header.strip("# ")
    # Convert the title to a GitHub-friendly anchor link
    anchor = re.sub(r"[^\w\s-]", "", title).replace(" ", "-").lower()
    toc.append(f"- [{title}](#{anchor})")

# Join the list to create the final TOC string
toc_content = "\n".join(toc)

print("Table of Contents:")
print(toc_content)
