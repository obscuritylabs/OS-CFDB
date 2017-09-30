

# Finding Details 

## Title
  Default Administrator Enabled (RID 500)
## SVR
  3
## CVSS
  4.0-5.9
## Risk
  Medium
## Service
  * Internal Penetration Testing
  * External Penetration Testing 
## NIST 800-53 
  * CM-2
  * CM-6
  * IA-2
  * IA-3
## Refrences
  * https://nvd.nist.gov/800-53/Rev4/control/IA-2
  * https://technet.microsoft.com/en-us/mt227395.aspx
 
# Technical Information

## Description 
The default administrator account is often used during initial setup of a host and joining an AD (Active Directory) Domain environment. This type of account is often referred to as BUILTIN\Administrator, also known as NT AUTHORITY\Administrator with the relative identifier (RID) 500. This account exists by default on all Microsoft Windows (Windows NT-based) systems as well as Active Directory domains. The assessment team discovered that hosts contained an enabled Administrator Account. 

## Impact
If an attacker can gain elevated system privileges on a compromised host, the attacker could gather clear-text and the NTLM hash of this account. These credentials could be used to further access or lateral spread mechanisms such as Pass-The-Hash attacks where other machines use this same password. 


## Recommendation(s)
The assessment team recommends disabling the built-in Administrator if business requirements allow for it. This account should only be used during initial setup and disaster recovery if possible. If disabling the account is not an option, its recommend to use a solution such as LAPS (Local Administrator Password Solution) or enroll in third-party solutions to randomize and manage bulk password management.

# Finding Metadata
### Finding Development
| Author Name | Twitter Handle | Email | Created | Updated |
|:-:|:-:|:-:|:-:|:-:|
| Alexander Rymdeko-Harvey | @Killswitch-GUI |  | 09/27/2017 | 09/27/2017 |

### Finding Sources
| URL | 
|:-:|
|  |
