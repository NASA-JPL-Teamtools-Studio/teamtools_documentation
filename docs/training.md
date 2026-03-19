# Teamtools Studio (TTS) Operator-Developer Training Curriculum

## Program Overview
**Goal:** Transform operators with moderate Python scripting experience into "Operator-Developers" capable of building, maintaining, and utilizing multi-mission libraries within the Teamtools Studio ecosystem.
**Prerequisites:** Moderate Python syntax knowledge, basic familiarity with command-line operations, at least a year or two experience in operations or operations development

---

## Module 1: Why are we here?
*Objective: Get on the same page about what it is that TTS is attempting to do here. What are the tupical stumbling blocks
for JPL projects in Teamtools Space? How does TTS propose to improve that situation?*


### 1.1 What is the Teamtools Studio? What isn't it?
* **Really? You want to own ALL TEAMTOOLS?** No, not really... lots of technical debt, etc. Own process, core tools
* **Aren't you just reinventing GDS?** Yes and no... can't know a priori where the gaps will be, on small project you could use a lot more than on large ones.
* **The Penultimate 3/4 Mile:** GDS is still the primary ground software solution. But they will never do the last mile as well as we do.
* **Developing a Center of Excellence at JPL:** We want to establish a cadre of experts to lead the way JPL does this work going forward.
* **Intro to TTS documentation**: Look at the docs, explain standards, how to find stuff, where it's all deployed, etc

### 1.2 Typical Issues in Teamtools
* **Class B, what's that?**: Critical functionality sneaks into teamtools and escapes SQA practice.
* **When Hertitage Doesn't Count**: Can you pick up that potted plant, or is it rooted to the ground? Just because it serves a critical purpose wall on mission A doesn't mean it can be easily carried to mission B
* **Single mission "multimission" tools:** Many engineers are sympathetic to these ideas and have even tried to have bigger impacts by building tools they hope will become multimission

### 1.3 Design Philosophies Part 1: Portability
* **Architecture Drivers:** Core/Adaptation architecture, Abstract Base Classes, big picture view
* **Choices that keep us Light:** No Servers. Very light external dependencies. Abstraction connections to missions

### Exercise
* Install Docker, build image, run unit tests

---

## Module 2: Professional Software Engineering Standards
*Objective: Level up students on the tooling required for collaborative library development, moving beyond "works on my machine."*

### 2.1 Environment Management
* **Virtual Environments:** Moving away from global system Python. Best practices for creating scope-specific environments (e.g., `demosat_tower_development`).
* **Dependency Management:** Understanding `pip`, `requirements.txt`, and resolving conflicts between libraries.

### 2.2 The Git Workflow & Governance
* **Roles:** Understanding the distinction between Contributor, Committer, and Product Manager.
* **Branching & PRs:** Standard workflow for checking out code, creating feature branches, and submitting Pull Requests.
* **Code Review:** How to give and receive feedback constructively.

### 2.3 Quality Assurance
* **Testing:** Introduction to `pytest`. The goal of "one test per function/method" and striving for 100% coverage (with a 50% minimum requirement).
* **Style & Norms:** Walk through of a few key libraries, showing the scope of each, separation of concerns, fundamental stuff like capitalization standards, etc
* **Documentation:** Writing docstrings, building documentation

### 2.4 Introduction to Support Libraries
* **TTS Utilities:** Really just point out it exists, show that there's a logger in there and some other QOL features
* **TTS Spice:** Just point it out, we won't need this for a while, but know it's here
* **HTML Utils:** High level demo of big wins.
* **Data Utils:** Explore ABC structure, show Filter Methods, PowerTable, Lorem, Contextual Highlighting, Nesting of Containers

### 2.5 Continuous Development/Integration
* **Unit Test Matrix:** 
* **Document Builder:**
* **Notional Next Steps:**

### Exercise
* Implement a feature! No matter how small. Even if it's just a docstring change. Clone, branch, push, write the PR

---

## Module 3: Introduction to DemoSat, Planning and Sequencing
*Objective: Start digging into the actual functionality we have, get on the same page about what the gross units of this work are.*

### 3.1 "Functional Library Overview"

### 3.2 DemoSat Introduction

### 3.3 TTS Plan
* **Activities**
* **Claims**
* **Resource Modeling**

### 3.4 TTS Seq (not including simulation)
* **TTS Dictionary Interface:**
* **SeqCollections**
* **SeqDict and its extensions**

### Exercise
* Implement a new activity for DemoSat

---

## Module 4: Simulating DemoSat
*Objective:.*

### 4.2 Simulation Modules
* **Simulation Module Structure:**
* **The EVR Module**
* **Modeling values and the EHA Module**

### 4.3 Simulating Commands
* **The Command Module**
* **Comand Modeling**

### Exercise
* Model and Simulate your DemoSat activity

---

## Module 5: Uplink Rule Checking
*Objective: Understand Tower, Fresh, and the ecosystems they live in.*

### 5.1 Rule Checking Historically
* **SeqGen/SEQR/SOCR**
* **The Phase D Flight Rule Development Bottleneck**
* **Don't Send Command X in Condition Y**

### 5.2 TTS Solutions
* **FRESH:**
* **TOWER:**
* **Exercise:**


## Module 6: Downlink Data Analysis

