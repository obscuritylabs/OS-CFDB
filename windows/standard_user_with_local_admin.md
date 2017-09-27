
# Finding Details 

## Name
  Standard User with Local Admin 
## SVR
  3
## CVSS
  4.0-5.9
## Risk
  Medium
## Service
  * Internal Penetration Testing
  * External Penetration Testing 
 
# Technical Information

## Description 
Following the least privileged model, standard users should have only enough rights to perform their task or duty. It was discovered this user granted the group permissions of “Administrator”, this resulted in the ability for the team to use a User Access Control (UAC) bypass to gain full SYSTEM privileges of the host.  

## Impact
Over delegation of Local Admin rights to a “Standard” user account can result in unwanted or unauthorized software and unnecessary system access. If a system is compromised in a “Standard” user context, an attacker can use local administrator privileges to  gain access to cached credentials, install persistence, or preform post exploitation attacks to further their access.  

# Recommendation(s)
It is recommended that the least privileged model is followed when assessing if users should have the local “Administrator” windows group permission. In many cases this privilege can be obtained on a case-by-case basis for certain administrator functions. One method of employing this is using credential check out systems, or assigning that user a secondary account for administrator functions. This will reduce the overall attack surface of running at that privilege level for day-to-day tasks. 
