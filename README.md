# Neural Sonata

*An interactive art project that visualizes and sonifies the thought process of an AI in real-time.*

---

### [✨ LIVE DEMO ✨](https://hamidomarov.github.io/)

---

<img src="https://i.imgur.com/gKBCKqC.png" alt="Neural Sonata Demo Screenshot">
[Neural Sonata](https://github.com/user-attachments/assets/1349a212-6792-4392-b076-93fbefd613a1)


## 🎵 About The Project

"Neural Sonata" explores the intersection of art, music, and artificial intelligence. When a Large Language Model (LLM) generates text, it calculates mathematical probabilities for each potential next word. This project captures that fleeting "moment of decision" and transforms it into a dynamic, interactive audio-visual experience.

As you type, the application sends your text to a backend AI model. The model's predictions—the top 10 most likely next words and their probabilities—are streamed back to the frontend. This data is then used to generate a procedural "sonata":
* Each potential word is represented by a pulsating circle.
* The **size and brightness** of the circle correspond to the word's probability.
* The probabilities are mapped to a **pentatonic scale**, creating a harmonious arpeggio that represents the AI's "thought process."
* The connections between potential words are visualized with a faint, dynamic web of lines.

This is not a tool, but an experience—a poetic glimpse into the black box of AI.

## 🛠️ Built With

This project is built with a decoupled frontend/backend architecture.

**Frontend:**
* [p5.js](https://p5js.org/) for creative coding (visualization, animation, and sound synthesis).
* HTML5 & CSS3
* Hosted on **GitHub Pages**.

**Backend:**
* [Python](https://www.python.org/)
* [Flask](https://flask.palletsprojects.com/) for the web server and API.
* [Hugging Face Transformers](https://huggingface.co/docs/transformers/index) for loading and running the AI model.
* The backend is currently running `gpt2-medium` on a free CPU instance.
* Hosted on **Hugging Face Spaces**.

## 🚀 Key Features

* **Real-time Interactivity:** The visualization and sonification react instantly as you type.
* **Data-driven Visualization:** Circle size, brightness, line thickness, and particle effects are all directly mapped from the AI's probability data.
* **Procedural Audio:** A harmonious arpeggio is generated on the fly based on a pentatonic scale, ensuring the "sonata" is always musical.
* **Permanent Deployment:** Fully deployed on free-tier services (GitHub Pages and Hugging Face Spaces), making it permanently accessible.

## 🔗 Links

* **Live Demo:** [https://hamidomarov.github.io/](https://hamidomarov.github.io/)
* **Backend API Host:** [https://YOUR_HUGGINGFACE_SPACE_LINK.hf.space/](https://huggingface.co/spaces/HamidOmarov/neural-sonata-api)
