# Finding Details 

### Finding Matrix
| Title  | VSR  |  CVSS  | Risk | ID |
|:-:|:-:|:-:|:-:|:-:|
|  SMB Signing Disabled | 4  | 6.0 – 7.9  | High  | OS-CFDB-1008 | 

### Finding Service
| Service  |
|:-:|
| Internal Penetration Testing  |
| External Penetration Testing  |

### Finding NIST 800-53 Controls
| NIST  |
|:-:|
| CM-2 |
| CM-6 | 
| IA-2 |
| IA-3 |


### Finding MITRE ATT&CK Correlation
| Name | Tactic | ID | Link |
|:-:|:-:|:-:|:-:|
| Network Sniffing	| Credential Access | T1040 | https://attack.mitre.org/wiki/Technique/T1040 |

### Finding References
| URL |
|:-:|
| https://pen-testing.sans.org/blog/2013/04/25/smb-relay-demystified-and-ntlmv2-pwnage-with-python |
| https://support.microsoft.com/en-us/help/161372/how-to-enable-smb-signing-in-windows-nt |
| https://blogs.technet.microsoft.com/josebda/2010/12/01/the-basics-of-smb-signing-covering-both-smb1-and-smb2/ |
| https://msdn.microsoft.com/en-us/library/windows/desktop/aa378749(v=vs.85).aspx |
 
 
# Technical Information

## Description 
Server Message Block (SMB) is the file protocol most commonly used by Windows. This protocol allows communication for network file sharing or accessing remote resources of a server. SMB singing specifically is supported on all versions of SMB (1,2,3) but only enabled on Domain Controllers by default. This security feature allows the protocol to ensure authenticity at the packet level.


## Impact
If an attacker gains access to the LAN (Local Area Network), it enables the ability to send specially crafted packets using LLMNR (Link-Local Multicast Name Resolution) spoofing to direct network share access queries to the attacker. Using this MITM (Man-In-The-Middle) attack, an attacker can capture NTLM and NTLMv2 (Windows Challenge/Response Protocol) credentials and potentially brute force these to gain access to resources on the network. 



## Recommendation(s)
The assessment team recommends that SMB signing enabled via GPO policy or registry for the In-Scope network hosts. If this is not possible due to business constraints, core servers and resources should allow SMB signing to prevent GPO tampering or credential compromise of high-value accounts.  

# Finding Metadata
### Finding Development
| Author Name | Twitter Handle | Email | Created | Updated |
|:-:|:-:|:-:|:-:|:-:|
| Alexander Rymdeko-Harvey | @Killswitch-GUI |  | 09/27/2017 | 09/27/2017 |

### Finding Sources
| URL | 
|:-:|
|  |
