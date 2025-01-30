"""
Collect the total number of dependents over all versions

Reference: https://docs.deps.dev/api/v3alpha/#getdependents
Path parameters

packageKey.system: string

    The package management system containing the package.

    Can be one of GO, NPM, CARGO, MAVEN, PYPI, NUGET.
packageKey.name: string

    The name of the package.


## GetPackage

GET https://api.deps.dev/v3alpha/systems/{packageKey.system}/packages/{packageKey.name}

GetPackage returns information about a package, including a list of its available versions, with the default version marked if known.

Response

packageKey: object

    The name of the package. Note that it may differ from the name in the request, due to canonicalization.
packageKey.system: string

    The package management system containing the package.

    Can be one of GO, NPM, CARGO, MAVEN, PYPI, NUGET.
packageKey.name: string

    The name of the package.
purl: string

    The purl that identifies this package. Note that the package name may differ from the name in the request, due to canonicalization.
versions[]: object[]

    The available versions of the package.
versions[].versionKey: object

    The name of the version. Note that the package name may differ from the name in the request, due to canonicalization.
versions[].versionKey.system: string

    The package management system containing the package.

    Can be one of GO, NPM, CARGO, MAVEN, PYPI, NUGET.
versions[].versionKey.name: string

    The name of the package.
versions[].versionKey.version: string

    The version of the package.
versions[].purl: string

    The purl that identifies this version of the package. Note that the package and version name in the purl may differ from the names in the request, due to canonicalization.
versions[].publishedAt: string

    The time when this package version was published, if available, as reported by the package management authority.
versions[].isDefault: boolean

    If true, this is the default version of the package: the version that is installed when no version is specified. The precise meaning of this is system-specific, but it is commonly the version with the greatest version number, ignoring pre-release versions.
versions[].isDeprecated: boolean

    If true, this version has been marked as deprecated.


## GetDependents

GET /v3alpha/systems/{versionKey.system}/packages/{versionKey.name}/versions/{versionKey.version}:dependents

GetDependents returns information about the number of distinct packages known to depend on the given package version. Dependent counts are currently available for Go, npm, Cargo, Maven and PyPI.

Dependent counts are derived from the dependency graphs computed by deps.dev, which means that only public dependents are counted. As such, dependent counts should be treated as indicative of relative popularity rather than precisely accurate.
Path parameters

versionKey.system: string

    The package management system containing the package.

    Can be one of GO, NPM, CARGO, MAVEN, PYPI, NUGET.
versionKey.name: string

    The name of the package.
versionKey.version: string

    The version of the package.

Response

dependentCount: number

    The number of packages known to depend on this package version, either directly or indirectly. Note that this may be less than the sum of the direct and indirect dependent counts.
directDependentCount: number

    The number of packages known to depend directly on this package version.
indirectDependentCount: number

    The number of packages known to depend indirectly on this package version.

GetCapabilities

GET /v3alpha/systems/{versionKey.system}/packages/{versionKey.name}/versions/{versionKey.version}:capabilities

GetCapabilityRequest returns counts for direct and indirect calls to Capslock capabilities for a given package version. Currently only available for Go.
Path parameters

versionKey.system: string

    The package management system containing the package.

    Can be one of GO, NPM, CARGO, MAVEN, PYPI, NUGET.
versionKey.name: string

    The name of the package.
versionKey.version: string

    The version of the package.

Response

capabilities[]: object[]

    The Capslock capabilities associated with a package, along with the number of direct and indirect callpaths to this capability.
capabilities[].capability: string

    A Capslock capability, indicating that the packages uses this capability.
capabilities[].directCount: number

    The number of calls from this package directly to this capability.
capabilities[].indirectCount: number

    The number of calls from this package to the capability via another package.

GetProject

GET /v3alpha/projects/{projectKey.id}

GetProject returns information about projects hosted by GitHub, GitLab, or BitBucket, when known to us.

Example: /v3alpha/projects/github.com%2Ffacebook%2Freact
Path parameters

projectKey.id: string

    A project identifier of the form github.com/user/repo, gitlab.com/user/repo, or bitbucket.org/user/repo.

Response

projectKey: object

    The identifier for the project. Note that this may differ from the identifier in the request, due to canonicalization.
projectKey.id: string

    A project identifier of the form github.com/user/repo, gitlab.com/user/repo, or bitbucket.org/user/repo.
openIssuesCount: number

    The number of open issues reported by the project host. Only available for GitHub and GitLab.
starsCount: number

    The number of stars reported by the project host. Only available for GitHub and GitLab.
forksCount: number

    The number of forks reported by the project host. Only available for GitHub and GitLab.
license: string

    The license reported by the project host.
description: string

    The description reported by the project host.
homepage: string

    The homepage reported by the project host.
scorecard: object

    An OpenSSF Scorecard for the project, if one is available.
scorecard.date: string

    The date at which the scorecard was produced. The time portion of this field is midnight UTC.
scorecard.repository: object

    The source code repository and commit the scorecard was produced from.
scorecard.repository.name: string

    The source code repository the scorecard was produced from.
scorecard.repository.commit: string

    The source code commit the scorecard was produced from.
scorecard.scorecard: object

    The version and commit of the Scorecard program used to produce the scorecard.
scorecard.scorecard.version: string

    The version of the Scorecard program used to produce the scorecard.
scorecard.scorecard.commit: string

    The commit of the Scorecard program used to produce the scorecard.
scorecard.checks[]: object[]

    The results of the Scorecard Checks performed on the project.
scorecard.checks[].name: string

    The name of the check.
scorecard.checks[].documentation: object

    Human-readable documentation for the check.
scorecard.checks[].documentation.shortDescription: string

    A short description of the check.
scorecard.checks[].documentation.url: string

    A link to more details about the check.
scorecard.checks[].score: number

    A score in the range [0,10]. A higher score is better. A negative score indicates that the check did not run successfully.
scorecard.checks[].reason: string

    The reason for the score.
scorecard.checks[].details[]: string[]

    Further details regarding the check.
scorecard.overallScore: number

    A weighted average score in the range [0,10]. A higher score is better.
scorecard.metadata[]: string[]

    Additional metadata associated with the scorecard.
ossFuzz: object

    Details of this project’s testing by the OSS-Fuzz service. Only set if the project is tested by OSS-Fuzz.
ossFuzz.lineCount: number

    The total number of lines of code in the project.
ossFuzz.lineCoverCount: number

    The number of lines of code covered by fuzzing.
ossFuzz.date: string

    The date the fuzz test that produced the coverage information was run against this project. The time portion of this field is midnight UTC.
ossFuzz.configUrl: string

    The URL containing the configuration for the project in the OSS-Fuzz repository.


"""

import requests

def get_package_info(system: str, package_name: str) -> dict:
    """Get package information from deps.dev API"""
    url = f"https://api.deps.dev/v3alpha/systems/{system}/packages/{package_name}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"API request failed: {response.status_code}")
    return response.json()

def get_version_info(system: str, package_name: str, version: str) -> dict:
    """Get specific version information including dependents"""
    url = f"https://api.deps.dev/v3alpha/systems/{system}/packages/{package_name}/versions/{version}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"API request failed: {response.status_code}")
    return response.json()

def get_dependents_for_version(system: str, package_name: str, version: str) -> int:
    """Get dependent count for a specific version"""
    url = f"https://api.deps.dev/v3alpha/systems/{system}/packages/{package_name}/versions/{version}:dependents"
    response = requests.get(url)
    if response.status_code != 200:
        return 0
    data = response.json()
    return data.get('dependentCount', 0)

def get_total_dependents(system: str, package_name: str) -> int:
    """
    Get total number of dependents across all versions of a package
    
    Args:
        system: Package system (NPM, PYPI, etc)
        package_name: Name of the package
    
    Returns:
        Total number of unique dependents
    """
    try:
        # Get all versions
        package_info = get_package_info(system, package_name)
        if 'versions' not in package_info:
            return 0

        total_dependents = 0
        for version in package_info['versions']:
            version_key = version['versionKey']
            dependents = get_dependents_for_version(
                version_key['system'],
                version_key['name'],
                version_key['version']
            )
            total_dependents = max(total_dependents, dependents)
            print(f"Version {version_key['version']}: {dependents} dependents")
            
        return total_dependents
        
    except Exception as e:
        print(f"Error collecting dependents for {package_name}: {str(e)}")
        return 0

if __name__ == "__main__":
    # Example usage
    system = "MAVEN"
    package = "org.apache.logging.log4j:log4j-api"
    total = get_total_dependents(system, package)
    print(f"Total unique dependents for {package}: {total}")