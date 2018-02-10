# Finding Details 

### Finding Matrix
| Title  | VSR  |  CVSS  | Risk |
|:-:|:-:|:-:|:-:|
| Standard User with Local Admin  | 3  | 4.0-5.9  | Medium  |

### Finding Service
| Service  |
|:-:|
| Internal Penetration Testing  |
| External Penetration Testing  |

### Finding NIST 800-53 Controls
| NIST  |
|:-:|
| AC-6 |


### Finding MITRE ATT&CK Corelation
| Name | Tactic | ID | Link |
|:-:|:-:|:-:|:-:|
| Bypass User Account Control | 	Defense Evasion, Privilege Escalation | T1088 | https://attack.mitre.org/wiki/Technique/T1088 |

### Finding Refrences
| URL |
|:-:|
| https://technet.microsoft.com/en-us/library/dd744293(v=ws.10).aspx |
| https://nvd.nist.gov/800-53/Rev4/control/AC-6 | 
 
 
# Technical Information

## Description 
Following the least privileged model, standard users should have only enough rights to perform their task or duty. The assessment team discovered the following users contain the group permissions of Administrator. Resulting in the ability for the assessment team to execute a User Access Control (UAC) bypass to gain full SYSTEM privileges of the host.  

## Impact
Over delegation of Local Admin rights to a “Standard” user account can result in unwanted, unauthorized or unnecessary software system access. If a system becomes compromised in a “Standard” user context, an attacker can use local administrator privileges to gain access to cached credentials, install persistence, or perform post exploitation attacks to further their access.  

## Recommendation(s)
The assessment team recommends that the least privileged model is followed when assessing if users should have the local “Administrator” group permission. In many cases, this privilege could be granted on a case-by-case basis for certain administrative functions. One method of employing this is using credential checkout systems or assigning the user a secondary account for administrator functions. These remediations reduce the overall attack surface of running at elevated privilege levels for day-to-day tasks.

# Finding Metadata
### Finding Development
| Author Name | Twitter Handle | Email | Created | Updated |
|:-:|:-:|:-:|:-:|:-:|
| Alexander Rymdeko-Harvey | @Killswitch-GUI |  | 09/27/2017 | 09/27/2017 |

### Finding Sources
| URL | 
|:-:|
|  |
