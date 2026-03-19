import os
import subprocess
import shutil
import re
from pathlib import Path

# List of your repositories
REPOS = [
    {"url": "git@github.com:NASA-JPL-Teamtools-Studio/tts_utilities.git", "name": "tts_utilities"},
    {"url": "git@github.com:NASA-JPL-Teamtools-Studio/tts_starter_template.git", "name": "tts_starter_template"},
    {"url": "git@github.com:NASA-JPL-Teamtools-Studio/tts_html_utils.git", "name": "tts_html_utils"},
    {"url": "git@github.com:NASA-JPL-Teamtools-Studio/tts_data_utils.git", "name": "tts_data_utils"},
    {"url": "git@github.com:NASA-JPL-Teamtools-Studio/tts_dtat.git", "name": "tts_dtat"},
    {"url": "git@github.com:NASA-JPL-Teamtools-Studio/tts_papertrail.git", "name": "tts_papertrail"},
    {"url": "git@github.com:NASA-JPL-Teamtools-Studio/tts_dictionary_interface.git", "name": "tts_dictionary_interface"},
    {"url": "git@github.com:NASA-JPL-Teamtools-Studio/tts_seq.git", "name": "tts_seq"},
    {"url": "git@github.com:NASA-JPL-Teamtools-Studio/tts_fresh.git", "name": "tts_fresh"},
    {"url": "git@github.com:NASA-JPL-Teamtools-Studio/tts_tower.git", "name": "tts_tower"},
    {"url": "git@github.com:NASA-JPL-Teamtools-Studio/tts_dexter.git", "name": "tts_dexter"},
    {"url": "git@github.com:NASA-JPL-Teamtools-Studio/tts_dante.git", "name": "tts_dante"},
    {"url": "git@github.com:NASA-JPL-Teamtools-Studio/tts_plan.git", "name": "tts_plan"},
    {"url": "git@github.com:NASA-JPL-Teamtools-Studio/tts_spice.git", "name": "tts_spice"}
]

def process_markdown(content):
    # --- FIX: Convert GitHub 'blob' links to 'raw' ---
    content = content.replace('/blob/', '/raw/')

    lines = content.splitlines()
    output = []
    skipping = False
    
    STRIP_SECTIONS = ["About Teamtools Studio", "For More Information"]

    # Check if the content already has a GitHub link section
    has_repo_links = "**Repository Links:**" in content

    for line in lines:
        header_match = re.match(r'^(#+)\s+(.*)', line)
        
        if header_match:
            header_text = header_match.group(2)
            
            is_banned = any(section.lower() in header_text.lower() for section in STRIP_SECTIONS)
            is_what_is = bool(re.match(r'^What is.*?\?', header_text, re.IGNORECASE))

            if is_banned or is_what_is:
                skipping = True
                continue
            else:
                skipping = False
        
        if not skipping:
            output.append(line)
            
    return "\n".join(output)

def generate_repo_links(ssh_url):
    """
    Converts git@github... SSH URL to browser-friendly URLs.
    """
    # 1. Convert 'git@' to 'https://' and remove '.git'
    base_url = ssh_url.replace("git@", "https://").replace(".git", "")
    
    # 2. Fix the colon (github.com:org -> github.com/org)
    if "github.com:" in base_url:
        base_url = base_url.replace("github.com:", "github.com/")
    
    # 3. Construct Pages URL
    # We do NOT force .lower() here anymore. We rely on the input list casing.
    # If your org is CamelCase in the URL, ensure REPOS list matches.
    pages_url = base_url.replace("github.com/", "nasa-jpl-teamtools-studio.github.io/")
    
    # Ensure trailing slash to prevent GHE directory redirect loops/404s
    if not pages_url.endswith('/'):
        pages_url += '/'
    
    return {
        "root": base_url,
        "issues": f"{base_url}/issues",
        "site": pages_url
    }

def main():
    docs_dir = Path(__file__).parent.parent.parent.joinpath('docs/repositories')
    if not os.path.exists(docs_dir):
        os.makedirs(docs_dir)

    for repo in REPOS:
        temp_dir = f"/tmp/{repo['name']}"
        print(f"--- Processing {repo['name']} ---")
        
        try:
            # 1. Shallow clone
            subprocess.run(["git", "clone", "--depth", "1", repo['url'], temp_dir], check=True)
            
            readme_path = os.path.join(temp_dir, "README.md")
            if os.path.exists(readme_path):
                with open(readme_path, 'r') as f:
                    content = f.read()
                
                # 2. Clean content
                cleaned_content = process_markdown(content)

                # 3. Generate and Append Footer Links
                links = generate_repo_links(repo['url'])
                
                # Using HTML <a> tags with rel="noopener noreferrer"
                # This forces the browser to treat the click as a fresh navigation
                # (similar to typing in the address bar), bypassing referrer-based 
                # blocking or caching glitches common in Brave/GHE.
                footer = (
                    f"\n\n---\n"
                    f"**Repository Links:** "
                    f'<a href="{links["site"]}" target="_blank" rel="noopener noreferrer">Docs</a> | '
                    f'<a href="{links["issues"]}" target="_blank" rel="noopener noreferrer">Issues</a> | '
                    f'<a href="{links["root"]}" target="_blank" rel="noopener noreferrer">Source</a>'
                )
                cleaned_content += footer
                
                # 4. Save to meta-repo
                target_path = os.path.join(docs_dir, f"{repo['name']}.md")
                with open(target_path, 'w') as f:
                    f.write(cleaned_content)
                print(f"Saved cleaned README to {target_path}")
            
        except subprocess.CalledProcessError as e:
            print(f"Error processing {repo['name']}: {e}")
        finally:
            if os.path.exists(temp_dir):
                shutil.rmtree(temp_dir)

if __name__ == "__main__":
    main()