#!/usr/bin/env python3
"""
add_github_links.py - Add GitHub edit links to markdown files

This script adds a link at the bottom of each non-repository markdown file that points to the 
corresponding file in the GitHub repository. This makes it easy for users to edit
or comment on the documentation.

Usage:
    python add_github_links.py --docs-dir docs --repo-url "https://github.jpl.nasa.gov/teamtools-studio/teamtools-documentation" --branch main

Options:
    --docs-dir: Path to the docs directory (default: docs)
    --repo-url: URL of the GitHub repository (default: https://github.jpl.nasa.gov/teamtools-studio/teamtools-documentation)
    --branch: Branch name (default: main)

Note:
    - This script skips files in the repositories directory (these are handled by readme_collector.py)
    - If a file already has an edit link, it will be updated with the latest version
"""

import os
import re
from pathlib import Path
import argparse

def add_github_link(file_path, repo_url, branch="main", docs_dir="docs"):
    """
    Add a GitHub edit link to the bottom of a markdown file.
    
    Args:
        file_path (str): Path to the markdown file
        repo_url (str): URL of the GitHub repository
        branch (str): Branch name
        docs_dir (str): Directory containing the docs
    """
    # Skip repository pages (they're in the repositories directory)
    if '/repositories/' in file_path:
        print(f"Skipping repository page: {file_path}")
        return
        
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # For the GitHub URL, we just want the path relative to the docs directory
    # This ensures we don't include the full local path in the URL
    docs_dir_name = os.path.basename(docs_dir)
    rel_path = os.path.join(docs_dir_name, os.path.relpath(file_path, docs_dir))
    
    # Construct the path to the file in the GitHub repository
    edit_url = f"{repo_url}/blob/{branch}/{rel_path}"
    
    # Create the GitHub link
    github_link = f"\n\n---\n<a href=\"{edit_url}\" target=\"_blank\" rel=\"noopener noreferrer\">Edit/Comment on GitHub</a>"
    
    # Check if the file already has an edit link section
    if "---\n<a href=\"" in content or "---\n**Edit" in content:
        # Remove existing edit link section
        pattern = r"\n\n---\n.*?GitHub</a>"
        new_content = re.sub(pattern, "", content, flags=re.DOTALL)
        # Add the new link
        new_content += github_link
        print(f"Updated GitHub link in {file_path}")
    else:
        # Add the link to the content
        new_content = content + github_link
        print(f"Added GitHub link to {file_path}")
    
    # Write the content back to the file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)

def process_directory(docs_dir, repo_url, branch="main"):
    """
    Process all markdown files in the docs directory and add GitHub edit links.
    
    Args:
        docs_dir (str): Path to the docs directory
        repo_url (str): URL of the GitHub repository
        branch (str): Branch name
    """
    # Walk through the docs directory
    for root, _, files in os.walk(docs_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                add_github_link(file_path, repo_url, branch, docs_dir)

def main():
    """Main function to add GitHub edit links to markdown files."""
    parser = argparse.ArgumentParser(description='Add GitHub edit links to markdown files.')
    parser.add_argument('--docs-dir', default='docs', help='Path to the docs directory')
    parser.add_argument('--repo-url', default='https://github.jpl.nasa.gov/teamtools-studio/teamtools-documentation', 
                        help='URL of the GitHub repository')
    parser.add_argument('--branch', default='main', help='Branch name')
    
    args = parser.parse_args()
    
    # Get the absolute path to the docs directory
    docs_dir = os.path.abspath(args.docs_dir)
    
    print(f"Adding GitHub edit links to markdown files in {docs_dir}")
    print(f"Repository URL: {args.repo_url}")
    print(f"Branch: {args.branch}")
    
    process_directory(docs_dir, args.repo_url, args.branch)
    
    print("Done!")

if __name__ == "__main__":
    main()
