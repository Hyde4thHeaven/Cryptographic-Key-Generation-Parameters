## Welcome to 5th episode of my series **Code for Security**.  

<div align="center"> <img src="cover.png"/> </div>  
  
When generating cryptographic keys (or key pairs), it is important to use strong parameters. Key length, for instance, should provides enough entropy against brute-force attacks.

For RSA and DSA algorithms key size should be at least 2048 bits long
For ECC (elliptic curve cryptography) algorithms key size should be at least 224 bits long
For RSA public key exponent should be at least 65537.
This rule raises an issue when an RSA, DSA or ECC key-pair generator is initialized using weak parameters.

It supports the following libraries:

cryptography
PyCrypto
Cryptodome
### Noncompliant Code Example
> from cryptography.hazmat.primitives.asymmetric import rsa, ec, dsa  
>    
> dsa.generate_private_key(key_size=1024, backend=backend) # Noncompliant  
> rsa.generate_private_key(public_exponent=999, key_size=2048, backend=backend) # Noncompliant  
> ec.generate_private_key(curve=ec.SECT163R2, backend=backend)  # Noncompliant  
    
## Solution
> from cryptography.hazmat.primitives.asymmetric import rsa, ec, dsa  
>   
> dsa.generate_private_key(key_size=2048, backend=backend) # Compliant  
> rsa.generate_private_key(public_exponent=65537, key_size=2048, backend=backend) # Compliant  
> ec.generate_private_key(curve=ec.SECT409R1, backend=backend) # Compliant   
   
**Another secure function is done!** Secured coding is just a flipped hand when you know the hint!

Let's hunt more vulnerable code to make **Code for Security** next episode. Stay tuned!  
  
**#generate_private_key() #Code4Sec**  
  
Credit/Ref:  
[Python static code analysis](https://rules.sonarsource.com/python/RSPEC-4426)
[OWASP Top 10 2017 Category A3](https://owasp.org/www-project-top-ten/2017/A3_2017-Sensitive_Data_Exposure.html) - Sensitive Data Exposure
[OWASP Top 10 2017 Category A6](https://owasp.org/www-project-top-ten/2017/A6_2017-Security_Misconfiguration.html) - Security Misconfiguration
[ANSSI RGSv2](https://www.ssi.gouv.fr/uploads/2014/11/RGS_v-2-0_B1.pdf) - Référentiel Général de Sécurité version 2
[NIST FIPS 186-4](https://nvlpubs.nist.gov/nistpubs/FIPS/NIST.FIPS.186-4.pdf) - Digital Signature Standard (DSS)
[MITRE, CWE-326](https://cwe.mitre.org/data/definitions/326.html) - Inadequate Encryption Strength
  
______________________________
<table border="0">
 <tr>
   <td> <h3><i>Although my profile picture is quiet, but the real me can make some noise.</i></h3>
      <hr>
      <b><font color="Blue"> Author: Vuttawat Uyanont </font></b>  <br>
      <font color="grey"><i>Sexiest former engineer & banker who interested in Tech, Sake, and Beer.</i></font>  <br>
      <b>Studying:</b> Master Computer Science in Cybersecurity Management at Mahanakorn University.  <br> </td>  
   <td><img src="Author.png" width="150"/></td>  
 </tr>
</table>
  
