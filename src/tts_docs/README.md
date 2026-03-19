# Teamtools Documentation Utilities

This directory contains utilities for managing the Teamtools Studio documentation.

## Scripts

### readme_collector.py

This script collects README files from various repositories and processes them for inclusion in the documentation.

### add_github_links.py

This script adds GitHub edit links to the bottom of each non-repository markdown file in the docs directory. This makes it easy for users to edit or comment on the documentation.

#### Usage

```bash
python src/tts_docs/add_github_links.py --docs-dir docs --repo-url "https://github.jpl.nasa.gov/teamtools-studio/teamtools-documentation" --branch main
```

#### Options

- `--docs-dir`: Path to the docs directory (default: docs)
- `--repo-url`: URL of the GitHub repository (default: https://github.jpl.nasa.gov/teamtools-studio/teamtools-documentation)
- `--branch`: Branch name (default: main)

#### How it works

The script adds a link at the bottom of each non-repository markdown file that points to the corresponding file in the GitHub repository. This makes it easy for users to edit or comment on the documentation.

- Repository pages (in the repositories directory) are skipped as they are handled by readme_collector.py
- If a file already has an edit link, it will be updated with the latest version

#### Example output

At the bottom of each page, the script adds a link like this:

```markdown
---
<a href="https://github.jpl.nasa.gov/teamtools-studio/teamtools-documentation/blob/main/docs/index.md" target="_blank" rel="noopener noreferrer">Edit/comment on GitHub</a>
```
