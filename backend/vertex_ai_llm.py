from vertexai.language_models import TextGenerationModel

def query_llm(question, context):
    model = TextGenerationModel.from_pretrained("text-bison")
    prompt = f"Answer based on context:\n{context}\n\nQuestion: {question}"
    response = model.predict(prompt=prompt, temperature=0.3, max_output_tokens=512)
    return response.text