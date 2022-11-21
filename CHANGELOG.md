# Changelog

All notable changes to this project will be documented in this file.

The format is inspired by [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

Overarching Tractus-X releases are tested to the best of our knowledge. Test are performed on specific runtime
configurations, which is documented per release.

Tractus-X is sponsored by catena-X. For more information visit [catena.x.net](https://catena-x.net/).

## [2.0.0.RC1]

Disclaimer: This is a test / demo release candidate only. 

### Added
- Portal, v0.5.4
- Golden Record Business Partner Number (BPN) Service, v2.0.0
- Managed Identity Wallet, v0.5.2
- Dynamic Attribute Provisioning Service (DAPS), v1.7.1
- Digital Twin Registry, v0.2.0M2

### Known knowns
- FOSS components developed and pre-tested to TRL6 with artificial test data only
- No execution of Load-, Performance- or Penetration Tests
- No assignment of Export Control Classification Numbers (ECCN) to FOSS components
- GeoBlocking recommended for Operations (GBaaS)

### Runtime

- Tested on [Kubernetes](https://en.wikipedia.org/wiki/Kubernetes) versions: `1.22`
- Tested with [PostgreSQL](https://en.wikipedia.org/wiki/PostgreSQL) versions: `1.11`
