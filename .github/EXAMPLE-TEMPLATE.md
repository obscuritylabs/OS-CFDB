# Finding Details 

### Finding Matrix
| Title  | SVR  |  CVSS  | Risk |
|:-:|:-:|:-:|:-:|
| Insecure SYSVOL Scripts  |  3 |  4.0-5.9 | Medium  |

### Finding Service
| Service  |
|:-:|
| Internal Penetration Testing  |
| External Penetration Testing  |

### Finding NIST 800-53 Controls
| NIST  |
|:-:|
| IA-2  |
|  IA-7 |

### Finding MITRE ATT&CK Corelation
| Tactic | ID |
|:-:|:-:|
| Credential Access | T1081 |

### Finding Refrences
| URL |
|:-:|
| https://adsecurity.org/?p=2288 |
 
# Technical Information

### Description 
The SYSVOL folder on DC's (Domain Controllers) is a domain-wide network share in Active Directory (AD) to which all authenticated users in the domain have by default read access. The directory contains login scripts, group policy data, and other data that may be needed to be available to all users. The assessment team discovered that scripts within this folder contain sensitive information that may aid an attacker in lateral movement and reconnaissance.  Within these scripts also contained clear text credentials to other domain resources.

### Impact
If an attacker can gain access to the domain environment, they effectively can use these gathered credentials to attempt privilege escalation. These "User" credentials could result in further lateral movement or the ability to gain unauthorized access to different regions within the domain.

### Recommendation(s)
The assessment team recommends that scripts used for administration, password changes, authenticated share mounting be removed. Automated password changes and authenticated share mounting should be accomplished with proper AD group delegation. A thorough audit should be conducted domain wide to identify other scripts exposing sensitive data or credentials.  

# Finding Metadata
### Finding Development
| Author Name | Twitter Handle | Email | Created | Updated |
|:-:|:-:|:-:|:-:|:-:|
| Alexander Rymdeko-Harvey | @Killswitch-GUI |  | 09/27/2017 | 09/27/2017 |

### Finding Sources
| URL | 
|:-:|
| Http://google.com |
