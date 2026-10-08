# Rizqona DEVLOG

## Sprint 1 - Food Discovery 

**What is Built**
This sprint is used to built the models to define Restaurants, Menu Items. The local database connection is built with PostgreSQL. Furthermore, Restaurant repository is built to query the database. Finally, routes are built.  

**Things that I Fixed:**
- When querying a particular restaurant that doesn't exist, enabled HTTP Exception Error to handle that. 
- The routes were returning data in List. So, Handled it with RealDictCursor. 

**Decisions I made:**
- Only Food Discovery in Sprint 1 — keep it simple, add later.

**What I learned:**
- How to model something. Modelling Responses that limits what items we can return or not. How to handle credentials with .env and building connection to database using SQL. Finally, some- Basic CRUD Operations.  

__End of Sprint 1__

## Sprint 2 - Restaurant Owner Auth

**What is Built**
This sprint is used to authenticate users especially the vendor side. The scope was limited to a particular well-defined scope to be implementable within the timeframe. Finally, the FastAPI documentation is used to verify the authentications

**Things that I Fixed:**
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

**Things that I Fixed:**
- Mac ARM & Azure Server Linux/AMD Chip Mismatch. Used --platform to enabled Azure Server based Docker image. 
- Failed Deployment with Mac ARM was cached so new edited Image couldn't get build. Delete cached container app. 
- Azure Container App failed without Registry admin access. So, enabled access, got the password and used it accordingly. 

**Decisions I made:**
- This Sprint is only limited to Deployment. Getting around with Azure, Neon and Docker. 

**What I learned:**
- From writing DockerFile to Azure Registry to Deployment in Microsoft Azure with Live Link Enabled. 

__End of Sprint 3__

## Sprint 4 - Student Authentication

**What is Built**
Setup New Model for Students. Separate Repository for Restaurants, Students, Restaurant Owners. Validating Email Addresses for UM Student. Database Design for Student Login.

**Things that I Fixed:**
- Fixed Branch Management Issue like Requirements, Dockerfile and Notes were not in Sprint 4 branch but was on main branch. 
- Fixed Cache Issue in Docker. 
- Fixed Cache Issue in Azure Container App. Fixed it using relaunching the Container. 
- Found Flaw in Docker Naming. Using latest causes issue in Azure. Need unique codes/naming to make it work.  

**Decisions I made:**
-  Like, it needs to be end with "@siswa.um.edu.my" with PyDantic Field Validator.
- A Database Design Tradeoff - Product Design that a student can be at the same time a rider and also a user. Similarly, a student can open a restaurant in here so need two id. Furthermore, the issue with graduation. If a student graduates, can't login due to email would be invalid. 

**What I learned:**
- Docker and Azure Cache Fixing. Product and Database Design considering long term requirements. 

__End of Sprint 4__

## Sprint 5 - Event Logging

**What is Built**
Event Logging is built. Events tables is created in both local postgres and in Neon. Added log function to the routes to track logs for Future Recommendation Engine. 

**Things that I Fixed:**
- Old Database File (Repository.py) which containes all repo functions together has been separated to separate file. So CleanUps of the old file. 

**Decisions I made:**
- Primary decision is about design of the Database Table for Events Logs and its data inputs flows for. 
- Going for two tables or Single Table was a difficult decision. 

**What I learned:**
- How Each users activity is logged for recommendation engine. Each calls to the API creates a new row in the database with timestamps. Tracks users journey with their id. 

__End of Sprint 5__

## Sprint 6 - Search & Filter

**What is Built**
Basic Search & Filter is implemented. Both were implemented using SQL. 

**Things that I Fixed:**
- Initially used LIKE in SQL. However, found out that it is Type Strict. For Example- if the original word's first letter is capital, the search's first letter needs to be capital. So, changed LIKE to ILIKE. 

**Decisions I made:**
- Algorithm based Search is kept for future sprint when optimization is required as per user base.

**What I learned:**
-  Learned Path Paremeter vs Query Parameter

__End of Sprint 6__

