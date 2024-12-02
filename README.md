
# Customer Chat Assistant

This application helps businesses provide automated responses to customer inquiries using OpenAI's ChatGPT API. The system customizes responses based on the subject matter or product relevant to the user's needs.

## Features

- AI-driven customer response system using ChatGPT.
- Context-based communication for tailored responses.
- Chat history storage for reference and analysis.
- Easy-to-use API built with FastAPI.

---

## Installation

### Prerequisites

Ensure you have the following installed:

- Python 3.10 or higher
- Pip (Python package manager)
- Git

### Steps

1. Clone the repository:
   ```bash
   git clone git@github.com:georgegoldman/aer.git
   cd aer
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up the database:
   ```bash
   python -m app.database
   ```

4. Set up your OpenAI API key:
   - Create a `.env` file in the root directory.
   - Add your OpenAI API key:
     ```
     OPENAI_API_KEY=your-api-key-here
     ```

5. Run the server:
   ```bash
   uvicorn app.main:app --reload
   ```

---

## Usage

### API Endpoints

- **Root**: `GET /`
  - Health check endpoint.

- **Send Message**: `POST /api/v1/send-message`
  - **Request Body**:
    ```json
    {
      "user_id": "123",
      "context": "E-commerce chatbot",
      "message": "What is the price of a laptop?"
    }
    ```
  - **Response**:
    ```json
    {
      "response": "The price of a laptop starts at $500."
    }
    ```

### Testing

You can test the API using tools like **Postman** or **cURL**.

Example:
```bash
curl -X POST "http://127.0.0.1:8000/api/v1/send-message" -H "Content-Type: application/json" -d '{"user_id": "123", "context": "E-commerce chatbot", "message": "What is the price of a laptop?"}'
```

---

## Project Structure

```
app/
├── main.py            # Application entry point
├── models.py          # Database models
├── schemas.py         # Pydantic models for request/response validation
├── database.py        # Database configuration
├── services.py        # ChatGPT interaction logic
├── routers/
│   └── chat.py        # API routes for chat functionality
```

---

## Deployment

### Using Docker

1. Build the Docker image:
   ```bash
   docker build -t customer-chat-assistant .
   ```

2. Run the container:
   ```bash
   docker run -p 8000:8000 customer-chat-assistant
   ```

### Deployment Options

- **Cloud Providers**: AWS, Heroku, Google Cloud.
- **Container Orchestration**: Docker Compose or Kubernetes.

---

## Contributing

Contributions are welcome! Follow these steps:

1. Fork the repository.
2. Create a feature branch:
   ```bash
   git checkout -b feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Description of changes"
   ```
4. Push to the branch:
   ```bash
   git push origin feature-name
   ```
5. Open a pull request.

---

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [OpenAI API](https://openai.com/api/)
