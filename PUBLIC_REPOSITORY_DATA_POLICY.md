# Public Repository Data Policy

This repository is the reusable, portfolio-safe framework for **Onboarding Mapping Analyst**.

It is intentionally separated from the governed operational data used by a real implementation.

## Allowed in this repository

- agent architecture and routing logic;
- reusable Skills;
- governance patterns;
- templates and schemas;
- synthetic examples;
- generic CRM and project-system concepts;
- generated empty/template artifacts;
- documentation that does not identify a private client or implementation.

## Do not commit

- customer, employee, partner, or production records;
- real request payloads or CRM snapshots;
- populated production evidence;
- approved or draft client mappings;
- private service/application names;
- internal architecture identifiers;
- confidential product or partner-specific rules;
- private URLs, tickets, account IDs, tenant IDs, or environment identifiers;
- API keys, tokens, passwords, certificates, secrets, or credentials;
- user-specific personalization profiles;
- request-specific outputs containing operational data.

## Storage model

Real governed inputs and outputs belong in the external mapping workspace described by the architecture. The Git repository contains the reusable intelligence layer, not the operational dataset.

## Before publishing

A repository must be checked for both current files **and Git history**. Deleting a sensitive file in a later commit does not remove it from earlier commits.

If client-specific material was ever committed, sanitize the history or publish from a clean history before changing repository visibility.
