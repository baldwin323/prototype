```python
import os
import shutil

def upload_chat_history(creator_chat_history, destination_folder):
    """
    Function to upload the creator's chat history to a training history folder.
    """
    try:
        # Check if the destination folder exists, if not, create it.
        if not os.path.exists(destination_folder):
            os.makedirs(destination_folder)

        # Copy the chat history file to the destination folder.
        shutil.copy(creator_chat_history, destination_folder)

        print(f"Chat history uploaded successfully to {destination_folder}")

    except Exception as e:
        print(f"An error occurred while uploading chat history: {str(e)}")

# Example usage:
# upload_chat_history("path/to/chat_history.txt", "path/to/training_history_folder")
```