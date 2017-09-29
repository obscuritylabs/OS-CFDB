

# Finding Details 

## Title
  Insecure Credential Storage 
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
    * SI-13
    
## Refrences
  * https://www.sans.org/reading-room/whitepapers/authentication/clear-text-password-risk-assessment-documentation-113
  
# Technical Information

## Description 
The assessment team discovered storage of high-value accounts in a clear text format. Storing credentials of this nature in clear text is a severe security risk, allowing an attacker to gain access to credentials with ease. While allowing an attacker to use these credentials to compromise applications or systems of interest under the user context of the affected account. 

## Impact
Insecure credentials allow an attacker to Impersonate a legitimate user, breaking the authenticity of the system logging. Compromise of the host system could lead to malicious commands and actions to go unnoticed due to the privilege level of the account. 

## Recommendation(s)
Implement a review process for files and systems to look for cleartext account credentials. Secure all passwords with a centralized or independent password manager that meets business requirements.

# Finding Metadata
  * Author(s)
    * Alexander Rymdeko-Harvey (@Killswitch-GUI)
  * Source(s)
  * Created
    * 09/27/2017
  * Updated
    * 09/27/2017
