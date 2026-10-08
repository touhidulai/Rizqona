# Deployment Plan

## Azure Container Registry

1. Create Resource Group

```bash
az group create --name rizqona-rg --location southeastasia
```

2. Then, Proceed to create the Container Registry

```bash
az acr create --resource-group rizqona-rg --name rizqonaregistry --sku Basic
```

3. Enabled Admin Access on Registry

```bash
az acr update --name rizqonaregistry --admin-enabled true
```

## Docker

1. Writing the Dockerfile and add the .dockerignore. 
2. Running the docker build command as follows -
```bash
docker build -t rizqona:latest .
```
3. After the image is built, now Tagging the Microsoft Azure Container Registry Link: 

```bash
docker tag rizqona:latest rizqonaregistry.azurecr.io/rizqona:latest
```

4. Docker Push to Registry matching Azure Server Chip

- My Mac has created Docker Image by default based on ARM Chip, so during Deployment, it failed due to Chip MisMatch. So, Edited accordingly. 

```bash
docker buildx build --platform linux/amd64 -t rizqonaregistry.azurecr.io/rizqona:latest --push .
```

## Azure Container App

1. Created a Environment for the container app. 

```bash
az containerapp env create \
  --name rizqona-env \
  --resource-group rizqona-rg \
  --location southeastasia
```

2. Deploying the Container 

```bash
az containerapp create \
  --name rizqona-api \
  --resource-group rizqona-rg \
  --environment rizqona-env \
  --image rizqonaregistry.azurecr.io/rizqona:latest \
  --registry-server rizqonaregistry.azurecr.io \
  --registry-username rizqonaregistry \
  --registry-password my_PASSWORD \
  --target-port 8000 \
  --ingress external \
  --min-replicas 0 \
  --max-replicas 1 \
  --env-vars \
    DB_HOST=my_neon_host \
    DB_PORT=5432 \
    DB_NAME=neondb \
    DB_USER=neondb_owner \
    DB_PASS=my_neon_password \
    DB_SSLMODE=require \
    SECRET_KEY=my_secret_key
```

## Neon Database 

1. SSL is required for Neon, so adjusted accordingly for local Postgres.
2. Used Neon to minimize costing. 

_Deployed and live on this link_