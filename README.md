# Trip Reports

## Local Development

1. Install [Docker](https://docs.docker.com/get-docker/).

2. Run:

   ```
   docker compose up
   ```

### Developing inside a container


## Notes

### Developing inside a container

Launch or attach to a running container to develop within it and take advantage of the full environment (ex. installed dependencies).

See https://code.visualstudio.com/docs/devcontainers/containers.

tl;dr: `Cmd + Shift + P` -> Attach to running container

### Resources

#### Maps

* [Polyline algorithm](https://developers.google.com/maps/documentation/utilities/polylinealgorithm)

#### Google Cloud

* [Setting up Cloud Run for a Python service](https://cloud.google.com/run/docs/quickstarts/build-and-deploy/deploy-python-service)
* [Django & Cloud Run tutorial](https://cloud.google.com/python/django/run)
   * Includes Secret Manager, CloudSQL
* `GS_DEFAULT_ACL = 'publicRead'` is not compatible with [Uniform Bucket Level Access](https://cloud.google.com/storage/docs/uniform-bucket-level-access). Fails with "Cannot insert legacy ACL for an object when uniform bucket-level access is enabled."
* Cloud Build service account is no longer used as the default. See https://cloud.google.com/build/docs/cloud-build-service-account-updates.
