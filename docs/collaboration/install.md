# Installation

While you are free to install these libraries wherever you want, we find that it is best practice to have a virtual environment scoped to just this work and work that is closely related. That will minimize the number of conflicts you see between TTS libraries and libraries installed in the same environment for other purposes. 

If you work with TTS on multiple projects, it may even be prudent to have a different setup per project. This is especially true if your different projects use different versions of Python.

To initalize a virtual environment:

`python -m venv /path/to/your/venv`

We recommend that you give your virtual environment a descriptive name beyond just `venv`. And if you need to have multiple, it is useful to keep them in the same directory For example:

`python -m venv virtual_environments/demosat_tower_development`.

Beyond that, a simple sourcing of the venv and pip install of each library you would like to use is all that is needed. Note that your exact source command will depend on which shell you are using.

`source /path/to/your/venv/bin/activate`

The library tts_ci_cd offers tools that will help you set up quickly. Begin by installing it in your virtual environment. 

`pip install tts-ci-cd`

It can also be cloned and installed editbaly

`git clone git@github.com:NASA-JPL-Teamtools-Studio/tts_ci_cd.git`
`pip install -e tts_ci_cd`

When installing tts-ci-cd, pip will install several command line tools. In order to have access to their aliases, you should deactivate and reactivate your venv.

The fastest way to get up and running is to run the following command after reactivating:

`tts-demosat-dev-setup --targets demosat_tower --run-tests`

This will clone and install demosat_tower editable along with all of its TTS dependencies and run all of thier unit tests.

Alternatively, this command will clone and install demosat and TTS core libraries editably and run their unit tests. If you would like to only install core libraries, 
you can use tts-dev-setup in a similar way.

`tts-demosat-dev-setup --all --run-tests`


We recommend that each project set up a `[projectname]-tts-dev-steup` in the same way we have for demosat.


# Recommended Conventions

While you do not strictly need to follow our naming conventions, it is strongly recommended for an efficient workflow. Also, if you
are developing within JPL, this will make your mission more robust against staffing attrition as other projects have ostensibly done it this
way and you will have a build in cadre of developers who already know the look and feel of your work.

We recommend that your project has a github organization called `[projectname]-core-teamtools` (e.g. `nisar-core-teamtools` that has only these repositories in it. Each
repository should be named as described above: `[your_mission]\_[lib_to_adapt]` (e.g. `nisar_seq`). This will keep it clear which core libraries are
related to your adaptation libraries.


---
<a href="https://github.com/NASA-JPL-Teamtools-Studio/teamtools-documentation/blob/main/docs/collaboration/install.md" target="_blank" rel="noopener noreferrer">Edit/Comment on GitHub</a>