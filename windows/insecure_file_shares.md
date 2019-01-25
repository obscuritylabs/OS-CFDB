# Finding Details 

### Finding Matrix
| Title  | VSR  |  CVSS  | Risk | ID |
|:-:|:-:|:-:|:-:|:-:|
|  Insecure File Shares | 3  | 4.0-5.9  | Medium  | OS-CFDB-1005 |

### Finding Service
| Service  |
|:-:|
| Internal Penetration Testing  |
| External Penetration Testing  |

### Finding NIST 800-53 Controls
| NIST  |
|:-:|
| SI-2 |
| AC-1 |
| AC-3 |
| AC-6 |

### Finding MITRE ATT&CK Correlation
| Name | Tactic | ID | Link |
|:-:|:-:|:-:|:-:|
| Network Share Discovery | Discovery | T1135 | https://attack.mitre.org/wiki/Technique/T1135 |

### Finding References
| URL |
|:-:|
| https://technet.microsoft.com/en-us/library/cc754178(v=ws.11).aspx |
| https://technet.microsoft.com/en-us/library/cc772184(v=ws.11).aspx|
 
  
# Technical Information

## Description 
Windows File Shares using NTFS (New Technology File System) allows for granular control over RWX (Read, Write, Execute) down to specific files. Sensitive data related to business functions and personnel often are stored in centralized locations for ease of access. When non-elevated / privileged domain users can access sensitive data, it allows for an attacker to easily exfil or facilitate future attack paths. 

## Impact
This insecure storage misconfiguration leaves data open to theft by an attacker and could cause substantial damage to the organization and its employees. Insecure file shares can also lead to loss of data integrity and malicious code to target HVI (High-Value Individuals) 

## Recommendation(s)
The assessment team recommends following the model of least privileged. Implement a secure configuration by using NTFS Share Permissions and restricting Domain Users and Groups to sensitive data.

# Finding Metadata
### Finding Development
| Author Name | Twitter Handle | Email | Created | Updated |
|:-:|:-:|:-:|:-:|:-:|
| Alexander Rymdeko-Harvey | @Killswitch-GUI |  | 09/27/2017 | 09/27/2017 |

### Finding Sources
| URL | 
|:-:|
|  |
