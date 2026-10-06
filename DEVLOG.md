#Rizqona DEVLOG

##Sprint 2 - Restaurant Owner Auth
**Date:** 07 October, 2026

**What is Built**
This sprint is used to authenticate users especially the vendor side. The scope was limited to a particular well-defined scope to be implementable within the timeframe. Finally, the FastAPI documentation is used to verify the authentications

**What broke and how I fixed it:**
- bcrypt returns bytes, not string. Stored as hex in PostgreSQL. Fixed by adding .decode('utf-8') to hash_password.
- password VARCHAR(100) too short for bcrypt hash. Fixed with ALTER TABLE to VARCHAR(255).

**Decisions I made:**
- No email verification in Sprint 2 — keep it simple, add later.

**What I learned:**
- How to implement the basic authentication. Like using SQL to create database table with column constraints. Then, Hashing Password, and finally connecting the endpoint with the protection through JWT Token. 

