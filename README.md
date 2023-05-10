# Stock Market API Service

This project is a Django REST framework application that provides an API to fetch stock market information from Alpha Vantage. It implements user authentication via API keys and supports API throttling.

## Installation

1. Clone the repository:


2. Change to the project directory:

```
cd stock-market-api
```

3. Install the required dependencies:

```
pip install -r requirements.txt
```

4. Run migrations:

```
python manage.py migrate
```

5. Start the development server:

```
python manage.py runserver
```

The API should now be running at `http://localhost:8000`.

## Usage

### Sign up for an API key

To get an API key, make a POST request to the `/signup/` endpoint with your name, last name, and email.

Example using `curl`:

```
curl -X POST -H "Content-Type: application/json" -d '{"name": "John", "last_name": "Doe", "email": "john@example.com"}' http://localhost:8000/signup/
```

The response will include your API key:

```json
{
  "name": "John",
  "last_name": "Doe",
  "email": "john@example.com",
}
```

### Get stock market information

To fetch stock market information for a specific stock symbol, make a GET request to the `/stocks/{symbol}/` endpoint, replacing `{symbol}` with the stock symbol (e.g., AAPL for Apple). Pass your API key in the `API-Key` header.

Example using `curl`:

```
curl -X GET -H "API-Key: ac68cf7b9125482a93e10d8383102428" http://localhost:8000/stocks/AAPL/
```

The response will include the stock market information in JSON format:

```json
{
  "symbol": "AAPL",
  "open": 173.05,
  "high": 173.54,
  "low": 171.6,
  "close": 171.77,
  "variation": -1.73
}
```

## Admin Interface

To access the Django admin interface, visit `http://localhost:8000/admin/`. You will need to create a superuser account to log in.

To create a superuser, run the following command and follow the prompts:

```
python manage.py createsuperuser
```

In the admin interface, you can manage users and view API call logs.

## Testing

To run tests, execute the following command:

```
python manage.py test
```

## Deployment

This project can be deployed on various cloud platforms such as Heroku, Google Cloud, AWS, or Azure. Please refer to the respective platform's documentation for deployment instructions.