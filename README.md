[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
# OS-CFDB: Open Source - Common Findings Data Base

This project aims to provide a single source of common findings seen on **Web/Application**, **Network**, and **Red Team** assessments. While this project is scalable, it may not cover every single scenario applicable to your needs or reporting SOP (Standard Operating Procedures).

> *Please understand that this is **Open Source** project that is driven by **community** feedback. If you do not contribute, who will? Please take the time to correct, update, or even make a pull request when you are feeling up to the task.*

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [OS-CFDB: Open Source - Common Findings Data Base](#os-cfdb-open-source---common-findings-data-base)
  - [Why?](#why)
  - [How to Interpret the Data](#how-to-interpret-the-data)
    - [Finding Details](#finding-details)
    - [Technical Information](#technical-information)
    - [Finding Metadata](#finding-metadata)
  - [How the Data is Supplied](#how-the-data-is-supplied)
  - [Finding Classification and Scoring](#finding-classification-and-scoring)
- [Current Finding Tree](#current-finding-tree)
- [License Data](#license-data)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Why?

Too often in prior experience reporting was repetitive, inaccurate and time loss incurred during the phase of the assessment. These constraints were due to lack of a centralized repository for findings, a single source of truth. However, this can raise a greater question of how we can integrate into automation. Moving forward this project hopes to help small, over-tasked, and startups produce valuable data for clients and their organizations they support.

## How to Interpret the Data

The data within this project is broken out into multiple headers and lists; this allows for easy data serialization to JSON or other future formats as long as an MD parser exists.  You will find **three** major sections:

- Finding Details 
- Technical Information 
- Finding Metadata 

 Each major section contains multiple sub-sections to help automate and use canned vocabulary.

### Finding Details

 Contains the common data types that may be needed to include in reporting metadata and allow for toolset integration.

- Title - The title of the finding
- VSR - Vulnerability Severity Rating - Custom developed default rating to place a finding
- CVSS - Applied score that depicts a translation from VSR to CVSS
- Risk - The commonly applied label of the finding 
- Service - Descriptor of how a finding denoted identification 
- NIST 800-53 - Specific correlating controls to finding
- MITRE ATT&CK - Linked tactics that may relate to the finding for further risk analysis

- References - Curated list of sources that should be used during reporting

### Technical Information

- Description - The technical overview of a finding, this is not meant to be all-inclusive.
- Impact - A section of a how the result will affect an organization.
- Recommendation(s) - Current plan of action to impment.

### Finding Metadata

- Author(s) - List of people that worked on a finding.
- Source(s) - Sources the author used for research of a finding.
- Created - Time and date of creation.
- Updated - time and date of an update to a finding.

## How the Data is Supplied

- JSON - Will allow for serializable data structures or integration into many other solutions.
-- **CURRENTLY UNDER DEVLOPMENT** 
- MD - MarkDown is a way to display structured text and allow readers to view the findings quickly.


## Finding Classification and Scoring

Each finding is provided a **Default** Vulnerability Severity Rating (VSR) & a correlated Common Vulnerability Scoring System (CVSS) identifier. 

| Vulnerability Severity Rating | Common Vulnerability Scoring System (CVSS) | Vulnerability Severity Evaluation Criteria |
| :---------------------------: | :--------------------------------------: | :--------------------------------------- |
|            Level 5            |                8.0 – 10.0                | Finding may allow an attacker to gain remote execution as a privileged or unprivileged user that exposes sensitive data, or allows read/write of a remote system. This may allow an attacker to execute code, change or read sensitive data and break all confidentiality, integrity or accountability of the affected system. |
|            Level 4            |                6.0 – 7.9                 | The finding may allow an attacker to gain read-only, denial or resources or under certain conditions, the exploitability allows user-mode code execution.  |
|            Level 3            |                4.0 – 5.9                 | The finding may allow an attacker to manipulate or abuse application functionality, denial of service or partial read-only access to application data in a constrained environment.  |
|            Level 2            |                2.0 – 3.9                 | The finding may allow an attacker to obtain sensitive information about a system, internal network, or other identifying data that could lead to further compromise.  |
|            Level 1            |                 0.0 -1.9                 | The finding may allow an attacker to gather vague system information. This often occurs to do best practices not being properly implemented. |

# Current Finding Tree

* [LICENSE](./LICENSE)
 * [README.md](./README.md)
 * [android](./android)
   * [logging.md](./android/logging.md)
 * [ios](./ios)
   * [logging.md](./ios/logging.md)
 * [linux](./linux)
   * [outdated_kernal.md](./linux/outdated_kernal.md)
 * [macos](./macos)
   * [outdated_operating_system.md](./macos/outdated_operating_system.md)
 * [phishing](./phishing)
   * [spear_phishing_susceptibility.md](./phishing/spear_phishing_susceptibility.md)
   * [spear_phishing_weaknessess.md](./phishing/spear_phishing_weaknessess.md)
 * [web](./web)
   * [blind_sql_injection.md](./web/blind_sql_injection.md)
   * [refelctive_xss.md](./web/refelctive_xss.md)
   * [stored_xss.md](./web/stored_xss.md)
 * [windows](./windows)
   * [Insecure_active_direcotry_user_acl.md](./windows/Insecure_active_direcotry_user_acl.md)
   * [default_administrator_enabled.md](./windows/default_administrator_enabled.md)
   * [ease_account_leakage.md](./windows/ease_account_leakage.md)
   * [firewall_misconfiguration.md](./windows/firewall_misconfiguration.md)
   * [inadequate_network_segmentation.md](./windows/inadequate_network_segmentation.md)
   * [insecure_credential_storage.md](./windows/insecure_credential_storage.md)
   * [insecure_file_shares.md](./windows/insecure_file_shares.md)
   * [insecure_sysvol_scripts.md](./windows/insecure_sysvol_scripts.md)
   * [mscachev2_misconfiguration.md](./windows/mscachev2_misconfiguration.md)
   * [smb_signing_disabled.md](./windows/smb_signing_disabled.md)
   * [standard_user_with_local_admin.md](./windows/standard_user_with_local_admin.md)
   * [weak_password_policy.md](./windows/weak_password_policy.md)
   * [weak_spn_password.md](./windows/weak_spn_password.md)
   * [wpad_enabled.md](./windows/wpad_enabled.md)
