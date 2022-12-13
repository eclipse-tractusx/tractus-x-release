# Changelog

All notable changes to this project will be documented in this file.

Overarching Tractus-X releases are tested to the best of our knowledge. Test are performed on specific runtime
configurations, which is documented per release.

Tractus-X is sponsored by catena-X. For more information visit [catena.x.net](https://catena-x.net/).

## [2.0.0] 13-Dec-2022

Disclaimer: This is a test / demo release candidate only. 

### Added
- [Portal (Registration)](https://github.com/eclipse-tractusx/portal-frontend-registration), v0.5.4 [unreleased]
- [Golden Record Business Partner Number (BPN) Service](https://github.com/eclipse-tractusx/bpdm), v2.0.0
- [Managed Identity Wallet](https://github.com/eclipse-tractusx/managed-identity-wallets), v0.5.2
- [Dynamic Attribute Provisioning Service (DAPS)](https://github.com/eclipse-tractusx/daps-helm-chart/), v1.7.1
- [Digital Twin Registry](https://github.com/eclipse-tractusx/sldt-digital-twin-registry), v0.2.0M2

### Known knowns
- FOSS components developed and pre-tested to TRL6 with artificial test data only
- No execution of Load-, Performance- or Penetration Tests
- No assignment of Export Control Classification Numbers (ECCN) to FOSS components
- GeoBlocking recommended for Operations (GBaaS)

### Runtime

- Tested on [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes) versions: `1.24.3`
- Tested with [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) versions: `1.11`
