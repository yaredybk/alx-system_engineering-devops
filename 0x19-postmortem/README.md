## Postmortem: Database Update Bug and Data Recovery (May 9, 2024)
![unsafe update desaster]("usafe_update_disaster_3.jpg")
## Issue Summary
Duration: May 9, 2024 (5 days after code deployment) - May 11, 2024 (2 days)
Impact: All proforma updates after May 4, 2024, were overwritten due to an unsafe update query. Users were unable to access or edit proforma data beyond May 4th. Downtime for updates and editing lasted two days (May 9th - 10th). Paperwork was used as a temporary workaround.
Root Cause: The deployed update code lacked a WHERE clause, causing all proforma records to be updated with the latest data.
## Timeline

May 4, 2024: Faulty code for updating proforma records was deployed to production.
May 9, 2024: A user reported an inability to access historical proforma data.
May 9, 2024 (AM): Investigation began. The update code was reviewed, and the missing WHERE clause was identified as the culprit.
May 9, 2024 (PM): A fix was developed and implemented, introducing a parameterized query with a WHERE clause to update specific proforma records.
May 9, 2024 - May 10, 2024: Data recovery efforts commenced. Manual SQL queries were used to restore overwritten proforma data from daily database dumps.
May 11, 2024: Data recovery was mostly complete. System functionality was restored, allowing access and updates to all proforma records.
## Root Cause and Resolution

The root cause of the issue was an unsafe update query in the deployed code. The code lacked a WHERE clause to filter updates to specific proforma records. This resulted in all proforma entries being overwritten with the latest data point.

The resolution involved fixing the update code. A parameterized query with a WHERE clause specifying the idproforma was implemented to ensure updates only modify the intended record.

## Corrective and Preventative Measures

Code Reviews: Mandatory code reviews will be conducted before deploying updates, with a specific focus on database interactions and filtering mechanisms.
Unit Testing: Unit tests will be implemented to cover database interactions, including update queries, to identify potential issues before deployment.
Database Safeguards: We will explore implementing database-level safeguards, such as triggers or stored procedures, to prevent accidental data overwrites.
Backup Strategy Review: The current daily database dump strategy will be reviewed. We will consider implementing a versioning system to retain historical snapshots or explore alternative backup solutions that facilitate easier data recovery.
## Lessons Learned

The importance of thorough code reviews and unit testing before deploying updates cannot be overstated.
A well-defined data backup strategy with versioning or point-in-time restoration capabilities is crucial for efficient data recovery in case of incidents.
Clear communication with stakeholders during and after an incident is essential to minimize disruptions and restore user confidence.
## Additional Notes

This incident resulted in a two-day downtime for proforma updates and editing. Paperwork was used as a temporary workaround. Data recovery efforts involved restoring overwritten data from daily database dumps, resulting in the loss of some proforma entries written on May 4th. While the majority of data was recovered, this incident highlights the importance of robust data backup strategies and preventative measures to avoid similar situations in the future.
