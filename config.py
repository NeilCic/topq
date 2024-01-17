OWNER = 'topq-practice'
REPO_NAME = 'api-practice'
URL = f'https://api.github.com/repos/{OWNER}/{REPO_NAME}/issues'
MAX_PAGE_ENTRIES = 100
REQ_HEADERS = {
    "Accept": "application/vnd.github+json",
    "Authorization": "Bearer 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",
    "X-GitHub-Api-Version": "2022-11-28"
}

OK_STATUS = 200
CREATED_STATUS = 201
