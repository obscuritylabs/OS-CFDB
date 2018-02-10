# OS-CFDB: Open Source - Common Findings Data Base

This project aims to provide a single source of common findings seen on **Web/Application**, **Network**, and **Red Team** assessments. While this project is scalable, it may not cover every single scenario applicable to your needs or reporting SOP (Standard Operating Procedures).

> *Please understand that this is **Open Source** project that is driven by **community** feedback. If you do not contribute, who will? Please take the time to correct, update, or even make a pull request when you are feeling up to the task.*

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
- MD - MarkDown is a way to display structured text and allow readers to view the findings quickly.


## Finding Classification and Scoring

Each finding is provided a **Default** Vulnerability Severity Rating (VSR) & a correlated Common Vulnerability Scoring System (CVSS) identifier. 

| Vulnerability Severity Rating | Common Vulnerability Scoring System (CVSS) | Vulnerability Severity Evaluation Criteria |
| :---------------------------: | :--------------------------------------: | :--------------------------------------- |
|            Level 5            |                8.0 – 10.0                | Finding may allow an attacker to gain remote execution as a privileged or unprivileged user that exposes sensitive data, or allows read/write of a remote system. This may allow an attacker to execute code, change or read sensitive data and break all confidentiality, integrity or accountability of the affected system. |
|            Level 4            |                6.0 – 7.9                 | The finding may allow an attacker to gain read-only, denial or resources or under certain conditions, the exploitability allows user-mode code execution.  |
|            Level 3            |                4.0 – 5.9                 | The vulnerability may allow: An attacker to abuse or misuse a host or application, or perform a partial denial of service attack. Partial exposure (read access only) to sensitive host or network security configuration details or source code that allows an attacker to research additional attack(s). |
|            Level 2            |                2.0 – 3.9                 | The vulnerability may allow: information leakages, such as software distribution or version information that may be used by an attacker to research potential attacks against a host or application. |
|            Level 1            |                 0.0 -1.9                 | The vulnerability may allow: exposure of general information about a host or application. |

# Current Finding Tree

## Windows

- [Insecure File Shares](windows/insecure_file_shares.md)

# License Data

BSD 3-Clause License

Copyright (c) 2017, ⭕Alexander Rymdeko-Harvey
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

- Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.
- Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  And other materials provided with the distribution.
- Neither the name of the copyright holder nor the names of its
  contributors may be used to endorse or promote products derived from
  this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

