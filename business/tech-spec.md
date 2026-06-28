# tech-spec.md
## Stack
* Language: Python 3.10
* Framework: FastAPI 0.92.0
* Runtime: Python 3.10 asyncio
* Database: PostgreSQL 14.2
* AI Library: TensorFlow 2.10.0
* Sensor Integration: PySerial 3.5

## Hosting
* Primary Platform: AWS (Free Tier)
* Secondary Platform: Google Cloud Platform (Free Tier)
* Containerization: Docker 20.10.17
* Orchestration: Kubernetes 1.24.3

## Data Model
### Tables/Collections
#### Users
| Field | Type | Description |
| --- | --- | --- |
| id | UUID | Unique User ID |
| name | String | User Name |
| email | String | User Email |
| password | String | User Password (Hashed) |
#### Readings
| Field | Type | Description |
| --- | --- | --- |
| id | UUID | Unique Reading ID |
| user_id | UUID | Foreign Key referencing Users table |
| blood_sugar_level | Float | Blood Sugar Level reading |
| timestamp | DateTime | Timestamp of reading |
#### Sensors
| Field | Type | Description |
| --- | --- | --- |
| id | UUID | Unique Sensor ID |
| user_id | UUID | Foreign Key referencing Users table |
| sensor_type | String | Type of sensor (e.g. optical, electrical) |
| calibration_data | JSON | Sensor calibration data |

## API Surface
### Endpoints
1. **POST /users** - Create a new user
	* Method: POST
	* Path: /users
	* Purpose: Create a new user account
	* Request Body: { name, email, password }
2. **GET /users/{user_id}** - Get user details
	* Method: GET
	* Path: /users/{user_id}
	* Purpose: Retrieve user details
	* Response: { id, name, email }
3. **POST /readings** - Create a new blood sugar reading
	* Method: POST
	* Path: /readings
	* Purpose: Create a new blood sugar reading
	* Request Body: { user_id, blood_sugar_level, timestamp }
4. **GET /readings/{user_id}** - Get user's blood sugar readings
	* Method: GET
	* Path: /readings/{user_id}
	* Purpose: Retrieve user's blood sugar readings
	* Response: [ { id, user_id, blood_sugar_level, timestamp } ]
5. **POST /sensors** - Create a new sensor
	* Method: POST
	* Path: /sensors
	* Purpose: Create a new sensor
	* Request Body: { user_id, sensor_type, calibration_data }
6. **GET /sensors/{sensor_id}** - Get sensor details
	* Method: GET
	* Path: /sensors/{sensor_id}
	* Purpose: Retrieve sensor details
	* Response: { id, user_id, sensor_type, calibration_data }
7. **PUT /sensors/{sensor_id}** - Update sensor calibration data
	* Method: PUT
	* Path: /sensors/{sensor_id}
	* Purpose: Update sensor calibration data
	* Request Body: { calibration_data }
8. **DELETE /sensors/{sensor_id}** - Delete a sensor
	* Method: DELETE
	* Path: /sensors/{sensor_id}
	* Purpose: Delete a sensor
9. **GET /analytics** - Get analytics data
	* Method: GET
	* Path: /analytics
	* Purpose: Retrieve analytics data
	* Response: { user_id, average_blood_sugar_level, std_dev_blood_sugar_level }
10. **POST /analytics** - Create a new analytics task
	* Method: POST
	* Path: /analytics
	* Purpose: Create a new analytics task
	* Request Body: { user_id, task_type }

## Security Model
* Authentication: OAuth 2.0 with JWT tokens
* Authorization: Role-Based Access Control (RBAC)
* Secrets Management: AWS Secrets Manager
* IAM: AWS IAM roles and policies

## Observability
* Logging: AWS CloudWatch Logs
* Metrics: AWS CloudWatch Metrics
* Tracing: AWS X-Ray

## Build/CI
* Build Tool: Docker 20.10.17
* CI/CD Pipeline: GitHub Actions 2.0
* Testing Framework: Pytest 7.1.2
* Code Quality: SonarQube 9.9.0
* Deployment: AWS Elastic Beanstalk 3.0.1