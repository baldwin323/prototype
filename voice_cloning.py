```python
import os
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
from tensorflow.keras.callbacks import ModelCheckpoint
from pydub import AudioSegment
from python_speech_features import mfcc

class VoiceCloning:
    def __init__(self, ai_clone):
        self.ai_clone = ai_clone
        self.model = self.build_model()

    def build_model(self):
        model = Sequential()
        model.add(LSTM(256, input_shape=(None, 13), return_sequences=True))
        model.add(LSTM(256, return_sequences=True))
        model.add(Dense(256, activation='relu'))
        model.add(Dense(1, activation='linear'))
        model.compile(loss='mse', optimizer='adam')
        return model

    def train(self, voice_samples, epochs=100):
        voice_samples = np.array(voice_samples)
        X, y = voice_samples[:, :-1], voice_samples[:, -1]
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        checkpoint = ModelCheckpoint('voice_model.h5', monitor='val_loss', verbose=1, save_best_only=True, mode='min')
        self.model.fit(X_train, y_train, epochs=epochs, callbacks=[checkpoint], validation_data=(X_test, y_test))

    def clone_voice(self, voice_sample):
        voice_sample = np.array(voice_sample).reshape(1, -1, 13)
        cloned_voice = self.model.predict(voice_sample)
        return cloned_voice

    def load_voice_samples(self, voice_directory):
        voice_samples = []
        for filename in os.listdir(voice_directory):
            if filename.endswith('.wav'):
                audio = AudioSegment.from_wav(os.path.join(voice_directory, filename))
                mfcc_features = mfcc(audio.get_array_of_samples(), audio.frame_rate)
                voice_samples.append(mfcc_features)
        return voice_samples

ai_clone = "ai_clone"
voice_cloning = VoiceCloning(ai_clone)
voice_samples = voice_cloning.load_voice_samples('voice_samples')
voice_cloning.train(voice_samples)
```
