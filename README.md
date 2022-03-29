# NFT Api project

### Tu run the project follow the next steps

#### Clone the project to your machine and change directory to it

```bash
git clone https://github.com/manulafu/nft-api.git
```

```bash
cd nft-api
```

#### Build the docker container

```bash
docker build --tag nft-api
```

#### Run the application image

```bash
docker run -p 8000:8000  --rm nft-api
```

Access to the application by accessing http://localhost:8000/
