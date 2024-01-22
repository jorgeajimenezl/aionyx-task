# Aionyx Task

<div style="text-align: center;">
    <img src="images/logo.png" alt="Logo" width="100px">
</div>

Development of a Middleware API for AI Models

---

## Run Locally
Create an .env file with the necessary API keys. I should look like this:
```
OPENAI_API_KEY=...
ANTHROPIC_API_KEY=...
...
```

To run locally in debug mode run:

```
cd ./aionyx_task
python -m virtualenv .venv && source .venv/activate
uvicorn app.api:app --reload
```
Open your browser to http://localhost:8000/docs to view the OpenAPI UI.
For an alternate view of the docs navigate to http://localhost:8000/redoc

# Logo

The logo was made using Microsoft Designer 😀.