# 🌾 AgroVision — AI Farmer Copilot

<img src="ui/images/AgroVision.png"/>

<a href="https://github.com/Ayushman-Chabri/AI_Farmer_Copilot/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Ayushman-Chabri/AI_Farmer_Copilot" />
</a>

AgroVision is an **AI-powered smart farming assistant** designed to help farmers with crop guidance, disease detection, weather insights, and voice-based support.

Built using **LLMs, Computer Vision, and Voice AI** to support rural and smart agriculture.

## 🏗️ Project Structure
```bash
AI_Farmer_Copilot/
|
├── 📁 config/
├── 📁 data/
├── 📁 llm/
├── 📁 loaders/
├── 📁 logic/
├── 📁 pipeline/
├── 📁 safety/
├── 📁 tests/
├── 📁 ui/
├── 📁 vision/
├── 📁 voice/
├── 📝 README.md
├── 📕 conda-cheatsheet.pdf
├── ⚙️ environment.yml
├── 🐍 main.py
└── 📄 requirements.txt
```

## ⚙️ Installation & Setup

### 1️⃣ Clone repository
```bash
git clone https://github.com/Ayushman-Chabri/AI_Farmer_Copilot.git  
cd AI_Farmer_Copilot
```
### 2️⃣ Create environment (Recommended: Conda)
This project supports Mac, Windows, Linux
```bash
conda env create -f environment.yml  
conda activate TrithonEnv
```
Mac users (one-time audio setup):
```bash
brew install portaudio
```
### Alternative: pip setup (if not using conda)
```bash
pip install -r requirements.txt
```
### 3️⃣ Run project
```bash
python main.py
```
## 🧠 Features
- 🎙️ Voice-enabled AI assistant
- 🌱 Crop & farming advisory
- 🖼️ Image-based plant analysis
- 🤖 LLM-powered recommendations
- 🛡️ Safety & validation layer
- 🧩 Modular AI pipeline architecture