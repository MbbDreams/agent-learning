import re

def parse_action(text: str):
    action_match = re.search(r"Action:\s*(.*)", text)
    input_match = re.search(r"Action Input:\s*(.*)", text)

    action = action_match.group(1).strip() if action_match else None
    action_input = input_match.group(1).strip() if input_match else None

    return action, action_input