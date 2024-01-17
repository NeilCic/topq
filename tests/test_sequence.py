from utils import get_issues, create_issue, update_issue


def test_scenario():
    # step 1
    open_issues1 = get_issues({'state': 'open'})
    print(len(open_issues1))

    # step 2
    practice1_issues = get_issues({'labels': ['practice1']})
    print(len(practice1_issues))

    # step 3
    title = "Neil's issue"
    body = 'This issue was created via REST API from Python by Neil'
    labels = ['practice1']
    assignee = 'topq-practice'
    created_issue = create_issue(
        title=title,
        body=body,
        labels=labels,
        assignee=assignee
    )
    # step 4
    print(created_issue['number'])

    # step 5 - "Get a list of all issues and verify in the response JSON" I'm assuming this means all OPEN issues as instructed in step 1
    open_issues2 = get_issues({'state': 'open'})
    assert len(open_issues2) == len(open_issues1) + 1
    assert open_issues2[0]['title'] == title

    # step 6
    _ = update_issue(issue_num=created_issue['id'], state='closed', state_reason='not_planned')

    # step - 7 "Get a list of all issues and verify the total number of issues is again equal to the initial number
    # of issues (because the issue you created is now closed, it shouldn't be in the returned list of issues)."
    # assuming more confidently that this means getting all the OPEN issues
    open_issues3 = get_issues({'state': 'open'})
    assert len(open_issues3) == len(open_issues1)
