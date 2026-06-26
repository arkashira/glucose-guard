# REQUIREMENTS.md
## Introduction
The Glucose Guard project aims to develop a simple Python-based system that simulates a glucose monitoring and alert system. This document outlines the functional and non-functional requirements for the project.

## Functional Requirements
1. **FR-1: Glucose Reading Updates**: The system shall update glucose readings at regular intervals (e.g., every 5 minutes).
2. **FR-2: Alert Generation**: The system shall generate alerts when glucose levels exceed predefined thresholds (e.g., high: 180 mg/dL, low: 70 mg/dL).
3. **FR-3: Alert Dismissal**: The system shall allow users to dismiss alerts.
4. **FR-4: Alert Snoozing**: The system shall allow users to snooze alerts for a specified duration (e.g., 30 minutes).
5. **FR-5: User Notification**: The system shall notify users of alerts via a notification mechanism (e.g., email, SMS, or in-app notification).
6. **FR-6: Data Storage**: The system shall store glucose readings and alert history for future reference.
7. **FR-7: Configuration**: The system shall allow users to configure alert thresholds and notification preferences.

## Non-Functional Requirements
### Performance
1. **PERF-1: Response Time**: The system shall update glucose readings and generate alerts within 1 minute of a new reading.
2. **PERF-2: Data Retrieval**: The system shall retrieve stored glucose readings and alert history within 500 ms.

### Security
1. **SEC-1: Data Encryption**: The system shall encrypt stored glucose readings and alert history using a secure encryption algorithm (e.g., AES).
2. **SEC-2: Authentication**: The system shall implement user authentication to restrict access to authorized users.

### Reliability
1. **REL-1: Uptime**: The system shall maintain an uptime of at least 99.9% to ensure continuous monitoring and alerting.
2. **REL-2: Error Handling**: The system shall handle errors and exceptions gracefully, ensuring that the system remains functional even in case of errors.

## Constraints
1. **CON-1: Python Version**: The system shall be developed using Python 3.9 or later.
2. **CON-2: Dependency Management**: The system shall use pip for dependency management.
3. **CON-3: Testing Framework**: The system shall use Pytest as the testing framework.

## Assumptions
1. **ASM-1: User Input**: Users will input accurate and consistent glucose readings.
2. **ASM-2: Network Connectivity**: The system will have stable network connectivity to send notifications and store data.
3. **ASM-3: Hardware Compatibility**: The system will be deployed on hardware that meets the minimum requirements for the Python version and dependencies used.
