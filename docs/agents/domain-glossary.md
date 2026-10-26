# Domain Glossary

## Purpose

Shared deterministic terms used across TTS repos. Repo-specific language stays in each repo's `CONTEXT.md`. This glossary is lazy: terms are added as `/domain-modeling` surfaces gaps/conflicts.

## Conventions

- Terms are canonical; synonyms are listed as avoided.
- Definitions are short and stable.
- Link to ADR when term is decision-driven.

## Current terms

**EHA**:
Engineering and Housekeeping Attributes — continuous time-series telemetry
channel samples from spacecraft sensors/subsystems (numeric measurements,
status values, health indicators).
_Avoid_: channel value, telemetry point (when EHA specifically is meant)

**EVR**:
Event Record — a discrete FSW log message carrying a severity level,
distinct from EHA's continuous numeric samples.
_Avoid_: event, log message (when EVR specifically is meant)

## Usage

When naming concepts in issues, refactor proposals, tests, use the term as defined here or in the owning repo's `CONTEXT.md`. If a term is missing, note it for `/domain-modeling` rather than inventing new language.

## Maintenance

This file is canonical for cross-repo vocabulary. Convenience copies in repos are allowed but must reference this file.
