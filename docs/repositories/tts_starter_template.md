# tts_starter_template
A starter repository to help users quickly set up a Teamtools Studio project with common structure, configs, and package scaffolding. 

![Project logo](https://github.com/NASA-JPL-Teamtools-Studio/teamtools_documentation/raw/main/docs/images/tts_image_artifacts/tts_starter_template.png)

### Overview

This is a simple starter kit for new repositories to help enforce consistent style and packaging conventions common to all TTS libraries.
It is important to follow these conventions as much of our CI/CD is built around assumptions about how these libraries are built.

* Notice that we use pyproject.toml with a simple helper setup.py to bootstrap older Python versions
* Notice that we deploy tests within src/library. This is so we can call them via pytest --pyargs [mylib]

## Making Your Own Repository From This Template

This is a "template" GitHub repository, which makes it much simpler to copy without needing to for example manage a fork.

If you are a member of this GitHub organization, this repository should show up under the templates avaliable to you
when creating a new repository normally.

### TTS dependencies

* TTS Utilities

---
**Repository Links:** <a href="nasa-jpl-teamtools-studio.github.io/NASA-JPL-Teamtools-Studio/tts_starter_template/" target="_blank" rel="noopener noreferrer">Docs</a> | <a href="github.com/NASA-JPL-Teamtools-Studio/tts_starter_template/issues" target="_blank" rel="noopener noreferrer">Issues</a> | <a href="github.com/NASA-JPL-Teamtools-Studio/tts_starter_template" target="_blank" rel="noopener noreferrer">Source</a>