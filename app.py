from langchain_google_genai import ChatGoogleGenerativeAI
print("git hubdemo")
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", google_api_key=os.getenv("GOOGLE_API_KEY"))
print(llm.invoke("What is the capital of France?"))