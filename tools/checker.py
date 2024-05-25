import requests
import subprocess
import pandas as pd
from pathlib import Path

# TODO make this to be a parameter
# constant of your markdown file
file_path = Path("Testtable.md")

# TODO determine tables by release
# TODO run check per table
# Read markdown
with file_path.open() as f:
    markdown_table = f.read()

# Convert Markdown table to DataFrame
data = markdown_table.split("\n")
data = [line.strip("|").split("|") for line in data if line.strip()]
headers = [header.strip() for header in data[0]]
# skip headers and format line with "|---|---|..."
df = pd.DataFrame(data[2:], columns=headers)

# Helm repository setup
subprocess.run(["helm", "repo", "add", "tractusx-dev", "https://eclipse-tractusx.github.io/charts/dev"], capture_output=True)
subprocess.run(["helm", "repo", "update"], capture_output=True)


def transform_row_to_dict(row):
    component_name = row['Component'].strip().split(']')[0][1:]
    helm_chart = row['Helm Chart (s)']

    component_link = row['Component'].strip().split(']')[1][1:-1]

    # sample Frontend: [v1.3.1](https://link-to-version)<br/> Backend: [v1.3.1](https://link-to-version)
    app_kit_line = row['App-/KIT Version (s)'].strip()
    print(f"app_kit_line: {app_kit_line}")
    app_kit_array = []
    if "<br/>" in app_kit_line:
        print("Multiline app_kit_line")
        for app in app_kit_line.split("<br/>"):
            name = app.strip().split(":")[0]
            version = app[app.index("[") +1:app.index("]")]
            version = version[1:] if version[0] == "v" else version
            link = app[app.index("(") +1:app.index(")")]
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
        print(f"helm chart {helm_chart}")
        chart_name = helm_chart.split(':')[0].strip()
        chart_version = helm_chart[helm_chart.index("[") + 1:helm_chart.index("]")].strip()
        print(f"chart_version: {chart_version}")
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


def check_link(url):
    try:
        # follow redirects as eclipse-tractusx.github.io redirects
        response = requests.head(url, allow_redirects=True)

        status_code = response.status_code
        # print(f"Status code: {status_code}")
        return 200 <= status_code < 300
    except requests.RequestException:
        print(f"Error: {url}, {requests.RequestException}")
        return False


def check_versions(chart_name):
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


def check_links_kit(parsed_row):
    print(f"Checking links for {parsed_row['type']}: {parsed_row['type_name']}")

    # Eclipse-Tractus-X link
    if not check_link(parsed_row['type_link']):
        print(f"  Error: KIT {parsed_row['type_name']} has invalid link '{parsed_row['type_link']}'")

    # github changelog
    if not check_link(parsed_row['kit']['link']):
        print(f"  Error: Changelog of KIT {parsed_row['type_name']} has invalid link '{parsed_row['kit']['link']}'")


def check_links_foss(parsed_row):
    print(f"Checking links for {parsed_row['type']} Component: {parsed_row['type_name']}")

    # release
    if not check_link(parsed_row['type_link']):
        print(f"  Error: FOSS {parsed_row['type_name']} has invalid link '{parsed_row['type_link']}'")

    # chart
    chart = parsed_row['chart']
    if not check_link(chart['link']):
        print(f"  Error: Release of FOSS Chart {chart['name']} has invalid link '{chart['link']}'")
    if not chart['link'].endswith(chart['version']):
        print(
            f"  Error: Release version '{chart['version']}' and link version '{chart['link']}' of FOSS Chart {chart['name']} do not match")

    # apps
    for app in parsed_row['apps']:
        if not check_link(app['link']):
            print(f"  Error: Release of FOSS APP {app['name']} has invalid link '{app['link']}'")
        if not app['link'].endswith(app['version']):
            print(f"  Error: Release version '{app['version']}' and link version '{app['link']}' of FOSS APP {app['name']} do not match")

def check_chart_versions_repo_foss(parsed_row):
    print(f"Checking chart for {parsed_row['type']} Component: {parsed_row['type_name']}")

    chart = parsed_row['chart']
    # Check if Helm chart and app version are latest
    latest_chart_version, latest_app_version = check_versions(chart["name"])
    if not (latest_chart_version and latest_app_version):
        print(f"  Error: Could not retrieve latest Helm chart or app version for {chart['name']}.")

    if latest_chart_version != chart["version"]:
        print(f"  Error: Chart version of FOSS Chart {chart['name']} has version {chart['version']} while version {latest_chart_version} is available in tractusx-dev")

    for app in parsed_row['apps']:
        if latest_app_version != app["version"]:
            print(
                f"  Error: App version of FOSS Chart {chart['name']} (app {app['name']}) has app version {app['version']} while version {latest_app_version} is set in Chart available in tractusx-dev")


for index, row in df.iterrows():

    parsed_row = transform_row_to_dict(row)

    if parsed_row["type"] == 'KIT':
        check_links_kit(parsed_row)
    else:
        check_links_foss(parsed_row)
        check_chart_versions_repo_foss(parsed_row)

