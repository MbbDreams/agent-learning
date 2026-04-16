from langchain_core.prompts import (
PromptTemplate,
HumanMessagePromptTemplate,
SystemMessagePromptTemplate,
ChatPromptTemplate
)

# template = "tell me a {adjective} joke about {content}"
# prompt = PromptTemplate.from_template(template)
# text = prompt.format(adjective = "funny", content = "chickens")
# print(text)
#
# promtp1 = PromptTemplate(
#     input_variables=["topic", "level"],
#     template="tell me a {topic} joke about {level}"
# )
# text2 = promtp1.format(topic = "funny", level = "chickens")
# print(text2)

system = SystemMessagePromptTemplate.from_template("You are an English tutor who explains grammar clearly.")
human = HumanMessagePromptTemplate.from_template( "Explain this sentence: {sentence}")
chat_prompt = ChatPromptTemplate.from_messages([system, human])
chat_prompt.format_prompt(sentence ="She had gone before I arrived." ).to_messages()