### Cancer Prediction API (FastAPI + XGBoost)
---
This project provides a machine learning API built with FastAPI for predicting cancer types based on user-provided symptoms.
It uses an XGBoost classifier and includes a pre-trained model for demonstration purposes.

#### Features
---
- RESTful API built with FastAPI

- Predicts cancer type from user symptoms

- JSON-based input/output

- Easy to test with Swagger UI or Postman

- Ready for integration with web or mobile frontends

### Installation Guide
---
Follow these steps carefully to set up and run the project on your local machine.

#### Create a Virtual Environment

A virtual environment keeps dependencies isolated.
```bash
python -m venv venv
```
#### Activate the Virtual Environment

```bash
venv\Scripts\activate
```
When active, your terminal prompt should show:
```bash
(venv) >
```
#### Install Required Dependencies
```bash
pip freeze > requirements.txt
```
#### Run the FastAPI Server
```bash
uvicorn main:app --reload
```

You should see something like:

INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)

#### How to Test the Model
---
You can now interact with your model using 3 methods:

🔹 Option 1: Swagger UI

Visit:

  http://127.0.0.1:8000/docs

This will open an interactive web interface where you can test predictions easily.

🔹 Option 2: ReDoc

Visit:

  http://127.0.0.1:8000/redoc

This provides a clean documentation view of all endpoints.

