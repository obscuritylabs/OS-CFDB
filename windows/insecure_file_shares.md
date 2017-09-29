# Finding Details 

## Title
  Insecure File Shares
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
  * SI-2, 
  * AC-1
  * AC-3
  * AC-6
 ## Refrences
  * https://technet.microsoft.com/en-us/library/cc754178(v=ws.11).aspx
  * https://technet.microsoft.com/en-us/library/cc772184(v=ws.11).aspx
  
# Technical Information

## Description 
Windows File Shares using NTFS (New Technology File System) allows for granular control over RWX (Read, Write, Execute) down to specific files. Sensitive data related to business functions and personnel often are stored in centralized locations for ease of access. When non-elevated / privileged domain users can access sensitive data, it allows for an attacker to easily exfil or facilitate future attack paths. 

## Impact
This insecure storage misconfiguration leaves data open to theft by an attacker and could cause substantial damage to the organization and its employees. Insecure file shares can also lead to loss of data integrity and malicious code to target HVI (High-Value Individuals) 

## Recommendation(s)
The assessment team recommends following the model of least privileged. Implement a secure configuration by using NTFS Share Permissions and restricting Domain Users and Groups to sensitive data.

# Finding Metadata
  * Author(s)
    * Alexander Rymdeko-Harvey (@Killswitch-GUI)
  * Source(s)
  * Created
    * 09/27/2017
  * Updated
    * 09/27/2017
