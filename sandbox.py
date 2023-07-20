```python
import os
from ai_clone import ai_clone
from api_integration import integrateAPI
from user_credentials import user_credentials

class Sandbox:
    def __init__(self):
        self.ai_clone = ai_clone
        self.user_credentials = user_credentials

    def setup_sandbox(self):
        os.environ['SANDBOX'] = 'True'
        self.ai_clone.setup_clone()
        self.integrateAPIs()

    def integrateAPIs(self):
        for credential in self.user_credentials:
            integrateAPI(credential)

    def teardown_sandbox(self):
        os.environ['SANDBOX'] = 'False'
        self.ai_clone.teardown_clone()

sandbox = Sandbox()
```