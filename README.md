# audio-streamer-server

### High-Level Overview of the Audio Streaming Server Project

#### Project Components:
1. **Backend Server**:
   - **Technology**: Flask (Python web framework).
   - **Functionality**:
     - Captures live audio input using `pyaudio`.
     - Applies real-time audio effects using `pydub`.
     - Streams audio to connected clients.
     - Handles HTTP requests and serves the web interface.

2. **Frontend Interface**:
   - **Technology**: HTML, Tailwind CSS (for styling), JavaScript.
   - **Functionality**:
     - Provides a user-friendly interface for audio control and effects.
     - Allows users to play, pause, and record the audio stream.
     - Enables users to apply audio effects (gain, normalization, echo, bass boost).
     - Allows downloading recorded audio.

#### Detailed Breakdown:

1. **Backend Server (`server.py`)**:
   - **Setup**:
     - Initializes a Flask app.
     - Configures and opens an audio stream with `pyaudio`.
   - **Routes**:
     - **`/`**: Renders the main HTML page (`index.html`).
     - **`/audio`**: Streams live audio data with applied effects.
   - **Audio Processing**:
     - Captures audio in chunks.
     - Converts raw audio data into `AudioSegment` objects.
     - Applies effects like normalization, gain adjustment, echo, and bass boost based on query parameters.
     - Streams the modified audio in WAV format.

2. **Frontend Interface (`templates/index.html`)**:
   - **Layout**:
     - An HTML page styled with Tailwind CSS.
     - Contains an audio player and various controls for user interaction.
   - **Controls**:
     - Play and pause buttons to control audio playback.
     - Record button to capture and download the audio stream.
     - Sliders and checkboxes to adjust audio effects.
   - **JavaScript**:
     - Handles dynamic updates to the audio source URL based on user input.
     - Manages audio player controls and recording functionality.

#### Key Features:
- **Real-time Audio Streaming**: The server captures and streams live audio to the client.
- **User Interface**: A simple web-based interface for controlling audio playback and effects.
- **Audio Effects**: Real-time application of audio effects like gain, normalization, echo, and bass boost.
- **Recording**: Ability to record and download the live audio stream.

### Summary

This project implements an enhanced live audio streaming server with a web-based user interface. The backend uses Flask and pyaudio to capture and stream live audio, while the frontend provides controls for playback, effects, and recording. The combination of real-time audio processing and a user-friendly interface makes this project a comprehensive solution for live audio streaming with interactive features.

## Collaborate with GPT Engineer

This is a [gptengineer.app](https://gptengineer.app)-synced repository 🌟🤖

Changes made via gptengineer.app will be committed to this repo.

If you clone this repo and push changes, you will have them reflected in the GPT Engineer UI.

## Tech stack

This project is built with React with shadcn-ui and Tailwind CSS.

- Vite
- React
- shadcn/ui
- Tailwind CSS

## Setup

```sh
git clone https://github.com/GPT-Engineer-App/audio-streamer-server.git
cd audio-streamer-server
npm i
```

```sh
npm run dev
```

This will run a dev server with auto reloading and an instant preview.

## Requirements

- Node.js & npm - [install with nvm](https://github.com/nvm-sh/nvm#installing-and-updating)
