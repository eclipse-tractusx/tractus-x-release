# Changelog

All notable changes to this project will be documented in this file.

Overarching Tractus-X releases are tested to the best of our knowledge. Tests are performed on specific runtime
configurations, which is documented per release.

Tractus-X is sponsored by catena-X. For more information visit [catena.x.net](https://catena-x.net/).
## Unreleased
- Portal (Registration), v0.5.4
- Managed Identity Wallet (MIW), v0.5.2

## [2.0.0] 13-Dec-2022

Disclaimer: This is a test / demo release candidate only. 

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
