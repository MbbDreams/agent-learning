from llm import call_llm
from parser import parse_action
from tools import TOOLS
print(TOOLS)
PROMPT = """
你是一个智能 Agent，可以使用工具。

可用工具：
- calculator：数学计算
- weather：查询天气

【规则】：
1. 必须严格按照格式输出
2. 不要输出 <think>
3. Action 只能是工具名或 "none"

格式：

Question: {input}

Thought: 分析问题
Action: 工具名 或 "none"
Action Input: 输入内容

Observation: 工具返回结果

Thought: ...
Final Answer: 最终答案

开始。
"""

def run_agent(question):
    prompt = PROMPT.format(input=question)
    output = call_llm(prompt)
    print("LLM输出:\n", output)
    action,action_input = parse_action(output)
    if action in TOOLS:
        tool = TOOLS[action](action_input)
        #把结果投入回模型
        new_prompt = prompt + "\n" + output + f"\nObservation: {output}\n"
        final_output = call_llm(new_prompt)
        print("\n最终结果:\n", final_output)
        return final_output
    return output