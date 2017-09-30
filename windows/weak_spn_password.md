
# Finding Details 

## Title
  Weak SPN Password 
## SVR
  5
## CVSS
  8.0 – 10.0
## Risk
  Critical
## Service
  * Internal Penetration Testing
  * External Penetration Testing 
## NIST 800-53 
  * 
## Refrences
  * https://adsecurity.org/?p=2011
  * https://msdn.microsoft.com/en-us/library/ms677949(v=vs.85).aspx
  * https://msdn.microsoft.com/en-us/library/windows/desktop/ms684272(v=vs.85).aspx
  * https://blog.netspi.com/faster-domain-escalation-using-ldap/
  * https://docs.microsoft.com/en-us/windows-server/security/group-managed-service-accounts/what-s-new-for-managed-service-accounts
 
# Technical Information

## Description 
Service Principal Names (SPNs) are a Microsoft way of designating and identifying where services are running in a domain. These SPNs are attached to accounts within active directory. Any Domain User has the ability to lookup these attributes and request access to the service they provide. The Active Directory Domain Controller issues the requesting user access to the service a Kerberos ticket. This ticket includes the encrypted and hashed password for the user of the service. Microsofts Kerberos implementation does this to allow access to the requested resource even if the client does not have the account name

## Impact
If an attacker gains access to any user within the domain, they can start to request SPNs service tickets for all requested services within the domain. Once these tickets are collected, and they are running under standard user, the attacker can attempt to crack the passwords using the Kerberos 5 TGS-REP standard. If a ticket is cracked, the attacker can then access the service or utilize that password to further their access within the domain impersonating that service account. 

## Recommendation(s)
The assessment team recommends removing SPNs and migrating to Managed Service Accounts (MSAs). MAS is designed to provide services and tasks such as Windows services to share their domain accounts while eliminating the need for an administrator to administer passwords for these accounts manually. It is a managed domain account that provides automatic password management. If business requirements do not allow for MSA migration, guarantee all service accounts use the proper password complexity. Changing passwords of affected accounts to applicable industry best practices and company-defined requirements. 


# Finding Metadata
### Finding Development
| Author Name | Twitter Handle | Email | Created | Updated |
|:-:|:-:|:-:|:-:|:-:|
| Alexander Rymdeko-Harvey | @Killswitch-GUI |  | 09/27/2017 | 09/27/2017 |
| Rob Fuller | Rob Fuller |  | 09/27/2017 | 09/27/2017 |

### Finding Sources
| URL | 
|:-:|
| https://github.com/mubix/cfdb/blob/master/Windows/Weak_SPN_Password.md |
