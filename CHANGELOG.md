# Changelog

For background information visit [https://catena-x.net](https://catena-x.net).

All notable changes on overarching level will be documented in this file. Refer to component repositories for specific content, changelog and documentation.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/). Versions listed here refer to app versions.

Note: Versions listed in this log refer to the app version of the mentioned component, not the Helm Charts which install the app. Helm Charts
may have version numbers which differ from the app version.

## Unreleased
- [Portal (Registration)](https://github.com/eclipse-tractusx/portal-frontend-registration), v0.5.4
- [Managed Identity Wallet](https://github.com/eclipse-tractusx/managed-identity-wallets) (MIW), v0.5.2

## [2.0.0] 2022-12-14

### Added
- [Eclipse Data Space Connector (EDC)](https://github.com/eclipse-tractusx/tractusx-edc), v0.1.2
- [Golden Record Business Partner Number (BPN) Service](https://github.com/eclipse-tractusx/bpdm), v2.0.0
- [Dynamic Attribute Provisioning Service (DAPS)](https://github.com/eclipse-tractusx/daps-helm-chart/), v1.7.1
- [Digital Twin Registry](https://github.com/eclipse-tractusx/sldt-digital-twin-registry), v0.2.0M2

### Known knowns
- FOSS components developed and pre-tested to TRL6 with artificial test data only
- No execution of Load-, Performance- or Penetration Tests
- No assignment of Export Control Classification Numbers (ECCN) to FOSS components
- GeoBlocking recommended for Operations (GBaaS)
- Portal (Registration) as well as Managed Identity Wallet scope required for full functionality; yet both are unreleased 
  at this point in time and can be expected with Release 2.1.0
- Released HelmChart missing for EDC v0.1.2

### Runtime

- Tested on [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes) versions: `1.24.3`
- Tested with [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) versions: `1.11`
