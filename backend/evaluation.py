from trulens_eval import Feedback, TruChain
from langchain.chains import LLMChain

llm_chain = LLMChain.from_string("{context}\nQuestion: {question}\nAnswer: {answer}")
feedback = Feedback.openai_qa_eval_v2().on_input_output()
tru = TruChain(chain=llm_chain, app_id="faq-app", feedbacks=[feedback])
