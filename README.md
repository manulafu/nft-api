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

Access to the application by accessing http://localhost:8000/ to start using the api

##### Main endpoints

- **GET:** _/nft-api/v1/NFT/all/_ - get all nfts
- **GET:** _/nft-api/v1/NFT/id/_ - get single nft but 'asset_id'
- **GET:** _/nft-api/v1/collection/all/_ - get all collections
- **GET:** _/nft-api/v1/collection/all/_ - get single collection based on 'uuid'
- **POST:** _/nft-api/v1/NFT/all/_ - create nft
