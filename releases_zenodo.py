import os, requests

TOKEN = os.environ.get("MY_TOKEN")

def get_releases():
    # parse repositories.txt
    with open('repositories.txt') as f:
        lines = f.readlines()

    releases_report = []
    # query github API : get latest releases
    for repo in lines:
        if len(repo.strip()) > 0:
            repo_release = {}
            release_id, release_tag,draft_or_prerelease = None, None, False
            owner, repo_name = repo.split('/')[0],repo.split('/')[1].split(':',1)[0]
            req = requests.get("https://api.github.com/repos/"+owner+"/"+repo_name+"/releases")
            if req.status_code == 200:
                resp = req.json()
                if len(resp) > 0:
                    release_id = resp[0]['id'] if 'id' in resp[0] else None
                    release_tag = resp[0]['tag_name'] if 'tag_name' in resp[0] else None
                    draft_or_prerelease = False if (resp[0]['draft'] == False \
                        and resp[0]['prerelease'] == False) else True

            if release_id:
                repo_release["repo"] = repo
                repo_release["release_id"] = release_id
                repo_release["release_tag"] = release_tag
                repo_release["draft_or_prerelease"] = draft_or_prerelease
                releases_report.append(repo_release)
    if "GITHUB_OUTPUT" in os.environ :
        with open(os.environ["GITHUB_OUTPUT"], "a") as f :
            print("{0}={1}".format("releases_report", releases_report), file=f)

get_releases()
# zenodo sync ?
# report
# FIX: cannot be the same one because releases are for repos,
# while the schema validation is on more than 1 md per repo
# PR zenodo.json
# return list of repositories for RDF transformation
