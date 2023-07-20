```python
import tkinter as tk
from tkinter import messagebox
import backend
import api_integration
import ai_clone
import chat_room
import sandbox
import financial_api
import 3d_avatar
import debugger
import trainer
import sms_connector
import voice_cloning
import sales
import relationship_builder
import content_seller
import art_seller

class GUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Prompt.md")
        self.create_widgets()

    def create_widgets(self):
        self.chatRoom = chat_room.ChatRoom(self.root)
        self.sandbox = sandbox.Sandbox(self.root)
        self.avatarDisplay = 3d_avatar.AvatarDisplay(self.root)
        self.smsConnector = sms_connector.SMSConnector(self.root)
        self.voiceCloning = voice_cloning.VoiceCloning(self.root)

        self.chatRoom.pack()
        self.sandbox.pack()
        self.avatarDisplay.pack()
        self.smsConnector.pack()
        self.voiceCloning.pack()

    def integrateAPI(self):
        api_integration.integrateAPI()

    def cloneCreator(self):
        ai_clone.cloneCreator()

    def communicate(self):
        ai_clone.communicate()

    def debug(self):
        debugger.debug()

    def train(self):
        trainer.train()

    def connectSMS(self):
        sms_connector.connectSMS()

    def makeCall(self):
        sms_connector.makeCall()

    def cloneVoice(self):
        voice_cloning.cloneVoice()

    def sellContent(self):
        content_seller.sellContent()

    def sellArt(self):
        art_seller.sellArt()

    def buildRelationship(self):
        relationship_builder.buildRelationship()

if __name__ == "__main__":
    root = tk.Tk()
    gui = GUI(root)
    root.mainloop()
```