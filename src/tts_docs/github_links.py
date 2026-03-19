import os
from pathlib import Path
from mkdocs.plugins import BasePlugin
from mkdocs.config import config_options

class GitHubLinksPlugin(BasePlugin):
    """
    MkDocs plugin that adds a link to the GitHub source file at the bottom of each page.
    """
    
    config_scheme = (
        ('repo_url', config_options.Type(str, required=True)),
        ('repo_name', config_options.Type(str, default='GitHub')),
        ('branch', config_options.Type(str, default='main')),
        ('docs_dir', config_options.Type(str, default='docs')),
    )
    
    def on_page_markdown(self, markdown, page, config, files):
        """
        Add GitHub edit link to the bottom of each markdown page.
        """
        # Skip if the page already has repository links
        if "**Repository Links:**" in markdown:
            return markdown
        
        # Get the relative path to the markdown file
        site_dir = config.get('site_dir', 'site')
        docs_dir = self.config.get('docs_dir', 'docs')
        repo_url = self.config.get('repo_url')
        branch = self.config.get('branch', 'main')
        
        # Construct the path to the file in the GitHub repository
        file_path = page.file.src_path
        edit_url = f"{repo_url}/blob/{branch}/{docs_dir}/{file_path}"
        
        # Add the link at the bottom of the page
        github_link = f"\n\n---\n**Edit this page:** <a href=\"{edit_url}\" target=\"_blank\" rel=\"noopener noreferrer\">Edit on GitHub</a>"
        
        return markdown + github_link
