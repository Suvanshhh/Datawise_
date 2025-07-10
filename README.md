# Datawise Dataset Catalog

A fullstack project with a Flask + MongoDB backend and a React frontend for managing datasets and tracking quality logs.

## Setup Instructions

### Backend

1. **Clone the repository**  
   ```bash
   git clone 
   cd backend
   ```

2. **Create and activate a virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure environment variables**  
   - Create a `.env` file in the backend folder with:
     ```
     MONGO_URI="your-mongodb-uri-with-db-name"
     FLASK_ENV=development
     FLASK_APP=app.py
     ```
   - Example for MongoDB Atlas:
     ```
     MONGO_URI="mongodb+srv://username:password@cluster.mongodb.net/mydb?retryWrites=true&w=majority"
     ```

5. **Run the backend server**  
   ```bash
   flask run
   ```
   - By default, the API runs at `http://localhost:5000`

6. **API Documentation**  
   - Visit `http://localhost:5000/apidocs` for interactive Swagger docs.

### Frontend

1. **Navigate to the frontend directory**  
   ```bash
   cd ../frontend
   ```

2. **Install dependencies**  
   ```bash
   npm install
   ```

3. **Configure API endpoint**  
   - For local development, ensure `package.json` includes:
     ```json
     "proxy": "http://localhost:5000"
     ```
   - For production, set the API base URL in `src/api.js`:
     ```javascript
     const API_BASE = "https://your-backend-domain.com";
     ```

4. **Start the React development server**  
   ```bash
   npm start
   ```
   - The app runs at `http://localhost:3000`

5. **Build for production**  
   ```bash
   npm run build
   ```

## Overview of Features

- **Datasets**
  - Create, list, update, and soft-delete datasets.
  - Filter datasets by owner or tag.
- **Quality Logs**
  - Add and view quality logs for each dataset.
  - Status can be PASS or FAIL, with details and timestamp.
- **Validation**
  - Input validation using Marshmallow schemas.
- **API Documentation**
  - Auto-generated Swagger docs (Flasgger).
- **Testing**
  - Includes pytest test cases for main flows.
- **Responsive Frontend**
  - React UI for all dataset and quality log operations.
  - Modern, mobile-friendly CSS.
- **Error Handling**
  - Proper status codes and error messages for all API responses.

## Assumptions Made

- MongoDB URI includes the database name and is provided via environment variables.
- No authentication is required (for demonstration purposes).
- Soft delete is implemented by setting `is_deleted: true` (data is not physically removed).
- The backend and frontend may be deployed separately; API base URL must be configured accordingly.
- All required environment variables are set in deployment environments (not committed to the repo).

## Libraries and Tools Used

| Layer      | Libraries / Tools                         |
|------------|-------------------------------------------|
| Backend    | Flask, PyMongo, Marshmallow, Flasgger, Flask-CORS, python-dotenv, pytest, dnspython |
| Frontend   | React, react-scripts, fetch API, npm      |
| Testing    | pytest                                    |
| Deployment | Railway (example), MongoDB Atlas          |

## Example API Requests

**Create a dataset**
```bash
curl -X POST http://localhost:5000/datasets \
  -H "Content-Type: application/json" \
  -d '{"name": "Sample Dataset", "owner": "alice", "description": "Test data", "tags": ["finance", "2025"]}'
```

**List all datasets**
```bash
curl http://localhost:5000/datasets
```

**Add a quality log**
```bash
curl -X POST http://localhost:5000/datasets//quality-1 \
  -H "Content-Type: application/json" \
  -d '{"status": "PASS", "details": "Initial check passed"}'
```

## Project Structure

```
Datawise/
├── backend/
│   ├── app.py
│   ├── requirements.txt
│   ├── .env
│   ├── routes/
│   ├── services/
│   ├── models/
│   ├── utils/
│   └── tests/
├── frontend/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── ...
└── README.md
```

## Running Tests

- From the `backend/` directory:
  ```bash
  pytest tests/
  ```

## Notes

- For production, ensure secure environment variable management and restrict CORS.
- Update the API base URL in the frontend for your deployed backend.
- For any issues, check backend logs and ensure all services are running and accessible.

