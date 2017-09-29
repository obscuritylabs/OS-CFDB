

# Finding Details 

## Title
  Spear Phishing Weaknesses
## SVR
  3
## CVSS
  4.0 – 5.9
## Risk
  Medium
## Service
  * Internal Penetration Testing
  * External Penetration Testing 
## NIST 800-53 
  * SC-7
  * SI-3
## Refrences
  * https://www.us-cert.gov/report-phishing
  
# Technical Information

## Description 
The assessment team was able to spear phish successfully the in-scope organization; this requires an attacker's email to pass through the network border. Phishing commonly requires the email to make it through NSM (Network Security Monitoring) appliances and require user interaction to execute the payload. Most common phishing attacks can be mitigated by string border and host level automated protections. In some cases, inadequate host protections allow for execution of malicious payloads. 

## Impact
When a phishing email can subvert NSM and AESP (Advanced Endpoint Security Protection), an attacker can gain code execution on the target. Execution could lead to full system compromise and post-exploitation activities.

## Recommendation(s)
Regularly analyze border and host-level protections, including spam-filtering capabilities, to ensure their continued effectiveness in blocking the delivery and execution of malware. Build custom IOC's (Indicators of Compromise) to mitigate APT (Advanced Persistent Threats) and known techniques. 

# Finding Metadata
  * Author(s)
    * Alexander Rymdeko-Harvey (@Killswitch-GUI)
  * Source(s)
  * Created
    * 09/27/2017
  * Updated
    * 09/27/2017k 
