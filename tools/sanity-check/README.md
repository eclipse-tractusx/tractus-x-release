# Capability

This tool can accomplish the following sanity checks for tables in a specified release of a Changelog

Link checks:

- KIT
  - Eclipse-Tractus-X Link
  - Github Changelog
- FOSS
  - release / repo link
  - chart link
  - release link in GitHub for apps of chart

Version checks (FOSS only):

- check that chart has been released
- check that helm repo version == given version
- check that app version is same for all apps of chart

**Out of scope**: Check inline links in the text.

# Usage

## Prerequisites

You need the following tools installed
- [python3 (I used python3.10)](https://www.python.org/downloads/)
- [venv](https://docs.python.org/3/library/venv.html)

Create a venv based on requirements.txt (note: you could also just install the requirements.txt but that is 
REALLY BAD PRACTICE).

```shell
pip install --upgrade virtualenv
# outputs where your virtualenv script lies or adds it to path
#  WARNING: The script virtualenv is installed in '/home/user/.local/bin' which is not on PATH.
#  Consider adding this directory to PATH or, if you prefer to suppress this warning, use --no-warn-script-location.

# add to path or just use path as above
path/to/virtualenv venv
# creates 'venv' folder

# activate venv
source venv/bin/activate
# shell is prefixed with '(venv)'

# install dependencies
pip install -r requirements.txt
```

## Actual usage

Run for a CHANGELOG.md and a release as follows:

```shell
cd tools/sanity-check

# enter venv (linux, see https://docs.python.org/3/library/venv.html#how-venvs-work)
source venv/bin/activate

# run command
python3 check.py ../CHANGLEOG.md 24.05
```

Sample outputs for a run for R24.03 close to R24.05. Please note that it fails for incorrect structure as it can not 
substring needed information correctly (trace-x chart name missing).

```
Found 8 releases
Extracting tables for release: 24.03
Release consists of 103 lines

Processing table 'Added'
Checking LINKS for KIT: Certificate Management KIT
Checking LINKS for KIT: Data Governance KIT
Checking LINKS for KIT: Environmental and Social Standards (ESS) KIT
Checking LINKS for KIT: Industry Core KIT
Checking LINKS for KIT: Manufacturing as a Service (MaaS) KIT
Checking LINKS for FOSS Component: PURIS
Checking CHART for FOSS Component: PURIS
  ERROR: Chart version of FOSS Chart puris has version 1.0.0 while version 2.6.0 is available in tractusx-dev
  ERROR: App version of FOSS Chart puris (app PURIS) has app version 1.0.0 while version 2.0.0 is set in Chart available in tractusx-dev


Processing table 'Updated'
Checking LINKS for KIT: Business Partner KIT
Checking LINKS for KIT: Connector KIT
Multiline APPs for FOSS Component Country Risk
Checking LINKS for FOSS Component: Country Risk
Checking CHART for FOSS Component: Country Risk
  ERROR: Chart version of FOSS Chart country-risk has version 3.0.11 while version 4.0.2 is available in tractusx-dev
  ERROR: App version of FOSS Chart country-risk (app Frontend) has app version 1.3.1 while version 2.0.0 is set in Chart available in tractusx-dev
  ERROR: App version of FOSS Chart country-risk (app Backend) has app version 1.3.1 while version 2.0.0 is set in Chart available in tractusx-dev
Checking LINKS for KIT: Demand and Capacity Management (DCM) KIT
Checking LINKS for FOSS Component: Digital Product Pass (DPP)
Checking CHART for FOSS Component: Digital Product Pass (DPP)
  ERROR: Chart version of FOSS Chart digital-product-pass has version 2.1.4 while version 3.0.0 is available in tractusx-dev
  ERROR: App version of FOSS Chart digital-product-pass (app Digital Product Pass (DPP)) has app version v2.1.3 while version 3.0.0 is set in Chart available in tractusx-dev
Checking LINKS for KIT: Digital Twin KIT
Checking LINKS for FOSS Component: Digital Twin Registry
Checking CHART for FOSS Component: Digital Twin Registry
  ERROR: Chart version of FOSS Chart digital-twin-registry has version 0.3.31 while version 0.4.11 is available in tractusx-dev
  ERROR: App version of FOSS Chart digital-twin-registry (app Digital Twin Registry) has app version v0.3.23 while version 0.4.3 is set in Chart available in tractusx-dev
Checking LINKS for FOSS Component: Discovery Finder
Checking CHART for FOSS Component: Discovery Finder
  ERROR: Chart version of FOSS Chart discoveryfinder has version 0.1.18 while version 0.2.5 is available in tractusx-dev
  ERROR: App version of FOSS Chart discoveryfinder (app Discovery Finder) has app version v0.2.7 while version 0.3.1 is set in Chart available in tractusx-dev
Checking LINKS for FOSS Component: Discovery Service (BPN Finder)
Checking CHART for FOSS Component: Discovery Service (BPN Finder)
  ERROR: Chart version of FOSS Chart bpndiscovery has version 0.1.18 while version 0.2.6 is available in tractusx-dev
  ERROR: App version of FOSS Chart bpndiscovery (app Discovery Service (BPN Finder)) has app version 0.2.8 while version 0.3.1 is set in Chart available in tractusx-dev
Checking LINKS for FOSS Component: Eclipse Data Space Connector (EDC)
Checking CHART for FOSS Component: Eclipse Data Space Connector (EDC)
  ERROR: Chart version of FOSS Chart tractusx-connector has version 0.5.4 while version 0.7.2 is available in tractusx-dev
  ERROR: App version of FOSS Chart tractusx-connector (app Eclipse Data Space Connector (EDC)) has app version 0.5.4 while version 0.7.2 is set in Chart available in tractusx-dev
Checking LINKS for KIT: Eco Pass KIT
Checking LINKS for FOSS Component: Golden Record Business Partner Number (BPN) Service
Checking CHART for FOSS Component: Golden Record Business Partner Number (BPN) Service
  ERROR: Chart version of FOSS Chart bpdm has version 4.0.2 while version 5.0.0 is available in tractusx-dev
  ERROR: App version of FOSS Chart bpdm (app Golden Record Business Partner Number (BPN) Service) has app version v5.0.0 while version 6.0.0 is set in Chart available in tractusx-dev
Checking LINKS for FOSS Component: Item Relationship Service (IRS)
Checking CHART for FOSS Component: Item Relationship Service (IRS)
  ERROR: Chart version of FOSS Chart irs-helm has version 6.14.1 while version 6.18.0 is available in tractusx-dev
  ERROR: App version of FOSS Chart irs-helm (app Item Relationship Service (IRS)) has app version 4.5.1 while version 4.9.0 is set in Chart available in tractusx-dev
Checking LINKS for FOSS Component: Knowledge Agents
Checking CHART for FOSS Component: Knowledge Agents
  ERROR: Chart version of FOSS Chart remoting-agent has version 1.11.16 while version 1.12.19 is available in tractusx-dev
  ERROR: App version of FOSS Chart remoting-agent (app Knowledge Agents) has app version 1.11.16 while version 1.12.19 is set in Chart available in tractusx-dev
Checking LINKS for KIT: Knowledge Agents KIT
Checking LINKS for FOSS Component: Managed Identity Wallet (MIW)
Checking CHART for FOSS Component: Managed Identity Wallet (MIW)
  ERROR: Chart version of FOSS Chart managed-identity-wallet has version 0.3.0 while version 0.4.0 is available in tractusx-dev
  ERROR: App version of FOSS Chart managed-identity-wallet (app Managed Identity Wallet (MIW)) has app version 0.3.0 while version 0.4.0 is set in Chart available in tractusx-dev
Checking LINKS for FOSS Component: Managed Service Orchestrator
Checking CHART for FOSS Component: Managed Service Orchestrator
  ERROR: Chart version of FOSS Chart managed-service-orchestrator has version 1.5.4 while version 1.5.8 is available in tractusx-dev
  ERROR: App version of FOSS Chart managed-service-orchestrator (app Managed Service Orchestrator) has app version v1.5.4 while version 1.5.5 is set in Chart available in tractusx-dev
Checking LINKS for KIT: OSim KIT
Checking LINKS for FOSS Component: Policy Hub
Checking CHART for FOSS Component: Policy Hub
  ERROR: Chart version of FOSS Chart policy-hub has version 0.1.0 while version 1.0.0 is available in tractusx-dev
  ERROR: App version of FOSS Chart policy-hub (app Policy Hub) has app version 0.1.0 while version 1.0.0 is set in Chart available in tractusx-dev
Multiline APPs for FOSS Component Portal
Checking LINKS for FOSS Component: Portal
Checking CHART for FOSS Component: Portal
  ERROR: Chart version of FOSS Chart portal has version 1.8.0 while version 1.8.1 is available in tractusx-dev
  ERROR: App version of FOSS Chart portal (app Registration) has app version 1.6.0 while version 1.8.1 is set in Chart available in tractusx-dev
  ERROR: App version of FOSS Chart portal (app Frontend) has app version 1.8.0 while version 1.8.1 is set in Chart available in tractusx-dev
  ERROR: App version of FOSS Chart portal (app Backend) has app version 1.8.0 while version 1.8.1 is set in Chart available in tractusx-dev
  ERROR: App version of FOSS Chart portal (app Assets) has app version 1.8.0 while version 1.8.1 is set in Chart available in tractusx-dev
Checking LINKS for KIT: Product Carbon Footprint (PCF) KIT
Checking LINKS for KIT: Quality KIT
Checking LINKS for FOSS Component: Self Description (SD) Factory
Checking CHART for FOSS Component: Self Description (SD) Factory
  ERROR: Chart version of FOSS Chart sdfactory has version 2.1.12 while version 2.1.19 is available in tractusx-dev
  ERROR: App version of FOSS Chart sdfactory (app Self Description (SD) Factory) has app version v2.1.10 while version 2.1.12 is set in Chart available in tractusx-dev
Multiline APPs for FOSS Component Simple Data Exchanger (SDE)
Checking LINKS for FOSS Component: Simple Data Exchanger (SDE)
Checking CHART for FOSS Component: Simple Data Exchanger (SDE)
  ERROR: Chart version of FOSS Chart sde has version 0.1.5 while version 0.1.8 is available in tractusx-dev
  ERROR: App version of FOSS Chart sde (app Frontend) has app version 2.3.6 while version 2.4.0 is set in Chart available in tractusx-dev
  ERROR: App version of FOSS Chart sde (app Backend) has app version 2.3.6 while version 2.4.0 is set in Chart available in tractusx-dev
Checking LINKS for FOSS Component: Semantic Hub
Checking CHART for FOSS Component: Semantic Hub
  ERROR: Chart version of FOSS Chart semantic-hub has version 0.1.35 while version 0.2.3 is available in tractusx-dev
  ERROR: App version of FOSS Chart semantic-hub (app Semantic Hub) has app version v0.2.16 while version 0.3.2 is set in Chart available in tractusx-dev
Checking LINKS for FOSS Component: Trace-X Traceability Application
Checking CHART for FOSS Component: Trace-X Traceability Application
  ERROR: Could not retrieve latest Helm chart or app version for [1.3.28](https.
  ERROR: Chart version of FOSS Chart [1.3.28](https has version 1.3.28 while version None is available in tractusx-dev
  ERROR: App version of FOSS Chart [1.3.28](https (app Trace-X Traceability Application) has app version 10.3.0 while version None is set in Chart available in tractusx-dev
Checking LINKS for KIT: Traceability KIT


Processing table 'Unchanged, untested'
Checking LINKS for KIT: Behavioral Twin: Health Indicators (HI) KIT
Checking LINKS for KIT: Behavioral Twin: Model and Data processing (MDP) KIT
Checking LINKS for KIT: Behavioral Twin: Remaining useful Life (RUL) KIT
Checking LINKS for KIT: Circularity KIT
Checking LINKS for KIT: Modular Production KIT
```

# DEPENDENCY update

You can check dependencies for python using eclipse dash tool as follows:

Download latest version of dash [here](https://github.com/eclipse/dash-licenses/tags)

```shell
# move to a persistent folder. Could also be ~/jars.
mv org.eclipse.dash.licenses-1.1.0.jar ~/coding/org.eclipse.dash.licenses-1.1.0.jar
vim ~/.bashrc
# add following line using i
alias eclipseDashTool='java -jar ~/coding/org.eclipse.dash.licenses-1.1.0.jar'
# esc, qw -> enter to save and exit
source ~/.bashrc
# cd to directory containing the requirements.txt
cd tools/sanity-check

cat requirements.txt | grep -v \# \
| sed -E -e 's|([^= ]+)==([^= ]+)|pypi/pypi/-/\1/\2|' -e 's| ||g' \
| sort | uniq \
| eclipseDashTool -project automotive.tractusx -summary ./DEPENDENCIES -
```
