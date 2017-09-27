

# Finding Details 

## Title
  SMB Signing Disabled
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
  * https://pen-testing.sans.org/blog/2013/04/25/smb-relay-demystified-and-ntlmv2-pwnage-with-python
  * https://support.microsoft.com/en-us/help/161372/how-to-enable-smb-signing-in-windows-nt
  * https://blogs.technet.microsoft.com/josebda/2010/12/01/the-basics-of-smb-signing-covering-both-smb1-and-smb2/
  * https://msdn.microsoft.com/en-us/library/windows/desktop/aa378749(v=vs.85).aspx
 
# Technical Information

## Description 
Server Message Block (SMB) is the file protocol most commonly used by Windows. This protocol allows communication for network file sharing or accessing remote resources of a server. SMB singing specifically is supported on all versions of SMB (1,2,3) but only enabled on Domain Controllers by default. This security feature allows the protocol to ensure authenticity at the packet level.


## Impact
If an attacker gains access to the LAN (Local Area Network) they will be able to send specifically crafted packets using LLMNR spoofing to direct network share access quires to the attacker. Using this MITM (Man-In-The-Middle) attack they will be able to capture NTLM and NTLMv2 (Windows Challenge/Response Protocol) credentials and potentially brute force these to gain access to recourses on the network. 



## Recommendation(s)
It is recommended that SMB singing is enabled via GPO policy or via registry for the SDA Campus Network. If this is not possible due to business constraints core servers and resources should enable SMB signing to prevent GPO tampering or credential compromise of high value accounts.  

# Finding Metadata
  * Author(s)
    * Alexander Rymdeko-Harvey (@Killswitch-GUI)
  * Source(s)
  * Created
    * 09/27/2017
  * Updated
    * 09/27/2017
