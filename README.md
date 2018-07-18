# website

## Docker on the Server
1. Pull the most recent version from git
2. `cd` into the `website` root directory
3. Build the docker image with `docker build -t schemes-image .`
4. Stop the currently running container `docker stop schemes-container`
5. Remove the old container `docker rm schemes-container`
6. Create and run the new image `docker run -d --name schemes-container -p 10020:80 schemes-image`
