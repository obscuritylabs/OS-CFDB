# Finding Details 

### Finding Matrix
| Title  | VSR  |  CVSS  | Risk |
|:-:|:-:|:-:|:-:|
| Weak Password Policy   | 3  | 4.0-5.9  | Medium  |

### Finding Service
| Service  |
|:-:|
| Internal Penetration Testing  |
| External Penetration Testing  |

### Finding NIST 800-53 Controls
| NIST  |
|:-:|
| IA-2 |
| IA-7 |


### Finding MITRE ATT&CK Corelation
| Name | Tactic | ID | Link |
|:-:|:-:|:-:|:-:|
| Brute Force | Credential Access  | T1110 | https://attack.mitre.org/wiki/Technique/T1110 |

### Finding Refrences
| URL |
|:-:|
| https://technet.microsoft.com/en-us/library/cc731699(v=ws.11).aspx |
| https://technet.microsoft.com/en-us/library/cc786468(v=ws.10).aspx |
 
# Technical Information

## Description 
The strength of a password policy is a combination of length, complexity, and predictability. Failure to implement a strong password may result in unauthorized access to a system or application.  A strong password policy can protect an organization from brute-force password cracking, guessing, and reuse.

## Impact
If a strong password policy is absent, reverse brute-force and password guessing attacks can take place. These attacks can lead to further system compromise of domain access in a unauthenticated scenario.

## Recommendation(s)
Enforce password policy on all systems by applicable industry best practices, and company-defined requirements. Corporate password policy should be enforced via GPO (Group Policy Objects).

# Finding Metadata
### Finding Development
| Author Name | Twitter Handle | Email | Created | Updated |
|:-:|:-:|:-:|:-:|:-:|
| Alexander Rymdeko-Harvey | @Killswitch-GUI |  | 09/27/2017 | 09/27/2017 |

### Finding Sources
| URL | 
|:-:|
|  |
