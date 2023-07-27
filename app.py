import gradio as gr
import openai
import os

openai.api_key = os.getenv("OPEN_AI_API_KEY")

messages = [{"role": "system", "content": "Kamu adalah seorang ahli bernama andy yang mempunyai spesialisasi dalam bidang computer vision"}]

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

block = gr.Blocks(gr.themes.Soft())

with block:
    chatbot = gr.Chatbot(label="ITENAS COMVIS BOT")
    message = gr.Textbox(label="Message", placeholder="Type your message here...")
    state = gr.State()
    submit = gr.Button("SEND")
    gr.Markdown("""
                <footer>
                    <p>ITENAS</p>
                    <img src="https://cdn.discordapp.com/attachments/1072210515457224754/1134095848192622612/logo_itenas.png" alt="ITENAS logo" width="100" height="50">
                </footer>
    """)
    submit.click(chat_app, inputs=[message, state], outputs=[chatbot, state])

block.launch()