# dash-in-docker

![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Redis](https://img.shields.io/badge/redis-%23DD0031.svg?style=for-the-badge&logo=redis&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-%233F4F75.svg?style=for-the-badge&logo=plotly&logoColor=white)

Consolidating my docker learnings with a Plotly Dash App which uses Redis for caching and storage and Nginx for serving
frontend.

### Running the app locally

```docker
docker-compose -f docker-compose.dev.yml up -d
```

Once the above command runs successfully, you'll be able to access the app at http://localhost:3000.

You can bring down this setup with the following command:

```docker
docker-compose -f docker-compose.dev.yml down
```

Once done with the development, image can be created using:

```docker
docker-compose -f docker-compose.dev.yml build
```

1. Update the version in pyproject.toml file of the project.
2. Rename the built image to correct format for pushing to docker hub

```docker
docker tag dash-in-docker_dash-docker snehilvj/dash-docker:<version>
docker push snehilvj/dash-docker:<version>
```

The image will be available [here](https://hub.docker.com/r/snehilvj/dash-docker).
### Running the app in production

In order to run the setup in production, use the image just pushed to dockerhub (configured in
docker-compose.prod.yml).

```docker
docker-compose -f docker-compose.prod.yml up -d
```
