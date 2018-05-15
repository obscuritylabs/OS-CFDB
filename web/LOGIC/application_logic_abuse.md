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


#### Test business logic data validation (OTG-BUSLOGIC-001)

In business logic data validation testing, we verify that the application does not allow users to insert “unvalidated” data into the system/application. This is important because without this safeguard attackers may be able to insert “unvalidated” data/information into the application/system at “handoff points” where the application/system believes that the data/information is “good” and has been valid since the “entry points” performed data validation as part of the business logic workflow.


#### Test Ability to forge requests (OTG-BUSLOGIC-002)

In forged and predictive parameter request testing, we verify that the application does not allow users to submit or alter data to any component of the system that they should not have access to, are accessing at that particular time or in that particular manner. This is important because without this safeguard attackers may be able to “fool/trick” the application into letting them into sections of thwe application of system that they should not be allowed in at that particular time, thus circumventing the applications business logic workflow.


#### Test Integrity Checks (OTG-BUSLOGIC-003)

In integrity check and tamper evidence testing, we verify that the application does not allow users to destroy the integrity of any part of the system or its data. This is important because without these safe guards attackers may break the business logic workflow and change of compromise the application/system data or cover up actions by altering information including log files.


#### Test for Process Timing (OTG-BUSLOGIC-004)

In process timing testing, we verify that the application does not allow users to manipulate a system or guess its behavior based on input or output timing. This is important because without this safeguard in place attackers may be able to monitor processing time and determine outputs based on timing, or circumvent the application’s business logic by not completing transactions or actions in a timely manner.


#### Test Number of Times a Function Can be Used Limits (OTG-BUSLOGIC-005)

In function limit testing, we verify that the application does not allow users to exercise portions of the application or its functions more times than required by the business logic workflow. This is important because without this safeguard in place attackers may be able to use a function or portion of the application more times than permissible per the business logic to gain additional benefits.


#### Testing for the Circumvention of Work Flows (OTG-BUSLOGIC-006)

In circumventing workflow and bypassing correct sequence testing, we verify that the application does not allow users to perform actions outside of the “approved/required” business process flow. This is important because without this safeguard in place attackers may be able to bypass or circumvent workflows and “checks” allowing them to prematurely enter or skip “required” sections of the application potentially allowing the action/transaction to be completed without successfully completing the entire business process, leaving the system with incomplete backend tracking information.


#### Test Defenses Against Application Mis-use (OTG-BUSLOGIC-007)

In application mis-use testing, we verify that the application does not allow users to manipulate the application in an unintended manner.


#### Test Upload of Unexpected File Types (OTG-BUSLOGIC-008)

In unexpected file upload testing, we verify that the application does not allow users to upload file types that the system is not expecting or wanted per the business logic requirements. This is important because without these safeguards in place attackers may be able to submit unexpected files such as .exe or .php that could be saved to the system and then executed against the application or system.


#### Test Upload of Malicious Files (OTG-BUSLOGIC-009)

In malicious file upload testing, we verify that the application does not allow users to upload files to the system that are malicious or potentially malicious to the system security. This is important because without these safeguards in place attackers may be able to upload files to the system that may spread viruses, malware or even exploits such as shellcode when executed.

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
