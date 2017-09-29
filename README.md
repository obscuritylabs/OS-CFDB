# OS-CFDB: Open Source - Common Findings Data Base
This project aims to provide a single source of common findings seen on Web Application, Network, and Red Team assessments. While this project is scalable, it may not cover every single scenario applicable to your needs or reporting SOP (Standard Operating Procedures).

*Please understand that this is **Open Source** project that is driven by **community** feedback. If you do not contribute, who will? Please take the time to correct, update, or even make a pull request when you are feeling up to the task.*

## How to Interpret the Data

### How the Data is Supplied
 * JSON - Will allow for serializable data structures or integration into many other solutions.
 * MD - MarkDown is a way to display structured text and allow readers to view the findings easily.

|  Vulnerability Severity Rating |  Vulnerability Severity Rating |  Vulnerability Severity Rating |
|:-:|:-:|---|
|  Level 5 | 8.0 – 10.0  | The vulnerability may allow: an attacker to assume remote administrator or root privileges; exposure (full read and write access) of a host, application or backend database; an attacker to issue remote commands or execute arbitrary code.  |
|  Level 4 | 6.0 – 7.9  | The vulnerability may allow: an attacker to assume only user privileges, or perform a complete denial of service attack; partial exposure (read access only) of, for example, the host file system or a listing of all host or application users.  |
|  Level 3 | 4.0 – 5.9  | The vulnerability may allow: An attacker to abuse or misuse a host or application, or perform a partial denial of service attack. Partial exposure (read access only) to sensitive host or network security configuration details or source code that allows an attacker to research additional attack(s).  |
|  Level 2 |  2.0 – 3.9 | The vulnerability may allow: information leakage, such as software distribution or version information that may be used by an attacker to research potential attacks against a host or application.  |
|  Level 1 |  0.0 -1.9 |  The vulnerability may allow: exposure of general information about a host or application. |


# License Data

BSD 3-Clause License

Copyright (c) 2017, ⭕Alexander Rymdeko-Harvey
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this
  list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice,
  this list of conditions and the following disclaimer in the documentation
  and/or other materials provided with the distribution.

* Neither the name of the copyright holder nor the names of its
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
