# Helm Repository for Tractus-X

To have all Tractus-X sub-product Helm Charts in one place, a central Tractus-X Helm Repository is build. The central
Helm Repository is split into two branches:

- Dev
- Stable

## Helm Repository URL

Both branches will be hosted via GitHub Pages within this
repository ([eclipse-tractus-x/tractus-x-release](https://github.com/eclipse-tractusx/tractus-x-release)) and will be
accessible under URL

- https://eclipse-tractusx.github.io/tractus-x-release/charts/dev for Dev branch
- https://eclipse-tractusx.github.io/tractus-x-release/charts/stable for Stable branch

## Availability

### Dev Branch

Dev branch will contain all released Helm Charts of any Tractus-X sub-product. In the future, only a certain number
of released Helm charts per Tractus-X sub-product might be kept due to clarity reasons.

The Helm repository for Dev branch will be updated once a day.

### Stable branch

Stable branch will contain all Helm charts versions of Tractus-X sub-products associated with an official Tractus-X
release. In the future, Helm charts associated with Tractus-X versions which have reached its end of lifetime, will be
removed from the stable branch.

The Helm repository for stable branch will be updated when a new Tractus-X release or a patch update is released.

## Usage

### Dev Branch

```shell
$ helm repo add tractusx-dev https://eclipse-tractusx.github.io/tractus-x-release/charts/dev
$ helm install my-release tractusx-dev/sub-product-name
```

### Stable Branch

```shell
$ helm repo add tractusx https://eclipse-tractusx.github.io/tractus-x-release/charts/stable
$ helm install my-release tractusx/sub-product-name
```
