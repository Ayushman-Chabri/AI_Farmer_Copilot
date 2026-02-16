<img src="ui/images/AgroVision.png"/>

<a href="https://github.com/Ayushman-Chabri/AI_Farmer_Copilot/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=Ayushman-Chabri/AI_Farmer_Copilot" />
</a>


## 🏗️ Project Structure
```bash
AI_Farmer_Copilot/
|
├── 📁 config
│   └── 🐍 settings.py
├── 📁 data
│   ├── 📁 crops
│   │   └── ⚙️ odisha_crops.json
│   ├── 📁 diseases
│   │   └── ⚙️ diseases.json
│   ├── 📁 metadata
│   │   └── ⚙️ regions.json
│   ├── 📁 policies
│   │   └── ⚙️ odisha_policies.json
│   ├── 📁 referrals
│   │   └── ⚙️ odisha_referrals.json
│   ├── 📁 soil
│   │   └── ⚙️ odisha_soil.json
│   ├── 📁 techniques
│   │   └── ⚙️ techniques.json
│   └── 📁 weather
│       └── ⚙️ odisha_weather.json
├── 📁 llm
│   ├── 🐍 __init__.py
│   ├── 🐍 gemma_loader.py
│   ├── 🐍 generator.py
│   ├── 🐍 prompt_templates.py
│   └── 🐍 response_formatter.py
├── 📁 loaders
│   ├── 🐍 __init__.py
│   ├── 🐍 base_loader.py
│   ├── 🐍 policy_loader.py
│   ├── 🐍 region_loader.py
│   ├── 🐍 soil_loader.py
│   ├── 🐍 validation.py
│   └── 🐍 weather_loader.py
├── 📁 logic
│   ├── 🐍 __init__.py
│   ├── 🐍 context_builder.py
│   ├── 🐍 module_selector.py
│   ├── 🐍 risk_analysis.py
│   └── 🐍 rules.py
├── 📁 pipeline
│   ├── 🐍 __init__.py
│   ├── 🐍 orchestrator.py
│   └── 🐍 state.py
├── 📁 safety
│   ├── 🐍 __init__.py
│   ├── 🐍 fallback.py
│   ├── 🐍 referral_logic.py
│   └── 🐍 uncertainty.py
├── 📁 tests
│   ├── 🐍 test_loaders.py
│   ├── 🐍 test_logic.py
│   └── 🐍 test_pipeline.py
├── 📁 ui
│   ├── 📁 images
│   │   ├── 🖼️ AgroVision.png
│   │   └── 🖼️ Samriddhi.png
│   ├── 📁 screens
│   │   ├── 🐍 input.py
│   │   ├── 🐍 processing.py
│   │   ├── 🐍 results.py
│   │   └── 🐍 welcome.py
│   ├── 🐍 __init__.py
│   ├── 🐍 app.py
│   └── 🐍 ui_utils.py
├── 📁 vision
│   ├── 🐍 __init__.py
│   ├── 🐍 confidence.py
│   ├── 🐍 infer.py
│   ├── 🐍 model.py
│   └── 🐍 preprocess.py
├── 📁 voice
│   ├── 🐍 __init__.py
│   ├── 🐍 audio_utils.py
│   ├── 🐍 stt.py
│   └── 🐍 tts.py
├── 📝 README.md
├── 📕 conda-cheatsheet.pdf
├── ⚙️ environment.yml
├── 🐍 main.py
└── 📄 requirements.txt
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

## 🧠 Features
- 🎙️ Voice-enabled AI assistant
- 🌱 Crop & farming advisory
- 🖼️ Image-based plant analysis
- 🤖 LLM-powered recommendations
- 🛡️ Safety & validation layer
- 🧩 Modular AI pipeline architecture