# Python Demo Application for BTP Deployment

A simple Flask web application designed to demonstrate automated deployment to SAP BTP Cloud Foundry using the BTP Deployment Agent.

## Features

- ✅ Single-page web application with beautiful UI
- ✅ Flask server
- ✅ Health check endpoint
- ✅ Cloud Foundry ready with Gunicorn
- ✅ Auto-detected by BTP Deployment Agent

## Files Structure

```
python-demo/
├── app.py            # Flask application with embedded HTML
├── requirements.txt  # Python dependencies
├── Procfile          # Cloud Foundry process definition
├── .gitignore        # Git ignore file
└── README.md         # This file
```

## Local Testing

1. Create a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:
   ```bash
   python app.py
   ```

4. Open your browser:
   ```
   http://localhost:8080
   ```

## Deployment to SAP BTP

### Using the BTP Deployment Agent

1. Push this code to a GitHub repository

2. Use the BTP Deployment Agent at `http://localhost:3000`

3. Enter your repository URL and BTP credentials

4. The agent will automatically:
   - Clone the repository
   - Detect it as a Python application (via requirements.txt)
   - Generate a Cloud Foundry manifest.yml
   - Deploy to your BTP Cloud Foundry environment

### Manual Deployment

If you prefer to deploy manually:

1. Login to Cloud Foundry:
   ```bash
   cf login -a <API_ENDPOINT>
   ```

2. Push the application:
   ```bash
   cf push python-demo
   ```

## Endpoints

- `/` - Main application page
- `/health` - Health check endpoint (returns JSON with status and Python version)

## Requirements

- Python 3.8 or higher
- pip package manager
- SAP BTP Cloud Foundry account (for deployment)

## Technology Stack

- **Runtime:** Python 3.8+
- **Framework:** Flask 3.0.0
- **WSGI Server:** Gunicorn 21.2.0
- **Deployment:** Cloud Foundry

## Environment Variables

The application automatically uses the `PORT` environment variable provided by Cloud Foundry. Locally, it defaults to port 8080.

## Cloud Foundry Configuration

The `Procfile` specifies how Cloud Foundry should run the application:
```
web: gunicorn app:app --bind 0.0.0.0:$PORT
```

This uses Gunicorn as the production WSGI server, which is the recommended way to run Flask applications in production.

## License

MIT
