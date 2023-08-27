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

block = gr.Blocks(theme=gr.themes.Soft(), title="PixelTalkBot")

with block:
    gr.Markdown("""
                <footer>
                    <img style="display: inline-block; text-align: left;" src="https://cdn.discordapp.com/attachments/1072210515457224754/1135412968079769710/logo_itenas_black.png" alt="ITENAS logo" width="100px" height="50px">
                    <img style="display: inline-block; margin-left: 10px;" src="https://cdn.discordapp.com/attachments/1072210515457224754/1134098140853702729/logo_kmmi.png" alt="ITENAS logo" width="100px" height="50px">
                </footer>
    """)
    chatbot = gr.Chatbot(label="PixelTalkBot")
    message = gr.Textbox(label="Message", placeholder="Type your message here...")
    state = gr.State()
    submit = gr.Button(variant="primary", value="SEND")
    submit.click(chat_app, inputs=[message, state], outputs=[chatbot, state])

block.launch()