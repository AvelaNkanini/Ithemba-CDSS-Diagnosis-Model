### Cancer Prediction API (FastAPI + XGBoost)
---
This project provides a **Machine Learning API** built with FastAPI for predicting cancer types based on user-provided symptoms.
It uses an XGBoost classifier and includes a pre-trained model for demonstration purposes.

#### Features
---
- RESTful API built with FastAPI

- Predicts cancer type from user symptoms

- JSON-based input/output

- Easy to test with Swagger UI or Postman

- Ready for integration with web or mobile frontends

### Model Screenshots
---

<table>
  <tr>
    <td><img width="990" height="555" alt="image" src="https://github.com/user-attachments/assets/11b929f2-3243-41b5-967e-a9c619c6bc24" />
    </td>
    <td><img width="987" height="524" alt="image" src="https://github.com/user-attachments/assets/7217daf1-f2ef-4c8f-a64e-2fcdb69a8305" />
  </td>
  </tr>
  <tr>
    <td><img width="996" height="556" alt="image" src="https://github.com/user-attachments/assets/06877824-96d8-4b0e-9e94-ad40b0c82c9f" />
</td>
    <td><img width="996" height="557" alt="image" src="https://github.com/user-attachments/assets/03f86941-36e9-415b-a3d4-a1cca9c93f17" />
</td>
  </tr>
</table>

---

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
You can now interact with the model using 2 methods:

🔹 Option 1: Swagger UI

Visit:

  http://127.0.0.1:8000/docs

This will open an interactive web interface where you can test predictions easily.

🔹 Option 2: ReDoc

Visit:

  http://127.0.0.1:8000/redoc

This provides a clean documentation view of all endpoints.

