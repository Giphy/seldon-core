# GIPHY Seldon Router

## Build and push the image

```bash
    $ docker build -t giphy_router .
    $ aws ecr get-login --no-include-email
    $ docker tag giphy_router:latest 134757864544.dkr.ecr.us-east-1.amazonaws.com/$ seldon-core:giphy_router_1.17.1
    $ docker push 134757864544.dkr.ecr.us-east-1.amazonaws.com/seldon-core:giphy_router_1.17.1
```
