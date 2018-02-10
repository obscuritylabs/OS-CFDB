# Finding Details 

### Finding Matrix
| Title  | VSR  |  CVSS  | Risk |
|:-:|:-:|:-:|:-:|
| Inadequate Network Segmentation   | 4  | 6.0 – 7.9  |  High  |

### Finding Service
| Service  |
|:-:|
| Internal Penetration Testing  |
| External Penetration Testing  |

### Finding NIST 800-53 Controls
| NIST  |
|:-:|
| SC-32 |
| SC-7  |


### Finding MITRE ATT&CK Corelation
| Name | Tactic | ID | Link |
|:-:|:-:|:-:|:-:|
| Exfiltration Over Command and Control Channel | Exfiltration |  T1041 | https://attack.mitre.org/wiki/Technique/T1041 |

### Finding Refrences
| URL |
|:-:|
| https://www.cisco.com/c/en/us/about/security-center/framework-segmentation.html |
| https://www.sans.org/reading-room/whitepapers/bestprac/infrastructure-security-architecture-effective-security-monitoring-36512 |
  
# Technical Information

## Description 
The assessment team discovered that portions of the network have inadequate security boundaries. Improper network segmentation can allow unauthorized traffic to reach unattended destinations. This type of network architecture may be suitable for normal operations but lacks the security needed for critical business functions. 

## Impact
This ability to move traffic from a low security to a high-security boundary may allow an attacker to escalate privileges or access critical business data. If an attacker can locate firewall misconfigurations or crossing boundaries, they may be able to communicate to high-value targets within a secure enclave. 


## Recommendation(s)
Configure internal firewalls and network infrastructure to isolate traffic to areas of the network as necessary.  Network segmentation should take into account where more sensitive administrative or operational information resides, and bias toward protection of that data. If this is not possible an audit should be conducted and a risk assessment to determine a functions balance of security and operations. 

# Finding Metadata
### Finding Development
| Author Name | Twitter Handle | Email | Created | Updated |
|:-:|:-:|:-:|:-:|:-:|
| Alexander Rymdeko-Harvey | @Killswitch-GUI |  | 09/27/2017 | 09/27/2017 |

### Finding Sources
| URL | 
|:-:|
|  |
