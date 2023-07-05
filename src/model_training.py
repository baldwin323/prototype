```python
import openai
from src.chat_history.upload_chat_history import creator_chat_history
from src.error_handling import handleError

def trainModel():
    try:
        # Load the API key from an environment variable
        openai.api_key = api_keys['openai']

        # Load the creator's chat history
        chat_history = creator_chat_history

        # Train the model on the creator's chat history
        model = openai.Completion.create(
            engine="text-davinci-002",
            prompt=chat_history,
            temperature=0.5,
            max_tokens=100
        )

        # Save the trained model
        with open('trained_model.pkl', 'wb') as f:
            pickle.dump(model, f)

        print("Model training successful.")
        return model

    except Exception as e:
        handleError(e)
```