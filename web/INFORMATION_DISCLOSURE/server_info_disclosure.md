# Finding Details 

### Finding Matrix
| Title  | VSR  |  CVSS  | Risk |
|:-:|:-:|:-:|:-:|
| Database Information Disclosure  | 1-5  |  0.0-10.0 | Medium-High  |

### Finding Service
| Service  |
|:-:|
| Internal Penetration Testing  |
| External Penetration Testing  |

### Finding NIST 800-53 Controls
| NIST  |
|:-:|
| AC-1 |
| AC-17 |
| AC-22 |
| SC-23 |
| SI-15 |
| AC-3 |
| CA-2 |
| CA-7 | 
| CA-8 |

### Finding MITRE ATT&CK Corelation
| Name | Tactic | ID | Link |
|:-:|:-:|:-:|:-:|
| Exploit Public-Facing Application | Initial Access | T1190 | https://attack.mitre.org/wiki/Technique/T1190 |

### Finding Refrences
| URL |
|:-:|
| https://attack.mitre.org/wiki/Technique/T1190 |
| http://cwe.mitre.org/data/definitions/284.html |
| https://portswigger.net/kb/issues/00600200_email-addresses-disclosed |
| https://portswigger.net/kb/issues/00600400_social-security-numbers-disclosed |
| https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-53r4.pdf |

# Technical Information

### Description 
The use of software, data, or commands to take advantage of a weakness in an Internet-facing computer system or program in order to cause unintended or unanticipated behavior. The weakness in the system can be a bug, a glitch, or a design vulnerability. These applications are often websites, but can include databases (like SQL), standard services (like SMB2 or SSH), and any other applications with Internet accessible open sockets, such as web servers and related services. Depending on the flaw being exploited this may include Exploitation for Defense Evasion.
For websites and databases, the OWASP top 10 gives a good list of the top 10 most common web-based vulnerabilities.

### Impact
If an attacker can gain access to unauthorized data, they effectively can use the gathered data for further attacks against the web application or secondary/backend systems, as well as target users accounts.

### Recommendation(s)
The assessment team recommends that thorough testing be conducted on all resources to identify other web applications that are exposing sensitive data. In addition to additional testing, the following are some guidelines to follow so you can make sure that your web applications are well protected against the most obvious information disclosure issues:

* Make sure that your web server does not send out response headers that reveal information about the backend technology type or version.
* Make sure that all the services running on the server’s open ports do not reveal information about their builds and versions.
* Always make sure that proper access controls and authorizations are in place in order to disallow access for attackers on all web servers, services and web applications.
* Do not hard code credentials, API keys, IP addresses, or any other sensitive information in the code, not even in the form of comments.
* Configure the correct MIME types on your web server for all the different files being used in your web applications.
* Sensitive data or files that do not need to be on the web servers should never be uploaded on the web server.
* Always check whether each of the requests to create/edit/view/delete resources has proper access controls, preventing privilege escalation issues and making sure that all the confidential information remains confidential.
* Make sure that your web application processes user input correctly, and that a generic response is always returned for all the resources that don’t exist/are disallowed in order to confuse attackers.
* Enough validations should be employed by the backend code in order to catch all the exceptions and prevent the leakage of valuable information.
* Configure the web server to suppress any exceptions that may arise and return a generic error page.
* Configure the web server to disallow directory listing and make sure that the web application always shows a default web page.  

# Finding Metadata
### Finding Development
| Author Name | Twitter Handle | Email | Created | Updated |
|:-:|:-:|:-:|:-:|:-:|
| Keelyn Roberts | @real_slacker007 |  | 05/11/2018 | 05/11/2018 |

### Finding Sources
| URL | 
|:-:|
| https://attack.mitre.org/wiki/Technique/T1190 |
| http://cwe.mitre.org/data/definitions/284.html |
| https://portswigger.net/kb/issues/00600200_email-addresses-disclosed |
| https://portswigger.net/kb/issues/00600400_social-security-numbers-disclosed |
| https://nvlpubs.nist.gov/nistpubs/specialpublications/nist.sp.800-53r4.pdf |
