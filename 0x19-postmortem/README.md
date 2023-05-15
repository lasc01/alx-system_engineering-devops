# Postmortem

## Format

### Issue Summary

* Duration of outage
    + Start time: Friday, May 12th 2023. 3:30pm (GMT+1)
    + End time: Wednesday, May 12th 2023. 5:00pm (GMT+1)
* Impact
* Root cause

### Timeline

* Issue detection time: 3:30pm
* Issue detection method: Monitoring alert
* Actions taken: Test
* Misleading investigation(debugging) paths taken:
* Incident resolution method:



## Actual postmortem

### Issue Summary

This is a postmortem created for an issue that occured between 3:30 pm and 5pm on Friday, the 12th of May 2023 (GMT+1). It effectively led to the shutdown of our services witgin that time interval. About an estimated 70% of our userbase was affected by it. The root cause of the issue was found to be in a misconfiguration of our Nginx server after an upgrade.

The issue was detected by our monitoring service Datadog, some ten seconds after it occurred. An alert was consequently sent to Abioro Olamide our on-call software engineer who successfully solved the issue


