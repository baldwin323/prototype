```python
import os
import json
from collections import Counter
from typing import List, Dict

class ChatHistoryAnalysis:
    def __init__(self, chat_history_path: str):
        self.chat_history_path = chat_history_path
        self.creator_chat_history = self.load_chat_history()

    def load_chat_history(self) -> List[Dict[str, str]]:
        with open(self.chat_history_path, 'r') as file:
            return json.load(file)

    def analyze_chat_history(self) -> Dict[str, int]:
        word_count = Counter()
        for chat in self.creator_chat_history:
            message = chat.get('message', '')
            words = message.split()
            word_count.update(words)
        return dict(word_count)

    def save_analysis_result(self, result: Dict[str, int], output_path: str):
        with open(output_path, 'w') as file:
            json.dump(result, file, indent=4)

if __name__ == "__main__":
    chat_history_path = os.path.join(os.getcwd(), 'chat_history.json')
    analysis_output_path = os.path.join(os.getcwd(), 'chat_history_analysis.json')

    chat_history_analysis = ChatHistoryAnalysis(chat_history_path)
    analysis_result = chat_history_analysis.analyze_chat_history()
    chat_history_analysis.save_analysis_result(analysis_result, analysis_output_path)
```