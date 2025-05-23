# ElevenLabs Voice AI - Text-to-Speech

A simple Python script to convert text files to speech using the ElevenLabs API.

![Screenshot 2025-05-23 at 12 51 29 PM](https://github.com/user-attachments/assets/6e562843-4212-4d3e-af28-853d3976d21c)

## 🎯 Features

- **File Input**: Read text from any `.txt` file
- **Multiple Voices**: 8 pre-configured voice options (Adam, Bella, Arnold, etc.)
- **Voice Control**: Adjust stability, similarity boost, and style parameters
- **Multiple Models**: Support for different ElevenLabs AI models
- **Auto Output**: Automatically generates timestamped output filenames
- **Error Handling**: Comprehensive error handling and validation
- **Connection Testing**: Test your API connection before processing

## 🚀 Quick Start

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Set Your API Key
```bash
export ELEVENLABS_API_KEY="your_api_key_here"
```

Or create a `.env` file:
```
ELEVENLABS_API_KEY=your_api_key_here
```

### 3. Test Connection
```bash
python elevenlabs-tts.py --test-connection
```

![Screenshot 2025-05-23 at 12 23 18 PM](https://github.com/user-attachments/assets/5d356c8a-36e6-4c9d-b31a-d83c7c931158)


### 4. Convert Text to Speech
```bash
# Basic usage
python elevenlabs-tts.py sample_text.txt
```
![Screenshot 2025-05-23 at 12 24 13 PM](https://github.com/user-attachments/assets/cbdb3ccd-7a4d-4301-b28d-bc07a3146840)
```
# With custom voice and output
python elevenlabs-tts.py sample_text.txt -v bella -o my_speech.mp3
```
![Screenshot 2025-05-23 at 12 39 45 PM](https://github.com/user-attachments/assets/53cfa097-1067-4428-a54b-ca017363c14c)

```
# With custom voice settings
python elevenlabs-tts.py sample_text.txt -v josh --stability 0.7 --similarity 0.8
```

## 📋 Usage Examples

```bash
# Test API connection
python elevenlabs-tts.py --test-connection

# Basic conversion
python elevenlabs-tts.py input.txt

# Custom voice (female)
python elevenlabs-tts.py input.txt -v bella

# Custom output filename
python elevenlabs-tts.py input.txt -o speech.mp3

# Fine-tune voice settings
python elevenlabs-tts.py input.txt -v adam --stability 0.6 --similarity 0.9 --style 0.2

# Use different AI model
python elevenlabs-tts.py input.txt -m eleven_multilingual_v2
```

## 🎤 Available Voices

| Voice   | Description     | Gender | Style        |
|---------|----------------|--------|--------------|
| adam    | Deep voice     | Male   | Professional |
| bella   | Soft voice     | Female | Gentle       |
| arnold  | Crisp voice    | Male   | Clear        |
| josh    | Young voice    | Male   | Energetic    |
| dave    | British accent | Male   | Sophisticated|
| laura   | Upbeat voice   | Female | Enthusiastic |
| charlie | Casual voice   | Male   | Friendly     |
| george  | Warm voice     | Male   | Comforting   |

## ⚙️ Voice Parameters

- **Stability** (0.0-1.0): Controls voice consistency
  - Lower = more variable and expressive
  - Higher = more stable and predictable
  
- **Similarity Boost** (0.0-1.0): How closely to match the original voice
  - Lower = more creative interpretation
  - Higher = closer to original voice sample
  
- **Style** (0.0-1.0): Overall style and emotion
  - 0.0 = neutral
  - Higher = more stylized/emotional

## 🔑 Getting an ElevenLabs API Key

1. Sign up at [ElevenLabs](https://elevenlabs.io)
2. Go to your profile settings
3. Generate an API key
4. Free tier includes 10,000 characters per month

## 📁 Project Structure

```
part1-text-to-speech/
├── elevenlabs-tts.py          # Main script
├── requirements.txt       # Dependencies
├── sample_text.txt       # Sample input file
├── .env                 # Not included, stores API keys
├── README.md             # This file
└── output/               # Generated audio files (auto-created)
```

## 🛠️ Technical Details

- **Language**: Python 3.7+
- **Dependencies**: requests
- **Audio Format**: MP3
- **API**: ElevenLabs Text-to-Speech v1
- **Encoding**: UTF-8 with fallback support

## 🔍 Troubleshooting

### Common Issues

1. **API Key Error**
   ```
   ❌ ElevenLabs API key not found!
   ```
   Solution: Set the `ELEVENLABS_API_KEY` environment variable

2. **File Not Found**
   ```
   ❌ File not found: input.txt
   ```
   Solution: Check the file path and ensure the file exists

3. **API Connection Failed**
   ```
   ❌ API connection failed
   ```
   Solution: Check your internet connection and API key validity

4. **Text Too Long**
   ```
   ⚠️ Text is 6000 characters. Consider splitting for better results.
   ```
   Solution: Split large texts into smaller chunks


## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request


## 🔗 Links

- [ElevenLabs API Documentation](https://docs.elevenlabs.io/)
- [ElevenLabs Website](https://elevenlabs.io)
