from typing import Union, List

import requests

from config import *


def get_issues(query_params: dict) -> list:
    page = 1
    filtered_issues = []
    params = {
        "filter": "all",
        "per_page": MAX_PAGE_ENTRIES
    }
    params.update(query_params)

    while True:
        response = requests.get(URL, params={**params, 'page': page}, headers=REQ_HEADERS)
        # I could do some assertions on the body schema, but I think that's over-kill
        if response.status_code != OK_STATUS or not response.json():
            break

        page_issues = response.json()
        filtered_issues.extend(page_issues)
        page += 1

    return filtered_issues


def create_issue(title: Union[str, int],
                 body: str = '',
                 milestone: Union[str, int, None] = None,
                 labels: list = None,
                 assignees: List[str] = None) -> dict:
    req_body = {
        'title': title,
        'body': body,
        'milestone': milestone,
        'labels': labels,
        'assignees': assignees
    }
    clean_req_body = {k: v for k, v in req_body.items() if v is not None}
    response = requests.post(URL, headers=REQ_HEADERS, json=clean_req_body)
    assert response.status_code == CREATED_STATUS
    return response.json()


def update_issue(issue_num: int,
                 title: Union[str, int, None] = None,
                 body: Union[str, None] = None,
                 state: str = None,
                 state_reason: Union[str, None] = None,
                 milestone: Union[str, int, None] = None,
                 labels: list = None,
                 assignees: List[str] = None) -> dict:
    req_body = {
        'title': title,
        'body': body,
        'state': state,
        'state_reason': state_reason,
        'milestone': milestone,
        'labels': labels,
        'assignees': assignees
    }
    clean_req_body = {k: v for k, v in req_body.items() if v is not None}

    response = requests.patch(f'{URL}/{str(issue_num)}', headers=REQ_HEADERS, json=clean_req_body)

    assert response.status_code == OK_STATUS

    return response.json()
