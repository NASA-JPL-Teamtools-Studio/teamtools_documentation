# Teamtools Studio Utilities

![Project logo](https://github.com/NASA-JPL-Teamtools-Studio/teamtools_documentation/raw/main/docs/images/tts_image_artifacts/tts_utilities.png)

### Overview

Teamtools Studio Utilities is a helper library to improve the quality of life of Teamtools Studio developers. It is
required by all Teamtools Studio libraries in order to support versions of Python back to 3.6 while still using a modern
method of packaging. All TTS libraries include both a pyproject.toml and setup.py file, but only the pyproject.toml is
a source of truth. setup.py only calls a utility from this library to convert the information in the toml file into the
Pythonic format expected by Python versions prior to 3.8.

The most important thing here for most developrs is the common TTS logger.

### Projects Currently Supported

* Europa Clipper
* Mars 2020/Perseverance
* Mars Sample Return/Sample Retrieval Lander
* Mars Science Laboratory/Curiosity
* Mars Reconnaisance Orbiter
* NISAR
* Orbiting Carbon Observatory 2 (OCO-2)

## Architecture

### TTS dependencies

* None

---
**Repository Links:** <a href="https://nasa-jpl-teamtools-studio.github.io/NASA-JPL-Teamtools-Studio/tts_utilities/" target="_blank" rel="noopener noreferrer">Docs</a> | <a href="https://github.com/NASA-JPL-Teamtools-Studio/tts_utilities/issues" target="_blank" rel="noopener noreferrer">Issues</a> | <a href="https://github.com/NASA-JPL-Teamtools-Studio/tts_utilities" target="_blank" rel="noopener noreferrer">Source</a>