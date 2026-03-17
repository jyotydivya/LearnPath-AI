import os
from flask import Flask, request, jsonify, render_template
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY")

genai.configure(api_key=api_key)

app = Flask(__name__)

@app.route('/')
def index():
    """Renders the main page."""
    return render_template('index.html')

@app.route('/generate-path', methods=['POST'])
def generate_path():
    """Generates a learning path using the Gemini API."""
    try:
        topic = request.json['topic']
        
        prompt = f"Create a detailed, step-by-step learning path for a beginner to learn about '{topic}'. The path should include key concepts, recommended resources, and potential projects. Structure it with clear headings and bullet points."
        
        model = genai.GenerativeModel('gemini-1.5-flash') 
        
        response = model.generate_content(prompt)
        
        generated_text = response.text
        return jsonify({'learning_path': generated_text})

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({'error': 'Failed to generate learning path.'}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)