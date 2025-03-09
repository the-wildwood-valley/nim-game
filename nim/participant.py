import os

from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://api.deepseek.com",
)


class Participant:
    def __init__(self, role, name):
        self.game = None
        self.role = role
        self.name = name
        self.history = []

    def enter_game(self, game):
        self.game = game
        self.game.enter_game(self)

    def clear_history(self):
        self.history = []

    def act(self, action, content, scope="public"):
        role = f"{self.role} {self.name}"
        content = f"{action}：{content}"
        self.history.append({"role": role, "content": content})

        if scope == "public":
            print(f"{role} {content}")
            self.game.play(self, content)

    def observed(self, event):
        self.act("观察到", event, scope="private")

    def talk(self, content):
        self.act("说", content)

    def take(self, content):
        self.act("取走", content)

    def think(self, content):
        self.act("思考", content, scope="private")

    def ask(self, context, question):
        content = f"给定了如下的情况—\n\n{context}\n\n我问一下自己—{question}"
        self.think(content)

    def answer(self, position="最后一行", target="数量"):
        prompt = f"我在脑海中分析并在{position}明确给出{target}作为最终答案……"

        messages = []
        for event in self.history:
            role = event["role"]
            content = event["content"]
            content = f"{role}：{content}"
            messages.append({"role": 'user', "content": content})
        role = f"{self.role} {self.name}"
        prompt = f"{role}：{prompt}"
        messages.append({"role": 'user', "content": prompt})

        completion = client.chat.completions.create(
            model="deepseek-reasoner",
            messages=merge_consecutive_messages(messages),
            temperature=0.3,
        )
        complete_message = f"{prompt}{completion.choices[0].message.content}"
        print('--------------------------------------')
        print(complete_message)
        print('--------------------------------------')

        return complete_message


def merge_consecutive_messages(messages, target_role="user", separator="\n"):
    if not messages:
        return []

    merged = []
    current_msg = None  # Tracks the message being built

    for msg in messages:
        role = msg["role"]
        content = msg["content"].strip()

        # Merge if same target role and consecutive
        if role == target_role and current_msg and current_msg["role"] == role:
            current_msg["content"] += f"{separator}{content}"
        # Start new message group
        else:
            if current_msg:
                merged.append(current_msg)
            current_msg = {"role": role, "content": content}

    # Add the last accumulated message
    if current_msg:
        merged.append(current_msg)

    return merged

