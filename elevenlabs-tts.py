#!/usr/bin/env python3
"""
ElevenLabs Text-to-Speech Script
Part 1 of 3: Voice AI Series

Simple script to convert text files to speech using ElevenLabs API.
"""

# Import necessary libraries
# os: For interacting with the operating system (e.g., environment variables)
# sys: For system-specific parameters and functions (e.g., exiting the program)
# requests: For making HTTP requests to the ElevenLabs API
# argparse: For parsing command-line arguments
# pathlib: For handling file paths
# datetime: For generating timestamps
# dotenv: For loading environment variables from a .env file

import os
import sys
import requests
import argparse
from pathlib import Path
from datetime import datetime
from dotenv import load_dotenv

class ElevenLabsTTS:
    def __init__(self, api_key):
        """Initialize the TTS client with API key."""
        # Store the API key and set up the base URL and headers for API requests
        self.api_key = api_key
        self.base_url = "https://api.elevenlabs.io/v1"
        self.headers = {
            "Accept": "audio/mpeg",
            "Content-Type": "application/json",
            "xi-api-key": self.api_key
        }
        
        # Predefined voice IDs for convenience
        self.voices = {
            "adam": "pNInz6obpgDQGcFmaJgB",       # Male, deep
            "bella": "EXAVITQu4vr4xnSDxMaL",      # Female, soft
            "arnold": "VR6AewLTigWG4xSOukaG",     # Male, crisp
            "josh": "TxGEqnHWrfWFTfGW9XjX",       # Male, young
            "dave": "CYw3kZ02Hs0563khs1Fj",       # Male, British
            "laura": "FGY2WhTYpPnrIDTdsKH5",      # Female, upbeat
            "charlie": "IKne3meq5aSn9XLyUdCD",    # Male, casual
            "george": "JBFqnCBsd6RMkjVDRZzb",     # Male, warm
        }

    def test_connection(self):
        """Test API connection and list available voices."""
        try:
            # Make a GET request to the voices endpoint
            response = requests.get(
                f"{self.base_url}/voices",
                headers={"xi-api-key": self.api_key}
            )
            response.raise_for_status()  # Raise an error for HTTP status codes >= 400
            voices_data = response.json()  # Parse the JSON response
            
            print("✅ API connection successful!")
            print(f"📋 Available voices: {len(voices_data['voices'])}")
            
            # Display the first 10 voices
            print("\n🎤 Sample voices:")
            for i, voice in enumerate(voices_data['voices'][:10]):
                print(f"  {i+1}. {voice['name']} ({voice['voice_id'][:8]}...)")
            
            return True
            
        except requests.exceptions.RequestException as e:
            # Handle any request-related errors
            print(f"❌ API connection failed: {e}")
            return False

    def text_to_speech(self, text, voice="adam", model="eleven_turbo_v2_5", 
                      stability=0.5, similarity_boost=0.75, style=0.0):
        """Convert text to speech and return audio data."""
        
        voice_id = self.voices.get(voice.lower(), voice)
        
        # Request payload
        payload = {
            "text": text,
            "model_id": model,
            "voice_settings": {
                "stability": stability,
                "similarity_boost": similarity_boost,
                "style": style,
                "use_speaker_boost": True
            }
        }
        
        print(f"🎵 Generating speech with voice: {voice}")
        print(f"📝 Text length: {len(text)} characters")
        
        try:
            response = requests.post(
                f"{self.base_url}/text-to-speech/{voice_id}",
                json=payload,
                headers=self.headers
            )
            response.raise_for_status()
            
            print("✅ Speech generated successfully!")
            return response.content
            
        except requests.exceptions.RequestException as e:
            print(f"❌ Error generating speech: {e}")
            if hasattr(e.response, 'text'):
                print(f"Error details: {e.response.text}")
            return None

    def save_audio(self, audio_data, output_path):
        """Save audio data to file."""
        try:
            with open(output_path, 'wb') as f:
                f.write(audio_data)
            print(f"💾 Audio saved to: {output_path}")
            print(f"📊 File size: {len(audio_data)} bytes")
            return True
        except Exception as e:
            print(f"❌ Error saving audio: {e}")
            return False

def read_text_file(file_path):
    """Read text from file with encoding detection."""
    try:
        # Try UTF-8 first
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read().strip()
        return content
    except UnicodeDecodeError:
        # Fallback to other encodings
        for encoding in ['latin-1', 'cp1252']:
            try:
                with open(file_path, 'r', encoding=encoding) as f:
                    content = f.read().strip()
                print(f"ℹ️  File read with {encoding} encoding")
                return content
            except UnicodeDecodeError:
                continue
        
        print("❌ Unable to read file with any encoding")
        return None
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        return None
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return None

def main():
    # Set up the argument parser for command-line options
    parser = argparse.ArgumentParser(
        description="Convert text files to speech using ElevenLabs API",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python tts_script.py input.txt
  python tts_script.py input.txt -v bella -o my_audio.mp3
  python tts_script.py input.txt -v josh --stability 0.7 --similarity 0.8
  python tts_script.py --test-connection
        """
    )
    
    # Define command-line arguments
    parser.add_argument('input_file', nargs='?', help='Input text file')
    parser.add_argument('-o', '--output', help='Output audio file (default: auto-generated)')
    parser.add_argument('-v', '--voice', default='adam', 
                       help='Voice to use (adam, bella, arnold, josh, dave, laura, charlie, george)')
    parser.add_argument('-m', '--model', default='eleven_turbo_v2_5',
                       choices=['eleven_turbo_v2_5', 'eleven_turbo_v2', 
                               'eleven_multilingual_v2', 'eleven_monolingual_v1'],
                       help='AI model to use')
    parser.add_argument('--stability', type=float, default=0.5,
                       help='Voice stability (0.0-1.0)')
    parser.add_argument('--similarity', type=float, default=0.75,
                       help='Similarity boost (0.0-1.0)')
    parser.add_argument('--style', type=float, default=0.0,
                       help='Style setting (0.0-1.0)')
    parser.add_argument('--test-connection', action='store_true',
                       help='Test API connection and list voices')

    # Parse the arguments
    args = parser.parse_args()

    # Load environment variables from .env file
    load_dotenv()

    # Retrieve the API key from environment variables
    api_key = os.getenv('ELEVENLABS_API_KEY')
    if not api_key:
        print("❌ ElevenLabs API key not found!")
        print("Set it as environment variable: export ELEVENLABS_API_KEY='your_key_here'")
        print("Or add it to a .env file")
        sys.exit(1)

    # Initialize the ElevenLabsTTS client
    tts = ElevenLabsTTS(api_key)

    # Test the API connection if the flag is set
    if args.test_connection:
        tts.test_connection()
        return
    
    # Validate input file
    if not args.input_file:
        print("❌ Please provide an input text file")
        parser.print_help()
        sys.exit(1)
    
    # Read input text
    print(f"📖 Reading text from: {args.input_file}")
    text = read_text_file(args.input_file)
    if not text:
        sys.exit(1)
    
    # Validate text length
    if len(text) > 5000:
        print(f"⚠️  Text is {len(text)} characters. Consider splitting for better results.")
        response = input("Continue anyway? (y/N): ")
        if response.lower() != 'y':
            sys.exit(1)
    
    print(f"📝 Text preview: {text[:100]}{'...' if len(text) > 100 else ''}")
    
    # Generate speech
    audio_data = tts.text_to_speech(
        text=text,
        voice=args.voice,
        model=args.model,
        stability=args.stability,
        similarity_boost=args.similarity,
        style=args.style
    )
    
    if not audio_data:
        sys.exit(1)
    
    # Generate output filename if not provided
    if not args.output:
        input_name = Path(args.input_file).stem
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        args.output = f"{input_name}_{args.voice}_{timestamp}.mp3"
    
    # Save audio
    if tts.save_audio(audio_data, args.output):
        print(f"\n🎉 Success! Audio file created: {args.output}")
        print(f"🎧 You can now play the audio file with any media player")
    else:
        sys.exit(1)

if __name__ == "__main__":
    print("🎤 ElevenLabs Text-to-Speech Converter")
    print("=" * 40)
    main()
