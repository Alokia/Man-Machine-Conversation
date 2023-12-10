from utils import Speech, LLMQuery, RecordAudio, Recognize


def voice_chat(api_key):
    # 语音对话，需要录音设备
    speech = Speech(api_key=api_key)
    llm = LLMQuery(template_path="template.txt", api_key=api_key)
    record = RecordAudio(save_path="input.wav")
    recognize = Recognize(api_key=api_key)

    while True:
        input()  # 按下回车键开始录音
        record.start()
        input()  # 按下回车键结束录音
        record.stop()
        record.save()

        text = recognize.call("input.wav")
        print(">>", text)

        response = llm.query(text)
        print(response)
        speech.speak(response)


def text_chat(api_key):
    speech = Speech(api_key=api_key)
    llm = LLMQuery(template_path="template.txt", api_key=api_key)

    while True:
        text = input(">> ")
        response = llm.query(text)
        print(response)
        speech.speak(response)

        if text == "再见":
            break


if __name__ == '__main__':
    api_key = "your api key"

    # voice_chat(api_key)
    text_chat(api_key)
