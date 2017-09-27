
# Finding Details 

## Title
  MsCacheV2 Misconfiguration 
## SVR
  4
## CVSS
  6.0 – 7.9
## Risk
  High
## Service
  * Internal Penetration Testing
  * External Penetration Testing 
## NIST 800-53 
  * CM-2
  * CM-6
  * IA-2
  * IA-3
## Refrences
  * https://technet.microsoft.com/en-us/library/jj852209.aspx
  * https://webstersprodigy.net/2014/02/03/mscash-hash-primer-for-pentesters/
  
# Technical Information

## Description 
MsCacheV2 is a Microsoft implementation of local password storage for domain users. This is implemented using the registry and the local SAM hive to secure the cached credentials. By default, Windows will cache up to 10 credentials locally and remove the oldest credential as they are populated to the host. It’s important to note that this is not only limited to local logons, but interactive logins as well. 

## Impact
If an attacker can gain elevated system privileges on a compromised host, the attacker could gather MsCachV2 credentials using a variety of toolsets. These hashes could then be potentially cracked using the PBKDF2 hashing algorithm, which uses the “Username” as the known salt value. This leaves these credentials to potentially be used for further lateral movement or compromise of internal domain systems.  

## Recommendation(s)
It is recommended that MsCacheV2 credential caching is limited to three accounts at any given time. If this is not possible due to business requirements, this acceptable number can be easily adjusted. One method of managing this would be setting this within the default GPO (Group Policy Objects). 

# Finding Metadata
  * Author(s)
    * Alexander Rymdeko-Harvey (@Killswitch-GUI)
  * Source(s)
  * Created
    * 09/27/2017
  * Updated
    * 09/27/2017
