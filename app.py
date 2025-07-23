import gradio as gr
from transformers import pipeline, set_seed

# Load the text generation pipeline
generator = pipeline("text-generation", model="gpt2")
set_seed(42)  # Optional: for reproducibility

# Define the function that generates a caption
def generate_caption(prompt):
    result = generator(prompt, max_length=50, num_return_sequences=1, do_sample=True)
    return result[0]["generated_text"]

# Create Gradio interface
interface = gr.Interface(
    fn=generate_caption,
    inputs=gr.Textbox(lines=2, placeholder="e.g., Product: Vegan Protein Shake"),
    outputs=gr.Textbox(label="Generated Caption"),
    title="📱 Social Media Caption Generator",
    description="Enter a product name, idea, or phrase, and get an AI-generated social media caption."
)

interface.launch()

