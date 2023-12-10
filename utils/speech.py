import dashscope
from dashscope.audio.tts import SpeechSynthesizer, ResultCallback
import pyaudio


class CustomSpeechCallback(ResultCallback):
    _player = None
    _stream = None

    def on_open(self):
        self._player = pyaudio.PyAudio()
        self._stream = self._player.open(
            format=pyaudio.paInt16,
            channels=1,
            rate=48000,
            output=True
        )

    def on_error(self, response):
        print('Speech synthesizer failed, response is %s' % (str(response)))

    def on_event(self, result):
        if result.get_audio_frame() is not None:
            self._stream.write(result.get_audio_frame())


class Speech:
    # 使用语音合成, 朗读LLM的回复

    def __init__(self, api_key: str, model: str = "sambert-zhiwei-v1"):
        dashscope.api_key = api_key
        self.api_key = api_key
        self.model = model
        self.callback = CustomSpeechCallback()

    def speak(self, text: str):
        SpeechSynthesizer.call(
            model=self.model,
            text=text,
            sample_rate=48000,
            format="pcm",
            callback=self.callback
        )
