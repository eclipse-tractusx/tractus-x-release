# Helm Repository for Tractus-X

To have all Tractus-X sub-product Helm Charts in one place, two central Tractus-X Helm Repositories are built:

- Dev
- Stable

## Helm Repository URL

Both repositories will be hosted via GitHub Pages within this
repository ([eclipse-tractus-x/tractus-x-release](https://github.com/eclipse-tractusx/tractus-x-release)) and will be
accessible under URL

- https://eclipse-tractusx.github.io/tractus-x-release/charts/dev
- https://eclipse-tractusx.github.io/tractus-x-release/charts/stable

## Availability

### Dev Repository

Dev repository contains all released Helm Charts of any Tractus-X sub-product. Only a certain number of released Helm charts
per Tractus-X sub-product might be kept due to clarity reasons.

The Helm repository for Dev will be updated once a day.

### Stable Repository

Stable repository contains all Helm charts versions of Tractus-X sub-products associated with an official Tractus-X release.
In the future, Helm charts associated with Tractus-X versions which have reached its end of lifetime, will be removed
from the stable repository.

The Helm repository for stable will be updated when a new Tractus-X release or a patch update is released.

## Usage

### Dev Repository

```shell
$ helm repo add tractusx-dev https://eclipse-tractusx.github.io/tractus-x-release/charts/dev
$ helm search repo tractusx-dev/portal
NAME                    CHART VERSION   APP VERSION     DESCRIPTION                            
tractusx-dev/portal         0.8.0           0.8.0           Helm chart for Catena-X Portal frontend
tractusx-dev/portal-backend 0.8.0           0.8.0           Helm chart for Catena-X Portal backend
$
```

### Stable Repository

```shell
$ helm repo add tractusx https://eclipse-tractusx.github.io/tractus-x-release/charts/stable
$ helm search repo tractusx-dev/portal
NAME                    CHART VERSION   APP VERSION     DESCRIPTION                            
tractusx-dev/portal         0.8.0           0.8.0           Helm chart for Catena-X Portal frontend
tractusx-dev/portal-backend 0.8.0           0.8.0           Helm chart for Catena-X Portal backend
$
```
