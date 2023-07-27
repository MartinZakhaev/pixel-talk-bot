import gradio as gr
import openai
import os
# from dotenv import load_dotenv

# load_dotenv()

openai.api_key = os.getenv("OPEN_AI_API_KEY")

messages = [{"role": "system", "content": "Kamu adalah seorang ahli yang mempunyai spesialisasi dalam bidang perbaikan printer"}]

def get_chat_response(user_input):
    messages.append({"role": "user", "content": user_input})
    response = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = messages
    )
    bot_reply = response["choices"][0]["message"]["content"]
    messages.append({"role": "assistant", "content": bot_reply})
    return bot_reply

def chat_app(input, history):
    history = history or []
    s = list(sum(history, ()))
    s.append(input)
    inp = " ".join(s)
    output = get_chat_response(inp)
    history.append((input, output))
    return history, history

block = gr.Blocks()

with block:
    gr.Markdown("""<h1><center>ITENAS COMPUTER VISION BOT PRO</center></h1>""")
    chatbot = gr.Chatbot()
    message = gr.Textbox(placeholder="Type your message here...")
    state = gr.State()
    submit = gr.Button("SEND")
    submit.click(chat_app, inputs=[message, state], outputs=[chatbot, state])

block.launch()