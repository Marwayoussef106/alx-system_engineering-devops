# Postmortem Report

## Issue Summary

**Duration**: The outage lasted from 3:00 PM to 5:45 PM EST on April 14, 2024.

**Impact**: During this period, our main website was down, resulting in a complete inability for users to access their accounts. Approximately 68% of our users experienced this service disruption during peak hours, which prevented them from completing transactions and accessing important financial information.

**Root Cause**: The primary cause of the outage was an incorrect configuration change in the load balancers, which led to a routing loop within our internal networks.

## Timeline

- **3:00 PM**: Issue detected by our automated monitoring system, which flagged an unusually high response time from our primary web service.
- **3:05 PM**: Initial investigation by Site Reliability Engineering (SRE) team suggested a potential network bottleneck.
- **3:30 PM**: As user complaints increased, the issue was escalated to the Network Operations team.
- **3:50 PM**: Network Operations conducted a review of recent changes and identified a recent update to load balancer configurations as suspicious.
- **4:15 PM**: Testing in a controlled environment replicated the issue when using the new configuration.
- **4:45 PM**: A decision was made to roll back the load balancer configuration to the previous stable version.
- **5:00 PM**: Configuration rollback initiated.
- **5:30 PM**: Services began to recover gradually as the correct configuration was propagated across the network.
- **5:45 PM**: Full recovery achieved, monitoring confirmed that response times returned to normal levels.

## Root Cause and Resolution

**Cause**: The outage was triggered by a newly deployed configuration in the load balancers that incorrectly routed traffic, creating a loop that overwhelmed the network.

**Resolution**: The faulty configuration was rolled back to the previous stable version, and the correct routing paths were restored, resolving the outage.

## Corrective and Preventative Measures

To prevent a recurrence of this issue and improve our overall system resilience, we propose the following steps:

- **Review and enhance our change management procedures** to include additional checks and tests for network-related updates.
- **Enhance monitoring tools** to detect and alert unusual patterns in network traffic that could indicate routing issues.
- **Conduct a comprehensive audit of network configurations** across all environments to ensure they meet our standards for resilience and stability.
- **Implement a staged rollout for configuration changes** to load balancers, starting with a smaller subset of traffic to monitor impact before full deployment.
- **Training for all network engineers** on the latest best practices for configuration management and troubleshooting in complex environments.

By implementing these measures, we aim to strengthen our systems against similar failures and improve our response capabilities for future incidents.

