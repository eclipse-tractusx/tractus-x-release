# Tractus-X release

This repository specifies details about overarching Tractus-X releases. It contains process definitions, as well as
runtime-environment basic requirements, technical implementations for testing and packaging release artifacts.

## Schedule

Tractus-X releases follow a quarterly schedule. In addition to the overarching quarterly release, single product
releases take place on demand. The overarching release is intended to ensure compatibility, quality standards and
alignment between Tractus-X products.

## Runtime-Environment

A Tractus-X releas require a Kubernetes Runtime-Environment in
a [supported Kubernetes version](https://kubernetes.io/releases/). As a recommendation run the latest Kubernetes version
-1.

Example:  
As of 1.11.2022 the following Kubernetes Versions are supported:

- 1.25
- 1.24
- 1.23

Recommended Kubernetes version in this case is 1.24.

## Process

The release process describes manual and automated steps, that are performed to create a release. A release consists of
at least one artifact, that can be used to deploy a Tractus-X application, or to be used as a dependency by other projects.

### Product release process

Tractus-X products are individually developed and therefore no strict workflow is enforced.
To ensure a consistent view on releases, the following aspects should still be met:

- [GitHub releases](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases) are used to
  publish artifacts. Git tags are added accordingly (usually done automatically)
- A CHANGELOG.md file, that follows [keep a changelog](https://keepachangelog.com/en/1.0.0/) recommendations is
  maintained and updated with descriptions for the current release. Links to GitHub external artifacts
  (i.e. mvncentral or Docker Hub) are referenced

### Overarching release process

Overarching Tractus-X releases are initiated and coordinated by a release management group. This group is working with
already released versions of Tractus-X products to form the overarching release.

__TL;DR__

- Identify individual product version, that should be included in the overarching release
- Verify that products work well together, by deploying and testing on dedicated infrastructure
- Collect released product artifacts
- Create overarching release artifact package
- Update overarching release [CHANGELOG](CHANGELOG.md)

To verify, the released products work together correctly, integration- and end-to-end tests are performed.
These test include deploying the products to a dedicated runtime environment, using the provided Helm charts and
installation instructions.

If all tests are successful, the individual product release artifacts are collected and re-packaged to a combined,
overarching release artifact. This single artifact is afterwards published with a pe-defined version number as GitHub
release.

As last step, the release is documented in the [CHANGELOG](CHANGELOG.md)

## Artifacts

Tractus-X products are released in multiple formats. The number of artifacts and its format varies between
individual product and the overarching releases.

### Product release artifacts

The following sections describe some common formats of release artifacts used by Tractus-X products.

#### Sourcecode

Most Tractus-X products are software products. In these cases, packaging the sourcecode together with a list of used
dependencies is a good starting point and should be included as artifact of a release in almost any case.

#### Container images

`tbd`

#### Helm charts

Applications developed in the Tractus-X context typically provide a [Helm chart](https://helm.sh/) for easy deployment
on [kubernetes](https://kubernetes.io/).

To add a Helm chart as a release artifact it has to be packaged. There are multiple tools, that help packaging charts.
We recommend using the [chart-releaser-action](https://github.com/helm/chart-releaser-action) GitHub action since
together with activated [GitHub pages](https://pages.github.com/), it can transform your repository to function as Helm
chart repository on its own.

Additionally, Tractus-X offers a central Helm chart repository. It supports two channels for released
Helm charts - `dev` and `stable`.

The `dev`-channel is used to publish the most recently released charts. It is updated nightly and automatically pulls in
the latest chart releases of the [eclipse-tractusx](https://github.com/eclipse-tractusx) GitHub organization.

The `stable` channel is used by the release management group, to publish all Helm charts, that were successfully
tested and included in an overarching release. This means, that the stable channel only includes specific versions
of product charts, that are tested to the best of our knowledge to work together with other stable charts.

## Patching strategy

`tbd`
