# Antigravity Humanizer Pro

A premium, stateless AI Humanizer SaaS powered by Gemini 3 Flash. This engine strips the "robotic weight" from AI text using the **Five Laws of Antigravity**.

## Features

- **Five Laws Engine**: Breaking repetitive AI patterns for natural flow.
- **Human Score Stats**: Real-time Perplexity and Burstiness heuristics.
- **Apple-Style UI**: Sleek, glassmorphic design with smooth micro-animations.
- **FastAPI Backend**: Efficient, stateless performance.

## Getting Started

### Prerequisites
- Python 3.8+
- [Google AI Studio API Key](https://aistudio.google.com/)

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/usaidahmedat50-hub/humanizer-pro.git
   cd humanizer-pro
   ```

2. Set up environment variables:
   Create a `.env` file:
   ```env
   GEMINI_API_KEY=your_genai_api_key_here
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Start the backend:
   ```bash
   uvicorn app.main:app --reload
   ```

5. Open the frontend:
   Open `public/index.html` in your browser.

## Built With
- FastAPI
- Google Generative AI (Gemini 3 Flash)
- Tailwind CSS
- Vanilla JS

---
Built by Antigravity Writing Engine.
