import json
import gradio as gr
from textblob import TextBlob

def sentiment_analysis(text: str) -> str:
    """
    Analyze the sentiment of the given text.

    Args:
        text (str): The text to analyze

    Returns:
        str: A JSON string containing polarity, subjectivity, and assessment
    """

    blob = TextBlob(text)
    sentiment = blob.sentiment

    result = {
        "polarity": round(sentiment.polarity,2),
        "subjectivity": round(sentiment.subjectivity,2),
        "assessment": "positive" if sentiment.polarity > 0 else "negative" if sentiment.polarity < 0 else "neutral"
    }

    return json.dumps(result)


# Create the Gradio interface
demo = gr.Interface(
    fn=sentiment_analysis,
    inputs=gr.Textbox(placeholder="Enter text to analyze..."),
    outputs=gr.Textbox(),
    title="Text Sentiment Analysis",
    description="Analyze the sentiment of text using TextBlob"
)

"""
with gr.Interface() as demo:
    gr.Markdown("# Sentiment Analysis")
    with gr.Row():
        text_input = gr.Textbox(label="Text", placeholder="Enter text here...")
        sentiment_output = gr.Textbox(label="Sentiment")
    analyze_button = gr.Button("Analyze")
    analyze_button.click(fn=sentiment_analysis, inputs=text_input, outputs=sentiment_output)
"""

if __name__ == "__main__":
    demo.launch(mcp_server=True)   