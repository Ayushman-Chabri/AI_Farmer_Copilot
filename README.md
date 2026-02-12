# AgroVision

<a href="https://github.com/Ayushman-Chabri/AI_Farmer_Copilot/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Ayushman-Chabri/AI_Farmer_Copilot" />
</a>


## 🏗️ Project Structure
```bash
AI_Farmer_Copilot/
│
├── main.py                # Entry point
├── ui/                    # Streamlit interface
├── vision/                # Computer vision models
├── voice/                 # Voice processing modules
├── llm/                   # LLM interaction
├── pipeline/              # AI pipeline orchestration
├── loaders/               # Data loading modules
├── logic/                 # Core decision logic
├── safety/                # Validation & safety checks
├── config/                # Configuration files
├── tests/                 # Test cases
├── environment.yml        # Conda environment
└── requirements.txt       # pip dependencies
```

## ⚙️ Installation & Setup

1. Clone the repository
```bash
git clone https://github.com/Ayushman-Chabri/AI_Farmer_Copilot.git
```

2. Create environment 
- Option 1 : Conda (Recommended) \
This project supports Mac, Windows, and Linux
```bash
conda env create -f environment.yml
conda activate TrithonEnv
```
- Mac users (one time setup for audio)
```bash
brew install portaudio
```
- Option 2 : pip (Alternative) \
If you are not using conda:
```bash
pip install -r requirements.txt
```

3. Install the required dependencies
```bash
pip install -r requirements.txt
```

4. Run the project
```bash
python main.py
```

## Features
- Voice enabled AI assistant
- Crop & farming advisory
- Image based plant analysis
- LLM powered recommendations
- Safety & validation layer
- Modular AI pipeline architecture
