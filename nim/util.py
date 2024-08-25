import re


def extract_last_number(text):
    # 使用正则表达式来查找所有的数字段
    matches = re.findall(r'\d+', text)
    if matches:
        return matches[-1]  # 返回最后一个匹配的数字段
    else:
        return None


def extract_last_paragraph(text):
    return text.split('\n\n')[-1]
