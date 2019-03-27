# Finding Details 

### Finding Matrix
| Title  | VSR  |  CVSS  | Risk | ID |
|:-:|:-:|:-:|:-:|:-:|
|  Insecure Credential Storage | 4  | 6.0 – 7.9  |  High | OS-CFDB-1004

### Finding Service
| Service  |
|:-:|
| Internal Penetration Testing  |
| External Penetration Testing  |

### Finding NIST 800-53 Controls
| NIST  |
|:-:|
| SI-13 |


### Finding MITRE ATT&CK Correlation
| Name | Tactic | ID | Link |
|:-:|:-:|:-:|:-:|
| Credentials in Files | Credential Access | T1081 | https://attack.mitre.org/wiki/Technique/T1081 |

### Finding References
| URL |
|:-:|
|https://www.sans.org/reading-room/whitepapers/authentication/clear-text-password-risk-assessment-documentation-113  |
 
# Technical Information

## Description 
The assessment team discovered storage of high-value accounts in a clear text format. Storing credentials of this nature in clear text is a severe security risk, allowing an attacker to gain access to credentials with ease. While allowing an attacker to use these credentials to compromise applications or systems of interest under the user context of the affected account. 

## Impact
Insecure credentials allow an attacker to Impersonate a legitimate user, breaking the authenticity of the system logging. Compromise of the host system could lead to malicious commands and actions to go unnoticed due to the privilege level of the account. 

## Recommendation(s)
Implement a review process for files and systems to look for cleartext account credentials. Secure all passwords with a centralized or independent password manager that meets business requirements.

# Finding Metadata
### Finding Development
| Author Name | Twitter Handle | Email | Created | Updated |
|:-:|:-:|:-:|:-:|:-:|
| Alexander Rymdeko-Harvey | @Killswitch-GUI |  | 09/27/2017 | 09/27/2017 |

### Finding Sources
| URL | 
|:-:|
|  |
