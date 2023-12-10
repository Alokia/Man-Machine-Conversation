import dashscope
from dashscope.audio.asr import Recognition
from http import HTTPStatus


class Recognize:
    # 读取 wav 音频文件, 返回识别结果

    def __init__(self, api_key: str, model: str = "paraformer-realtime-v1"):
        dashscope.api_key = api_key

        self.recognition = Recognition(
            model=model,
            format="wav",
            sample_rate=16000,
            callback=None
        )

    def call(self, file_path: str):
        result = self.recognition.call(file_path)
        if result.status_code != HTTPStatus.OK:
            raise RuntimeError(f"Recognition failed, status code is {result.status_code}")
        result = result["output"]["sentence"][0]["text"]
        return result
