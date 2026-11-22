# Spott wiring

Check the destination application and pipeline configuration using HireData MCP. An application links the candidate to this particular vacancy. Common discovery paths include `application.candidate` and `application.vacancy`. Confirm their identifiers and the application owner in the context available at the send step.

An application-created event followed by a pipeline-stage filter can select records created in that stage. To alert a candidate when an existing application moves into a stage, verify that an appropriate transition event and filter are available. If that route cannot be verified, expose the limitation. Replaying creation could resend alerts for existing applications.

Where a vacancy description is held in a separate record, look it up by the current application’s vacancy ID. Verify language, medium and result count. Keep the employer and application owner available for message facts or reply routing while addressing the alert to the application’s candidate.

For interest collection, bind the chosen response route to the original application and a response identity that the destination can verify. Compare the actual stored answer option with each branch condition. Update only the bound application and link any note to the intended record. If a stage update can continue on error, check its result before creating a note that describes it as completed.

Test two applications for the same candidate and vacancy changes while waiting. Confirm a reply for the first application cannot update the second. Check whether the supported uniqueness mechanism covers simultaneous events before promising that guarantee.
