# Healthcare

This project serves an API to fetch and create members. It is also capable of
creating and batch inserting members by uploading a CSV file with the following columns:

* First Name
* Last Name
* Phone Number
* Client Member ID
* Account ID

CSV files are processed in the backround by chunking the data and processing distributed 
tasks using Celery.

## Run Locally

Clone the project

```bash
  git clone https://github.com/austenwood/healthcare.git
```

Go to the project directory

```bash
  cd healthcare
```

Start the Docker containers

```bash
  docker compose up
```

## Demo

Once the docker containers are up you can reach the React client at http://localhost:3000/.

You can monitor Celery by visiting the Flower dashboard at http://localhost:5555/.
## Running Tests

To run tests with coverage, run the following command

```bash
  docker compose exec web pytest -p np:warnings --cov=.
```

## API Reference

#### Get Members

```http
  GET /api/members/?account_id=&id=&phone_number=&client_member_id=
```

#### Create a new Member

```http
  POST /api/members/
```

#### Upload CSV File

```http
  POST /api/upload/
```