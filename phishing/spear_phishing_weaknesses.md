# Finding Details 

### Finding Matrix
| Title  | VSR  |  CVSS  | Risk |
|:-:|:-:|:-:|:-:|
|  Spear Phishing Weaknesses | 3  | 4.0 – 5.9  |  Medium |

### Finding Service
| Service  |
|:-:|
| Internal Penetration Testing  |
| External Penetration Testing  |

### Finding NIST 800-53 Controls
| NIST  |
|:-:|
| SC-7 |
| SI-3 |


### Finding MITRE ATT&CK Correlation
| Name | Tactic | ID | Link |
|:-:|:-:|:-:|:-:|
| Spear phishing messages with malicious links | Launch | PRE-T1146 | https://attack.mitre.org/pre-attack/index.php/Technique/PRE-T1146 |

### Finding References
| URL |
|:-:|
| https://www.us-cert.gov/report-phishing |

  
# Technical Information

## Description 
The assessment team was able to spear phish successfully the in-scope organization; this requires an attacker's email to pass through the network border. Phishing commonly requires the email to make it through NSM (Network Security Monitoring) appliances and require user interaction to execute the payload. Most common phishing attacks can be mitigated by string border and host level automated protections. In some cases, inadequate host protections allow for execution of malicious payloads. 

## Impact
When a phishing email can subvert NSM and AESP (Advanced Endpoint Security Protection), an attacker can gain code execution on the target. Execution could lead to full system compromise and post-exploitation activities.

## Recommendation(s)
Regularly analyze border and host-level protections, including spam-filtering capabilities, to ensure their continued effectiveness in blocking the delivery and execution of malware. Build custom IOC's (Indicators of Compromise) to mitigate APT (Advanced Persistent Threats) and known techniques. 

# Finding Metadata
### Finding Development
| Author Name | Twitter Handle | Email | Created | Updated |
|:-:|:-:|:-:|:-:|:-:|
| Alexander Rymdeko-Harvey | @Killswitch-GUI |  | 09/27/2017 | 09/27/2017 |

### Finding Sources
| URL | 
|:-:|
|  |
