# Finding Details 

### Finding Matrix
| Title  | VSR  |  CVSS  | Risk |
|:-:|:-:|:-:|:-:|
| Web Application-Logic Abuse  | 1-5  |  0.0-10.0 | Medium-High  |

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
| https://www.owasp.org/index.php/Testing_for_business_logic |
| https://csrc.nist.gov/Projects/Access-Control-Policy-Tool/Access-Control-Policy-Testing |

# Technical Information

### Description 
Business logic flaws are critical vulnerabilities and can range in severity based on the level of exposure caused by the logical oversight.  For example, if an application's authentication mechanism is developed with the intention of performing steps 1, 2, 3 in that specific order to authenticate a user. What happens if the user goes from step 1 straight to step 3? In this simplistic example, does the application provide access by failing open; deny access, or just error out with a 500 message?  There are many examples that can be made, but the one constant lesson is "think outside of conventional wisdom". This type of vulnerability cannot be detected by a vulnerability scanner and relies upon the skills and creativity of the penetration tester. In addition, this type of vulnerability is usually one of the hardest to detect, and usually application specific but, at the same time, usually one of the most detrimental to the application, if exploited.  The classification of business logic flaws has been under-studied; although exploitation of business flaws frequently happens in real-world systems, and many applied vulnerability researchers investigate them. The greatest focus is in web applications. There is debate within the community about whether these problems represent particularly new concepts, or if they are variations of well-known principles.  Testing of business logic flaws is similar to the test types used by functional testers that focus on logical or finite state testing. These types of tests require that security professionals think a bit differently, develop abused and misuse cases and use many of the testing techniques embraced by functional testers. Automation of business logic abuse cases is not possible and remains a manual art relying on the skills of the tester and their knowledge of the complete business process and its rules.

### Impact
This type of vulnerability is usually one of the hardest to detect, and usually application specific but, at the same time, usually one of the most detrimental to the application, if exploited.  If an attacker can gain access to unauthorized data, they effectively can use the gathered data for further attacks against the web application or secondary/backend systems, as well as target users accounts.

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
| https://www.owasp.org/index.php/Testing_for_business_logic |
| https://csrc.nist.gov/Projects/Access-Control-Policy-Tool/Access-Control-Policy-Testing |
