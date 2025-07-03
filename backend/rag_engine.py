from langchain.vectorstores import Chroma
from langchain.embeddings import VertexAIEmbeddings
from langchain.document_loaders import PyPDFLoader

persist_dir = "chroma_db"
loader = PyPDFLoader("data/sample_docs/demo.pdf")
docs = loader.load()

embedding_model = VertexAIEmbeddings()
vectorstore = Chroma.from_documents(docs, embedding_model, persist_directory=persist_dir)

def retrieve_docs(query):
    retriever = vectorstore.as_retriever(search_type="similarity", k=3)
    docs = retriever.get_relevant_documents(query)
    return "\n".join([doc.page_content for doc in docs])