def calculator(expression: str):
    try:
        return str(eval(expression))
    except:
        return "error"
PROMPT = """
你是一个智能 Agent，可以使用工具来解决问题。

你可以使用以下工具：

- calculator：用于数学计算

【重要规则（必须严格遵守）】：
1. 不要输出任何 <think> 或隐藏思考
2. 必须严格按照指定格式输出
3. 不要编造问题
4. 如果不需要工具，Action 必须为 "none"

【输出格式】：

Question: {input}

Thought: 分析问题，决定是否需要使用工具
Action: 工具名称 或 "none"
Action Input: 工具输入内容

（如果调用工具，会得到 Observation）

Observation: 工具返回结果

Thought: 根据结果继续思考
Final Answer: 给出最终答案

现在开始。
"""
from openai import OpenAI

def call_llm(prompt):
    client = OpenAI(
        api_key="sk-lFB02hEtWgkT9Cy38cE6EaBdA64644Bc96E447F93772C7Cf",
        base_url="https://aihubmix.com/v1"
    )
    response = client.chat.completions.create(
        model="coding-minimax-m2.5-free",
        messages=[
            {"role": "user", "content": prompt}
        ]
    )

    return response.choices[0].message.content

import re
# LLM 输出是“字符串”
# 而程序需要“结构化指令”
def parse_action(text):
    action_match = re.search(r"Action:\s*(.*)", text)
    input_match = re.search(r"Action Input:\s*(.*)", text)

    action = action_match.group(1).strip() if action_match else None
    action_input = input_match.group(1).strip() if input_match else None

    return action, action_input

# Agent 主循环（核心）
def run_agent(question):
    prompt = PROMPT.format(input=question)
    # 第一次让 llm决策
    output = call_llm(prompt)
    action,action_input = parse_action(output)
    if action == "calculator":
        result = calculator(action_input)
        #再把结果喂回去
        new_prompt = prompt + "\n" + output + f"\nObservation: {result}\n"
        final_output = call_llm(new_prompt)
        # print(final_output)
        return final_output
    return output
if __name__ == '__main__':
    print(run_agent("2+2是多少？"))