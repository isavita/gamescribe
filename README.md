# Gamescribe

Gamescribe generates 2D game concepts based on user-uploaded images and text input using AI. **This project was created for the Mistral London Hackathon on October 5-6, 2024**.

## Quick Start

1. Clone the repository:
   ```
   git clone https://github.com/isavita/gamescribe.git
   cd gamescribe
   ```

2. Set up a virtual environment (optional):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set your Mistral API key:
   ```
   export MISTRAL_API_KEY=your_mistral_api_key
   ```

5. Run the application:
   ```
   python main.py
   ```

6. Open `http://localhost:5000` in your browser.

## Usage

Upload images, enter your game idea, and click "Generate Game Idea" to get an AI-generated game concept.

## Running in Debug Mode

To run the application in debug mode, which provides more detailed logging, use:

```
DEBUG=true python main.py
```

This will enable verbose logging in the terminal, showing detailed information about the application's operations.
