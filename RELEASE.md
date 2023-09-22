# Tractus-X release process

This repository specifies details about overarching Tractus-X releases. It contains process definitions, as well as technical implementations for testing and packaging release artifacts.

## Process

The release process describes manual and automated steps, that are performed to create a release. A release consists of at least one artifact, that can be used to deploy your application, or to be used as a dependency by other projects.

### Product release process

Tractus-X products are individually developed and therefore no strict workflow is enforced. To ensure a consistent view on releases, the following aspects should still be met:

- A CHANGELOG.md file, that follows [keep a changelog](https://keepachangelog.com/en/1.0.0/) recommendations is maintained and updated with descriptions for the current release. Links to GitHub external artifacts (i.e. mvncentral or Docker Hub) are referenced
- [GitHub releases](https://docs.github.com/en/repositories/releasing-projects-on-github/managing-releases-in-a-repository) are used to publish artifacts. Git tags are added accordingly (usually done automatically)
- The changelog content of the current release is documented in the GitHub release
- Helm charts are released into the aligned helm chart repository

### Overarching Release Process

The overarching Tractus-X releases are coordinated by the release managment group (refer to sig-release). This team collaborates with the currently released versions of Tractus-X products to formulate the overarching release.

#### Pre-requisits

- __!!!__ If the last release, approved by the Eclipse Foundation, is more than a year old, you have to initiate a new release on the [Eclipse Tractus-X Project page](https://projects.eclipse.org/projects/automotive.tractusx) at least a week prior to the planned release date (see the [Release steps](#release-steps))
- Helm chart versions and app versions for all products intended for the release
- An official announcement text highlightning release features, vitual for the announcement email
- An optional official announcement image usable for the Eclipse Tractus-X Project page

#### Release Steps

- Verify the presence of all helm chart versions in the release helm repository
- Verify all referenced links are working (documentation, kits, etc.)
- Create a Pull Request with the new changelog entry
- Gather feedback and proceed with the merge
- Create a GitHub release and incorporate the new changelog entry
- Insert the new changelog entry under versions on the [eclipse-tractusx changelog page](https://eclipse-tractusx.github.io/CHANGELOG/)
- Register a new Tractus-X Release on the [Eclipse Tractus-X Project page](https://projects.eclipse.org/projects/automotive.tractusx) (Navigate to the Create new release button/link on the right side)
- Modify the Download section on the [Eclipse Tractus-X Project page](https://projects.eclipse.org/projects/automotive.tractusx) via the Downloads, Software Repositories, and Marketplace -> Downloads Message section
- Compose an email to the [tractusx-dev mailinglist](mailto:tractusx-dev@eclipse.org) announcing the new release
- Example:

```
Subject line: [tractusx-dev] Announcing Tractus-X 23.09 - Latest Release Now Available 🎉

Hello Tractus-X Community,
 
We're excited to announce the latest release of Tractus-X, now versioned as 23.09 in line with our transition from Semantic Versioning (SemVer) to Calendar Versioning (CalVer).
 
🔗 Release and Helm Charts
You can view the full changelog and Helm chart versions for each component here: Tractus-X 23.09 Release Notes.
 
🗓️ Transition to CalVer
We've transitioned our versioning strategy to CalVer to better reflect the release timing and to simplify version identification. Going forward, expect the version number to represent the release date in a YY.0M.MICRO format.
 
🙏 Acknowledgments
We'd like to thank all contributors, users, and community members who have played a role in this release. Your feedback, contributions, and ongoing support fuel the advancement of this project.
 
💬 We Value Your Feedback
We invite you to test out the new suite release and share your experiences with us. If you encounter any issues or have suggestions for future improvements, please submit them on our GitHub repository.
 
Thank you for your continued support and enthusiasm for the Tractus-X project. Together, we're driving the future of the ecosystem.
 
Best regards,
 
Bjoern, Daniel and Sigi
Eclipse Tratcus-X Project Leads
```

## Artifacts

Tractus-X products are released in multiple formats. The number of artifacts and its format varies between individual product and the overarching releases.

### Product release artifacts

The following sections describe some common formats of release artifacts used by Tractus-X products.

#### Sourcecode

Most Tractus-X products are software products. In these cases, packaging the sourcecode together with a list of used dependencies is a good starting point and should be included as artifact of a release in almost any case.

#### Container images

All container images provided by tractus-x are only provided for development, testing etc. without any guarantee on license or security.

Feel free to use them on your own risk, all images can be build by yourself through provided Dockerfiles.

#### Helm charts

Applications developed in the Tractus-X context typically provide a [Helm chart](https://helm.sh/) for easy deployment on [kubernetes](https://kubernetes.io/).

To add a Helm chart as a release artifact it has to be packaged. There are multiple tools, that help packaging charts. We recommend using the chart-releaser-action GitHub action though, since together with activated [GitHub pages](https://pages.github.com/), it can transform your repository to function as Helm chart repository on its own.

Additionally, Tractus-X offers a central Helm chart repository. It supports two channels for released Helm charts - `dev` and `stable`.

The `dev`-channel is used to publish the most recently released charts. It is updated nightly and automatically pulls in the latest chart releases of the [eclipse-tractusx](https://github.com/eclipse-tractusx) GitHub organization.

The `stable` channel is used by the releaese management group, to publish all helm charts, that were successfully tested and included in an overarching release. This means, that the stable channel only includes specifc versions of product charts, that are tested to the best of our knowledge to work together with other stable charts.

## Patching strategy

`tbd`

## Helm Repository

For information about using the Tractus-X Helm repository, please refer to the [charts](https://github.com/eclipse-tractusx/charts) repository.