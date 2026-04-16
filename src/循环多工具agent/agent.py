from llm import call_llm
from parser import parse_action
from tools import TOOLS

PROMPT = """
你是一个智能 Agent，可以使用工具。

可用工具：
- calculator：数学计算
- weather：查询天气

【规则】：
1. 必须严格按照格式输出
2. 不要输出 <think>
3. Action 只能是工具名或 "none"
4. 如果已经可以回答，直接输出 Final Answer

格式：

Question: {input}

Thought: 思考下一步
Action: 工具名 或 "none"
Action Input: 输入内容

Observation: 工具返回结果

Thought: ...
Final Answer: 最终答案

开始。
"""

def run_agent(question: str, max_steps=5):
    prompt = PROMPT.format(input=question)

    history = ""  # 保存上下文

    for step in range(max_steps):
        print(f"\n===== 第 {step+1} 轮 =====")

        full_prompt = prompt + "\n" + history

        output = call_llm(full_prompt)
        print("🧠 LLM输出:\n", output)

        action, action_input, final_answer = parse_action(output)

        # ✅ 如果已经结束
        if final_answer:
            print("\n✅ 最终答案:\n", final_answer)
            return final_answer

        # ❌ 没有 Action
        if not action:
            print("⚠️ 未解析到 Action")
            return output

        # ❌ 不调用工具
        if action == "none":
            print("\n✅ 直接回答:\n", output)
            return output

        # ❌ 工具不存在
        if action not in TOOLS:
            print(f"⚠️ 未知工具: {action}")
            return output

        # ✅ 调用工具
        result = TOOLS[action](action_input)
        print("🔧 工具结果:", result)

        # 🔥 关键：更新 history
        history += output + f"\nObservation: {result}\n"

    print("⚠️ 达到最大步数")
    return "未能完成任务"