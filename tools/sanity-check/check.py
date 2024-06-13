# #############################################################################
# Copyright (c) 2024 Contributors to the Eclipse Foundation
#
# See the NOTICE file(s) distributed with this work for additional
# information regarding copyright ownership.
#
# This program and the accompanying materials are made available under the
# terms of the Apache License, Version 2.0 which is available at
# https://www.apache.org/licenses/LICENSE-2.0.
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.
#
# SPDX-License-Identifier: Apache-2.0
# #############################################################################

import requests
import subprocess
import pandas as pd
from pathlib import Path
import sys

"""
Walks through a table row-wise and extracts it either as a KIT or FOSS component into a dict for easier processing

Example FOSS component:
{
    'type': 'FOSS',
    'type_name': 'Country Risk',
    'type_link': 'https://github.com/eclipse-tractusx/vas-country-risk',
    'chart': {
        'name': 'country-risk',
        'version': '3.0.11',
        'link': '3.0.11'
    },
    'apps': [
        {
            'name': 'Frontend',
            'version': 'v1.3.1',
            'link': 'https://github.com/eclipse-tractusx/vas-country-risk/releases/tag/v1.3.1'
        }, {
            'name': 'Backend',
            'version': 'v1.3.1',
            'link': 'https://github.com/eclipse-tractusx/vas-country-risk-backend/releases/tag/v1.3.1'
        }
    ]
}

Example KIT:
{
    'type': 'KIT',
    'type_name': 'Digital Twin KIT',
    'type_link': 'https://eclipse-tractusx.github.io/docs-kits/category/digital-twin-kit',
    'kit': {
        'version': '1.2.0',
        'link': 'https://eclipse-tractusx.github.io/docs-kits/kits/Digital%20Twin%20Kit/Digital%20Twin%20Kit%20Changelog'
    }
}
"""
def transform_row_to_dict(row):
    component_name = row['Component'].strip().split(']')[0][1:]
    helm_chart = row['Helm Chart (s)']

    component_link = row['Component'].strip().split(']')[1][1:-1]

    # sample Frontend: [v1.3.1](https://link-to-version)<br/> Backend: [v1.3.1](https://link-to-version)
    app_kit_line = row['App-/KIT Version (s)'].strip()
    app_kit_array = []
    if "<br/>" in app_kit_line:
        print(f"Multiline APPs for FOSS Component {component_name}")
        for app in app_kit_line.split("<br/>"):
            # portal has double br, skip empty line
            if len(app.strip()) == 0:
                continue
            name = app.strip().split(":")[0]
            version = app[app.index("[") + 1:app.index("]")]
            version = version[1:] if version[0] == "v" else version
            link = app[app.index("(") + 1:app.index(")")]
            app_kit_array.append({
                "name": name,
                "version": version,
                "link": link
            })
    else:
        version = app_kit_line[app_kit_line.index("[") + 1:app_kit_line.index("]")]
        link = app_kit_line[app_kit_line.index("(") + 1:app_kit_line.index(")")]
        app_kit_array.append({
            "name": component_name,
            "version": version,
            "link": link
        })

    type = "KIT" if "n/a" in helm_chart else "FOSS"

    # Extract chart name and version if available
    if type == "FOSS":
        chart_name = helm_chart.split(':')[0].strip()
        chart_version = helm_chart[helm_chart.index("[") + 1:helm_chart.index("]")].strip()
        chart_version_link = helm_chart.split('(')[-1].split(')')[0].strip()
        return {
            "type": type,
            "type_name": component_name,
            "type_link": component_link,
            "chart": {
                "name": chart_name,
                "version": chart_version,
                "link": chart_version_link
            },
            "apps": app_kit_array
        }
    else:
        return {
            "type": type,
            "type_name": component_name,
            "type_link": component_link,
            "kit": app_kit_array[0]
        }


"""
Returns true if link request results in a 200er, else false

Allows redirects
"""
def check_link(url):
    try:
        # follow redirects as eclipse-tractusx.github.io redirects
        response = requests.head(url, allow_redirects=True)

        status_code = response.status_code
        # print(f"Status code: {status_code}")
        return 200 <= status_code < 300
    except requests.RequestException:
        print(f"ERROR: {url}, {requests.RequestException}")
        return False


"""
Extracts latest chart and app version for chart.

chart_name without prefix "tractusx-dev/" 

We only take the latest. If there are different charts that start with the same name, we only use the first overall 
chart (it's the chart_name).
"""
def determine_latest_versions_for_chart(chart_name):
    # if rc and so on would be needed --devel
    helm_search = subprocess.run(
        ["helm", "search", "repo", f"tractusx-dev/{chart_name}", "--versions"],
        capture_output=True,
        text=True
    )
    latest_chart_version = None
    latest_app_version = None

    if helm_search.returncode == 0:
        output_lines = helm_search.stdout.splitlines()

        # > 1 needed due to header (NAME, CHART VERSION, APP VERSION)
        if len(output_lines) > 1:
            latest_chart_version = output_lines[1].split("\t")[1].strip()
            latest_app_version = output_lines[1].split("\t")[2].strip()
    return latest_chart_version, latest_app_version


"""
Checks all links for the KIT to be working

Checks following links:
- Eclipse-Tractus-X Link
- Github Changelog
"""
def check_links_kit(parsed_row):
    print(f"Checking LINKS for {parsed_row['type']}: {parsed_row['type_name']}")

    # Eclipse-Tractus-X link
    if not check_link(parsed_row['type_link']):
        print(f"  ERROR: KIT {parsed_row['type_name']} has invalid link '{parsed_row['type_link']}'")

    # github changelog
    if not check_link(parsed_row['kit']['link']):
        print(f"  ERROR: Changelog of KIT {parsed_row['type_name']} has invalid link '{parsed_row['kit']['link']}'")


"""
Checks all links for the FOSS to be working

Checks following links:
- release / repo link
- chart link
- release link in github for apps of chart
"""
def check_links_foss(parsed_row):
    print(f"Checking LINKS for {parsed_row['type']} Component: {parsed_row['type_name']}")

    # release
    if not check_link(parsed_row['type_link']):
        print(f"  ERROR: FOSS {parsed_row['type_name']} has invalid link '{parsed_row['type_link']}'")

    # chart
    chart = parsed_row['chart']
    if not check_link(chart['link']):
        print(f"  ERROR: Release of FOSS Chart {chart['name']} has invalid link '{chart['link']}'")
    if not chart['link'].endswith(chart['version']):
        print(
            f"  ERROR: Release version '{chart['version']}' and link version '{chart['link']}' of FOSS Chart {chart['name']} do not match")

    # apps
    for app in parsed_row['apps']:
        if not check_link(app['link']):
            print(f"  ERROR: Release of FOSS APP {app['name']} has invalid link '{app['link']}'")
        if not app['link'].endswith(app['version']):
            print(
                f"  ERROR: Release version '{app['version']}' and link version '{app['link']}' of FOSS APP {app['name']} do not match")


"""
Determines latest chart and app version from Chart and cross-checks

Performs following checks:
- check that chart has been released
- check that helm repo version == given version
- check that app version is same for all apps of chart
"""
def check_chart_versions_repo_foss(parsed_row):
    print(f"Checking CHART for {parsed_row['type']} Component: {parsed_row['type_name']}")

    chart = parsed_row['chart']
    # Check if Helm chart and app version are latest
    latest_chart_version, latest_app_version = determine_latest_versions_for_chart(chart["name"])
    if not (latest_chart_version and latest_app_version):
        print(f"  ERROR: Could not retrieve latest Helm chart or app version for {chart['name']}.")

    if latest_chart_version != chart["version"]:
        print(
            f"  ERROR: Chart version of FOSS Chart {chart['name']} has version {chart['version']} while version {latest_chart_version} is available in tractusx-dev")

    for app in parsed_row['apps']:
        # normalize as apps in GitHub may start with v but list output of helm search is always without v
        # only use for comparison so that during check we know not to false-positive correct the GitHub app link
        normalized_app_version = app["version"].lstrip('v')
        if latest_app_version != normalized_app_version:
            print(
                f"  ERROR: App version of FOSS Chart {chart['name']} (app {app['name']}) has app version {app['version']} while version {latest_app_version} is set in Chart available in tractusx-dev")


"""
Performs the actual checks:

KIT: check only links are working
FOSS:
- check links are working
- check versions are correct (latest used, links contain correct version)
"""
def check_table(df):
    for index, row in df.iterrows():

        parsed_row = transform_row_to_dict(row)

        if parsed_row["type"] == 'KIT':
            check_links_kit(parsed_row)
        else:
            check_links_foss(parsed_row)
            check_chart_versions_repo_foss(parsed_row)


"""
Transforms table data to a data frame

- data must be lines of data each still containing the table limiters "|"
- we expect exactly 3 columns per table (Component, Helm Chart (s), App-/KIT Version (s)
"""
def get_table_as_df(data):
    data = [line.strip("|").split("|") for line in data if line.strip()]
    for line in data:
        assert len(line) == 3, f"line {line} has wrong length {len(line)}, but we expect 3"
    headers = [header.strip() for header in data[0]]
    # skip headers and format line with "|---|---|..."
    df = pd.DataFrame(data[2:], columns=headers)
    return df


"""
Returns list of tuple (table heading, table as df)

- Finds heading via h3 (###)
- Identifies tables via starting with | and having further | in line
"""
def extract_tables_as_dfs(release_content):
    lines = release_content.split('\n')
    tables = []
    table_heading = ""
    table_data = []
    in_table = False

    print(f"Release consists of {len(lines)} lines")

    for line in lines:
        if line.startswith("###"):
            table_heading = line[4:].strip()
        if line.strip().startswith('|') and '|' in line:
            in_table = True
            table_data.append(line)
        else:
            if in_table:
                if len(table_data) > 0:
                    df = get_table_as_df(table_data)
                    tables.append((table_heading, df))
                table_data = []
                in_table = False

    # Process the last table if the file ends while still in a table
    if in_table and table_data:
        [print(line) for line in table_data]
        df = get_table_as_df(table_data)
        tables.append((table_heading, df))

    return tables


"""
Extracts tables from markdown file for a release_of_interest

Currently the links or similar outside the table are not considered
"""
def extract_tables_for_release(file_path, release_of_interest):
    with open(file_path, 'r') as file:
        content = file.read()

    # results in n +1 releases as there is one chunk prior to the first release heading
    releases = content.split('## [')[1:]
    print(f"Found {len(releases)} releases")
    tables = []
    for release in releases:
        # Heading till link [ has already been already substringed
        release_name = release.split(']')[0].strip()
        if release_name == release_of_interest:
            # release_content = release.split(']')[1]
            print(f"Extracting tables for release: {release_name}")
            tables = extract_tables_as_dfs(release)
            return tables

    return tables


"""
Extracts tables from markdown file to check for working links and version mismatches

Updates tractusx-dev helm chart repository to check chart versions
"""
def main():
    if len(sys.argv) > 1:
        file_path = Path(sys.argv[1])
        release_of_interest = sys.argv[2]
    else:
        print("Please use as follows: python relative-path/CHANGELOG.md 24.05")
        exit(-1)

    df_tables = extract_tables_for_release(file_path, release_of_interest)

    if len(df_tables) == 0:
        print(f"No tables found for release {release_of_interest} in file {file_path}")
        exit(0)

    # Helm repository setup
    subprocess.run(["helm", "repo", "add", "tractusx-dev", "https://eclipse-tractusx.github.io/charts/dev"],
                   capture_output=True)
    subprocess.run(["helm", "repo", "update"], capture_output=True)

    for table_heading, df in df_tables:
        print(f"\nProcessing table '{table_heading}'")
        check_table(df)
        print()


if __name__ == "__main__":
    main()
