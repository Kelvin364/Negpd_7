# import openai

# class ChatGPT:
#     def __init__(self, api_key):
#         self.api_key = api_key
#         openai.api_key = self.api_key

#     def get_health_tips(self):
#         return "Here are some health tips: Stay hydrated, eat balanced meals, and exercise regularly."

#     def chat(self, query):
#         try:
#             response = openai.Completion.create(
#                 model="text-davinci-003",
#                 prompt=f"You are a helpful assistant for health-related queries. {query}",
#                 max_tokens=150
#             )
#             return response.choices[0].text.strip()
#         except Exception as e:
#             return f"An error occurred: {e}"

# # Example usage
# api_key = 'sk-None-29QN9JvRwECKvYUl109cT3BlbkFJRo3FDu3C0mRG65ucIF8A'  # Replace with your actual OpenAI API key
# chatgpt = ChatGPT(api_key)
# print(chatgpt.get_health_tips())
# response = chatgpt.chat("What are the benefits of regular exercise?")
# print(response)
# import os
# import google.generativeai as genai
# from dotenv import load_dotenv

# load_dotenv()  

# genai.configure(api_key=os.environ["API_KEY"])

# model = genai.GenerativeModel('gemini-1.5-flash')
# response = model.generate_content("Write a story about a AI and magic")
# print(response.text)


# api_key = os.getenv('OPENAI_API_KEY')
# client = OpenAI(api_key=api_key)

# completion = client.chat.completions.create(
#   model="gpt-3.5-turbo",
#   messages=[
#     {"role": "system", "content": "You are a poetic assistant, skilled in explaining complex programming concepts with creative flair."},
#     {"role": "user", "content": "Compose a poem that explains the concept of recursion in programming."}
#   ]
# )

# print(completion.choices[0].message)