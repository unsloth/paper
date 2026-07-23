import gradio as gr

# Define your main function / AI model logic here
def process_input(text_input):
    return f"Processed input: '{text_input}' successfully!"

# Build the user interface
demo = gr.Interface(
    fn=process_input,
    inputs=gr.Textbox(lines=2, placeholder="Enter text here...", label="Input Text"),
    outputs=gr.Textbox(label="Output Result"),
    title="My Research paper",
    description="A standard research paper inside a Docker container."
)

# CRITICAL FOR HUGGING FACE DOCKER:
# Must bind to server_name="0.0.0.0" and server_port=7860
if __name__ == "__main__":
    demo.launch(server_name="0.0.0.0", server_port=7860)
