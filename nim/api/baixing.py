import requests


def get_response(text):
    import time
    import requests
    time.sleep(0.5)
    try:
        response = requests.post(
            'https://gpt.baixing.com',
            json={
                "p": text,
                "k": key,
            }
        )
        if response.status_code != 200:
            return "……"
        resp = response.json()
        text = resp['data'] or ""
        while "----想要和机器人一对一聊天？" in text:
            text = text.replace("----想要和机器人一对一聊天？", "")
        while "关注微信公众号BaixingAI" in text:
            text = text.replace("关注微信公众号BaixingAI", "")
        while "免费体验" in text:
            text = text.replace("免费体验", "")
        if text == "":
            text = "……"
        return text
    except Exception as e:
        return "……"
