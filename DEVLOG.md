# Rizqona DEVLOG

## Sprint 2 - Restaurant Owner Auth

**What is Built**
This sprint is used to authenticate users especially the vendor side. The scope was limited to a particular well-defined scope to be implementable within the timeframe. Finally, the FastAPI documentation is used to verify the authentications

**Things that I fixed it:**
- bcrypt returns bytes, not string. Stored as hex in PostgreSQL. Fixed by adding .decode('utf-8') to hash_password.
- password VARCHAR(100) too short for bcrypt hash. Fixed with ALTER TABLE to VARCHAR(255).

**Decisions I made:**
- No email verification in Sprint 2 — keep it simple, add later.

**What I learned:**
- How to implement the basic authentication. Like using SQL to create database table with column constraints. Then, Hashing Password, and finally connecting the endpoint with the protection through JWT Token. 

__End of Sprint 2__

## Sprint 3 - Docker & Deployment

**What is Built**
Setup Microsoft Azure. Created Resource + Container Registry. Dockerized my project. Pushed to Azure Container Registry and deployed using Azure Container App. 

**Things that I fixed it:**
- Mac ARM & Azure Server Linux/AMD Chip Mismatch. Used --platform to enabled Azure Server based Docker image. 
- Failed Deployment with Mac ARM was cached so new edited Image couldn't get build. Delete cached container app. 
- Azure Container App failed without Registry admin access. So, enabled access, got the password and used it accordingly. 

**Decisions I made:**
- This Sprint is only limited to Deployment. Getting around with Azure, Neon and Docker. 

**What I learned:**
- From writing DockerFile to Azure Registry to Deployment in Microsoft Azure with Live Link Enabled. 

__End of Sprint 3__