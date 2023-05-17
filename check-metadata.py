import json

with open('/tmp/service-catalog-payload.json') as fp:
  payload = json.load(fp)
  
catalog = payload['catalog.json']
messages = []

# Esnure that everyone has a GitHub URL specified.
github_url = catalog['meta'].get('github_url', None)
if not github_url:
  messages.append["No `github_url` specified in the `meta` section of the file."]

if github_url and not github_url.startswith("https://github.com"):
  messages.append("The `github_url` specified in the `meta` section of the file, doesn't seem to point to GitHub.")

# Ensure that priority 1 services have a pager_duty_url.
if catalog['priority'] < 2:
  pager_duty_url = catalog['meta'].get('pager_duty_url', None)
  if not pager_duty_url:
    messages.append("No `pager_duty_url` specified in the `meta` section of the file. This is required for priority 1 services.")

  if pager_duty_url and not pager_duty_url.startswith("https://pagerduty.com"):
    messages.append("The `pager_duty_url` specified in the `meta` section of the file, doesn't seem to point to PagerDuty. This is required for priority 1 services.")

  
result = "fail" if len(messages) > 0  else "pass"
with open('/tmp/service-catalog-result.json', 'w') as fp:
  json.dump({'result': result, 'message': "\n\n".join(messages)}, fp)
