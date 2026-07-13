# Day Zero Teamtools System Design

Along with the libraries delivered by the Teamtools Studio, we also maintain this document on best practices and a "day zero" reference design for the Teamtools system. As a reminder, we expect that these libraries will not constitute the full stack of your mission's ground software, but will instead be deployed alongside a GDS that fulfills the majority of your ground tooling needs.

This document includes best practices for organizing your GitHub repositories, setting up your initial codebase, and structuring your mission-specific adaptations of the Teamtools libraries.

## A word on long-term team dynamics

Typical missions at JPL start with a relatively modest number of engineers to begin designing the system and writing requirements, expand as designs become more mature and are implemented, and peak in size at launch or landing. As development completes (some is typically deferred past the beginning of prime mission), team members start to roll off, and the project then continues to shrink forever, especially as it goes into extended operations and sustainment.

Throughout this expansion and contraction, new teams will form, develop their own cultures, and eventually deliver their part of the system to someone else who will then operate and eventually retire the system. As the specifics will be different from project to project, the Teamtools system cannot be designed perfectly a priori. Instead, it must be designed to be flexible and to understand the fact that responsibility of its constituent parts will pass from person to person and team to team. There is no guarantee that any one author of a tool will ever talk to, let alone even know those who own it in the future, nor can it be guaranteed that any one engineer will continue to work on the project, work at JPL or even still be alive by the time the project is finally decommissioned.

## The Systems Teamtools Lead

As JPL mission Teamtools implementations have expanded and become more complex, most projects eventually begin to recognize that there is a critical mass of engineering complexity within the Teamtools developed by the project. As such, many missions have decided to staff roles specifically to manage this complexity. This includes

- Mars 2020 Engineering Operations Uplink Teamtools Lead
- Mars 2020 Engineering Operations Downlink Teamtools Lead
- Mars 2020 Robotic Operations Teamtools Lead
- Europa Clipper Spacecraft Team Teamtools Lead
- Sample Retrieval Lander Systems Teamtools Lead

Starting on Sample Retrieval Lander, the Teamtools Lead role began to be identified as one that typically is added too late, only after many ships have sailed and much unnecessary complexity has been added to the system. For this reason, the SRL Mission System Team scoped a Systems Teamtools Lead role to begin as early as early Phase C.

The Systems Teamtools Lead should be a teamtools practitioner themselves, which is to say they should NOT be from GDS (or at least not solely). Instead they should be a boots-on-the-ground operator. Depending on the phase of the project, this might mean they are a Testbed, ATLO or Flight Operations engineer. But the ethos of the Teamtools studio is that operators are better at solving some subset of software problems due to their proximity to the technical challenges, risks, and operational cadence of doing the work directly.

The specific responsibilities of the Systems Teamtools Lead will vary project to project, but they should include

- Maintaining the systems virtual environment (see below)
- Being a primary contact with the GDS, delivering system-wide impacts on things like upgrading operating systems and Python versions
- Holding a Teamtools Working Group to educate and communicate out to the entire project's community
    - Often these meetings are best held sporadically or ad hoc based on the needs of any one moment on the project
- Advertising and demonstrating the use of shared libraries, and providing guidance on how to best use them
- Formal ownership of any TTS adaptations and shared libraries developed by the project

On very large projects, it may be prudent to staff more than one engineer in this role, especially in moments like the transition to ops where deep perspective on both where the system has come from and where it is going are key to success.

## Virtual Environments and their management

Historically when using Python at JPL, GDS teams managed system Python environments for the use of Teamtools users. But as users became more and more sophisticated, they continually demanded more flexibility. As such, the norm that most projects have settled on (and TTS explicitly endorses) is to use virtual environments controlled by the Teamtools community to manage libraries available to users and developers.

The currently accepted best practice is to control the environment via a `requirements.txt` file in git. Teams wanting new libraries create issues or pull requests to formally request them, and the Systems Teamtools Lead reviews and approves these requests before merging them into the main branch. This formality may seem like overkill early in the mission, but as complexity grows, paper trails are essential to understand whether requirements are still needed and to know what can be regularly pruned. Otherwise the requirements will bloat and the lead will not be able to assess the risk in removing or updating any given repository.

Some projects have tried using different branches in git for development and staging, but in reality these have seen limited use. Successful management of teamtools is a balance of agility and formality, and so far no one has found a particularly useful way to utilize such branches effectively. The story with develop and staging artifactory indexes is similar. A small group of teamtools core developers may want to have this functionality, but it is generally not useful to the full team.

Teamtools Studio currently uses the Python `venv` module as the state of practice for creating and maintaining virtual environments, but we are aware that some teams prefer `uv`, `conda`, or `miniforge`. The decision to use `venv` is not hard and fast, but it is still recommended to standardize the work of teamtool developers.

Despite the utility of the systems virtual environment, the Teamtools Studio does not recommend that all teams blindly use it. There will be some instances where it makes sense for individual teams to maintain their own virtual environments for some tooling. This is often the case when teams come to a project with legacy code from former projects and does not have the budget to fully modernize their tooling. While continually modernizing all software on the project should be the norm, it is sometimes simply not possible, and allowing teams to manage their own environments is a tool in the teamtools toolbox. However, any team that decides to manage their own venv should understand that they are doing so **ON RISK**. The decision or not to modernize a team's software should hinge strongly on the likelihood that their software will need to be run in a different environment, or reused in some way. The more self-contained the application, the more acceptable it is to just manage it on its own. But even something like an automation pipeline can be easily stymied by non-systems virtual environments.

## GitHub Org Design 

GitHub organizations are a place where missions often introduce unnecessary complexity without realizing they are doing it. Teamtools Studio recommends setting up organizations to manage access control, and as such orgs should be created for each major team on the project. Repositories should not necessarily be created on a per team basis, but instead based on function. Remember that the organizations that work best for development in Phases C and D often are not the same as those that make the most sense in operations.

At a minimum, a mission needs to have an organization dedicated to the Systems Teamtools. This will include an environment repository as well as repositories for each of the TTS adaptations described below.

TTS strongly recommends that ALL mission repositories maintain read access for all JPL users, or when necessary, limits read access to only [mission_name]_teamtools_users (see below). While write access can be prudently locked to only a small subset of users on a team, read access should default to as broad as is allowable by a project's information control policies.

## LDAP and GH Groups

TTS recommends every project maintains a [mission_name]_teamtools_admin and [mission_name]_teamtools_users LDAP groups and GitHub groups with the same names and synced users on each. This enables permission management and communication to be as common as possible between GitHub orgs, GitHub Actions, Artifactory, Outlook Calendar invites, and any email announcements that need to be made.

It may also be prudent to have groups/lists like [mission_name]_[subsystem]_teamtools, but those decisions are better made by the project.

## GitHub Org Design Example (large mission)

| Organization Name | Description | Key Repositories |
|----------|----------|----------|
| [Mission Name] System Teamtools | Core teamtools infrastructure and shared libraries | environment, [msn]_data_utils, [msn]_ddp, [msn]_dictionary_interface, [msn]_query |
| [Mission Name] Flight Software | Flight software development | As needed per FSW team |
| [Mission Name] Flight Software Integration and Test | Flight software development and testing | As needed per FIT team |
| [Mission Name] Flight System | Flight software development and testing | As needed per FSSE subsystems (e.g. Power, Thermal, Avionics, etc) |
| [Mission Name] Robotics System | Instrument-specific ground tools and data processing | As needed per robotic subsystems (e.g. Mobility, Arm, Drill) |
| [Mission Name] Instrument Engineering | Instrument-specific ground tools and data processing | As needed per IE subsystems  |
| [Mission Name] Mission System | Operations planning, scheduling, and monitoring | Operations specific reporting, simulation support, generation of ops products |


## GitHub Org Design Example (small mission)

| Organization Name | Description | Key Repositories |
|----------|----------|----------|
| [Mission Name] System Teamtools | Core teamtools infrastructure and shared libraries | environment, tts_data_utils, tts_telemetry, tts_commanding, tts_sequencing |
| [Mission Name] Flight System | Flight software development and testing | As needed by FSW/FSSE teams |
| [Mission Name] Operations | Flight software development and testing | Operations specific reporting, simulation support, generation of ops products |
| [Mission Name] Analysis Tools | Shared analysis tools | As needed |

Note that these are notional reference designs and are not prescriptions. Every project will have its own needs and setups. The key is to remember that tooling may change hands and organizations that exist in early development may not in operations and vice versa. Both GitHub Organization and Repository design should always be done in atomic enough ways that ownership changes can be easily accomplished by moving repositories from one organization to another, even if the new organization did not exist until recently.

It is also imperative to notice that Mission System and Flight System will need to collaborate on this design. Many tools that begin their lives as analysis tools on testbeds will need to be used in operations and this atomicity will be key to enabling a smooth transition to operations.

## Day Zero Repositories

Because they are so fundamental to the way we do work at JPL, Teamtools Studio recommends that **EVERY** project includes adaptations of 4 libraries on day zero. Even if some of the adaptations are little more than a passthrough, it is extremely important to have a mission adaptation layer. Much of the Teamtools Studio design philosophy is built around class extension. This derives directly from our design philosophy that [Projects manage their own risk](../philosophy.md#projects-manage-their-own-risk). Even a very simple adaptation plus the instructions to your project to use the project-specific libraries means that you can change the behavior of the library at any time without waiting for TTS to make changes. This is a powerful tool for managing risk and ensuring that your project can move forward even if TTS is not able to support your specific use case on the timeline that you need it. If your users are using your extensions, then you can drop in new or changed functionality at any time on your own schedule without needing your users to change anything in many cases. Often you will still want to negotiate with TTS to get changes into the core (especially bug fixes), but this way negotiations with parties outside of your project happens **AFTER** you fix your own problem instead of before someone else fixes it for you.

While projects should explore all repositories to decide which adaptations are necessary, the following are the essential set to be adapted for day 0.

- [tts_query](https://github.com/NASA-JPL-Teamtools-Studio/tts_query/blob/main/README.md): The query switchboard. Often projects do not have the same database for early in the project and in mature operations (e.g. Legacy AMPCS vs Chillax or Elasticsearch). This library is a simple wrapper around all query interfaces in a project so users can write code that is agnostic to query source outside of a single keyword argument. This library is extremely important for testbed and ATLO code that will be reused in operations as data backends often change at the transition to operations.
- [tts_dpp](https://github.com/NASA-JPL-Teamtools-Studio/tts_dpp/blob/main/README.md): Data Product Parsing. DPP does not do much data product parsing on its own besides calling the EAS studio's `dplib` when available. Instead it provides a common library for DP owners to provide parsers to a common interface for engineers across the project. It is extremely valuable when products have use cases beyond the team that owns them (e.g. Command History). 
- [tts_dictionary_interface](https://github.com/NASA-JPL-Teamtools-Studio/tts_dictionary_interface/blob/main/README.md): Dictionaries are the Rosetta Stone of spacecraft engineering, but historically JPL missions have not had common ways of accessing them, often with many teams using tools like XML2Dict or lxml to parse them on an ad hoc basis. While there have been some cases of cross-team dictionary ingestors at JPL, `tts_dictionary_interface` goes even one step further, creating a common interface across **projects**. This is extremely useful for tooling that will use dictionaries later like `tts_seq` and enables optional but powerful capabilities in tools like `tts_data_utils` by enforcing conventions that allow TTS core developers to make key interface assumptions about how to retrieve dictionary information from a project without knowing a priori what that project's dictionaries look like exactly.
- [tts_data_utils](https://github.com/NASA-JPL-Teamtools-Studio/tts_data_utils/blob/main/README.md): Shared analysis toolkit. `tts_data_utils` provides among other classes, the `tts_data_frame`. This is an extension of the Pandas dataframe, and borrows heavily from `mech_data_tools` on Mars 2020. This allows teams to create dataframes that contain logic specific to their use cases like parsing EVR information or finding contiguous chanvals that are in alarm. The functionality enabled by `tts_data_utils` is fairly open ended, but it includes:
    - Interpolation of channels for scatter plotting, even when channels are reported at different times (with configurable options for how to interpolate and when )

The convention for naming adaptations is to replace TTS in each with a three or four letter identifier for your mission (e.g. SRL, M20, EURC)

TTS also recommends installing [`tts_dtat`](https://github.com/NASA-JPL-Teamtools-Studio/tts_dtat/blob/main/README.md), which has not yet been massaged into the same class extension model as the others

Teams using Teamtools Studio from within JPL should reach out to Section 326 or the Teamtools Studio for support. Adaptation is straightforward, but will be even faster with support from the Teamtools Studio team. One FTE week should be more than sufficient for initial setup (including margin).

Teams outside of JPL are free to ask questions in the public discussions and should follow the DemoSat examples. 

---
<a href="https://github.com/NASA-JPL-Teamtools-Studio/teamtools_documentation/blob/main/docs/collaboration/day_zero_design.md" target="_blank" rel="noopener noreferrer">Edit/Comment on GitHub</a>
