from cryptography.hazmat.primitives.asymmetric import rsa, ec, dsa

dsa.generate_private_key(key_size=1024, backend=hyde_backend())  # Noncompliant
rsa.generate_private_key(public_exponent=999, key_size=2048, backend=hyde_backend())  # Noncompliant
ec.generate_private_key(curve=ec.SECT163R2, backend=hyde_backend())  # Noncompliant

