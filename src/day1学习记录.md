# 🚀 Agent 学习 Day 1 总结（ReAct + 多工具 + 循环）

## 📌 今日目标

构建一个**真正可用的 Agent（而不是简单调用 LLM）**，实现：

* 自动判断是否使用工具
* 支持多个工具
* 支持多轮推理（循环）
* 输出可控（通过 Prompt 约束）

---

# 🧠 一、Agent 核心架构（已掌握）

## ✅ Agent = 三层结构

LLM（大脑） + Tools（工具） + Orchestrator（调度代码）

### 1️⃣ LLM（大脑）

* 负责：思考（Thought）、决策（Action）
* 本质：概率预测模型（预测下一个 token）

### 2️⃣ Tools（工具）

* 本质：Python 函数
* 示例：

  * calculator（计算）
  * weather（天气查询）

### 3️⃣ Orchestrator（控制器）

* 负责：

  * 调用 LLM
  * 解析输出
  * 执行工具
  * 维护上下文（history）

---

# 🔁 二、ReAct 核心机制（重点）

## 📌 模式

Question
↓
Thought（思考）
↓
Action（决定工具）
↓
Action Input（工具输入）
↓
Observation（工具结果）
↓
循环...
↓
Final Answer（最终答案）

---

## 🧠 本质

> 用 Prompt 让 LLM 模拟“会思考 + 会用工具的人”

---

# 🔧 三、已实现能力

## ✅ 1. 多工具支持

TOOLS = {
"calculator": calculator,
"weather": weather,
}

---

## ✅ 2. 自动工具选择

Action: calculator

---

## ✅ 3. 工具执行

result = TOOLS[action](action_input)

---

## ✅ 4. 循环 Agent（关键）

for step in range(max_steps):

实现：

* 多轮推理
* 多次工具调用
* 自主结束（Final Answer）

---

## ✅ 5. 上下文记忆（伪 Memory）

history += output + "\nObservation: " + result + "\n"

👉 本质：

* LLM 无记忆
* 通过 Prompt 拼接模拟“记忆”

---

# 🧾 四、Prompt 设计原则（非常关键）

## ✅ 强约束

必须严格按照格式输出

## ✅ 固定结构

Thought:
Action:
Action Input:

## ✅ 禁止项

不要输出 <think>

---

## 🧠 原理

> Prompt = 控制 LLM 行为的“程序”

---

# ⚠️ 五、踩坑总结

## ❌ 问题1：输出 `<think>`

原因：模型暴露内部推理
解决：Prompt 强约束禁止输出

## ❌ 问题2：无法解析 Action

原因：输出格式不稳定
解决：

* 固定字段（英文）
* 强约束 Prompt

## ❌ 问题3：乱调用工具

原因：没有明确规则
解决：如果不需要工具，Action 必须为 "none"

---

# 🧠 六、关键认知（非常重要）

## ❗ Agent ≠ 模型能力

Agent 的能力来自：

* Prompt 设计
* 工具系统
* 控制逻辑

## ❗ LLM 不会真的“调用工具”

实际流程：

1. LLM 输出：
   Action: calculator
2. 程序解析
3. 调用 Python 函数
4. 返回结果（Observation）

---

# 📊 七、当前能力评估

## ✅ 已达到

* 多工具 Agent
* 自动决策
* 循环推理
* 基础 Memory

## ❌ 还不足

* 解析不稳定（依赖正则）
* 无结构化输出
* 无长期记忆
* 无工程化能力

---

# 🚀 八、下一步计划（Day 2）

## 🔥 JSON Agent（工程级升级）

目标：

* 替代正则解析
* 使用结构化输出
* 提升稳定性

示例：

{
"action": "calculator",
"input": "2+2"
}

收益：

* 稳定性提升
* 易于对接 API / 前端
* 接近生产级 Agent

---

# 🎯 九、学习进度（阶段定位）

当前处于：阶段2：ReAct Agent（中后期）
下一阶段：阶段3：工程化 Agent

---

# 💡 十、一句话总结

今天完成了从“调用 LLM”到“构建 Agent”的关键跃迁，实现了一个可循环、多工具、可决策的智能体系统。
