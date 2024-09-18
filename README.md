# Whisper Streaming Ivrit-ai

This project enables real-time transcription of Hebrew audio files using the **ivrit-ai** model, based on OpenAI's Whisper model. It supports both streaming WAV files for transcription and providing live audio input via a microphone for real-time transcription.

## Project Overview

The project extends the original **Whisper streaming** capabilities to support Hebrew transcription through the ivrit-ai model. It can process both pre-recorded WAV files and live microphone input for transcription.

## Branches

### Main Branch

The **main branch** provides a basic setup for streaming transcription using the Whisper model.

### Ivrit Branch

The **ivrit branch** modifies the project to use the **ivrit-ai** model for Hebrew transcription. The model is deployed on **Runpod** via a Docker image, and the client-side is adjusted to interact with this model for real-time transcription.

## Set Up
### Setting Up Poetry 
This project uses **Poetry** as a dependency manager. Poetry handles dependencies, virtual environments, and package building.

Installing Project Dependencies
After cloning the repository, you can install all required dependencies by running: 
```bash
poetry install
```
This will create a virtual environment and install all the dependencies listed in the `pyproject.toml` file.

### Setting Up the Ivrit-ai Model on Runpod
To deploy the ivrit-ai model for Hebrew transcription, follow these steps:  

1. Log in to [runpod.io](https://www.runpod.io).
2. From the menu, navigate to **Serverless**, then click **New Endpoint**.
3. Select the desired worker configuration:
   - You can choose the cheapest worker (16GB GPU, $0.00016/second as of August 1st, 2024).
   - Active workers can be set to 0, and max workers to 1 or more.
   - GPUs per worker should be set to 1.
4. For the container image, select:
```bash
   yairlifshitz/faster-whisper-v2-d4:v1.0
```
5. Click Deploy


## Running the Project

There are two ways to run this project, depending on whether you want to transcribe pre-recorded audio or live audio from a microphone:

### 1. Transcribing a WAV File

To transcribe a pre-recorded WAV file in a stream-like manner, use the following command:

```bash
python whisper_online.py me-hebrew-stream.wav --language he --min-chunk-size 1 > out.txt
```

This command processes the me-hebrew-stream.wav file and outputs the transcription to out.txt as it is transcribed in real-time.

### 2. Transcribing Live Microphone Input
For live transcription of audio input from a microphone, follow these steps:

First, start the server to capture audio input:  
``` bash
rec -r 16000 -b 16 -e signed-integer --channels=1 -t raw - | nc localhost 43007
```

Then, run the client to process and transcribe the audio: 
```bash
poetry run python whisper_online_server.py --host localhost --port 43007 --warmup-file me-hebrew-stream.wav
```
Using a voice controller with this setup provides better results in terms of latency.:  
```bash
poetry run python whisper_online_server.py --vac-chunk-size 512 --host localhost --port 43007 --warmup-file me-hebrew-stream.wav`
```
## Latency Results

Here are the latency results for different setups:  
>Total Latency without Voice Control: 63.140 seconds  
>Latency per second without Voice Control: 1.709 seconds  
>Total Latency with Voice Control: 62.772 seconds  
>Latency per second with Voice Control: 1.699 seconds 
>Total Latency with VAD (Voice Activity Detection): 61.918 seconds  
>Latency per second with VAD: 1.676 seconds  


## Results

Example of Transcription Output for WAV File:  
When running whisper_online.py with a WAV file, the transcription output looks like this:   
 >15827.6072 0 6000 כשאנחנו נתקלים במצב שמעורר בנו חרדה, הגוף שלנו מיד מכין את עצמו לאימות.  
>47854.9259 6000 38000  הלב דופק חזק, אנחנו מזיעים, לפעמים מרגישים חולשה בגוף. קשה לנו להתרכז במשהו אחר. מבחינה פיזיולוגית, רמת החרדה לא נשארת קבועה, אלא עולה ויורדת כמו גל. חשוב לזכור את זה. בסוף, החרדה תמיד יורדת. עם עזרה, אפשר להתמודד עם החרדה גם כשהיא עולה.  ‫תודה רבה.
>
#### More example results can be found here:  
- me-hebrew-stream.wav - out3.txt  
- test_heberew.wav - out11.txt for longer audio  
- have-a-nice-day.wav - out.txt for english audio testing  





### Server-Side Modifications
For server-side modifications that integrate Whisper online with the Hebrew transcription model, check out my project runpod-serverless-whisper here. It includes modifications to seamlessly integrate the ivrit-ai model with Whisper for real-time transcription.     

## Links 

- Whisper Streaming project: [whisper-streaming](https://github.com/ufal/whisper_streaming)  
- Ivrit-ai Runpid serverless project: [ivrit-ai/runpod-serverless](https://github.com/ivrit-ai/runpod-serverless)   
- Check out my project for server-side modification that integrate Whisper online with the Hebrew transcription model. It includes modifications to seamlessly integrate the ivrit-ai model with Whisper for real-time transcription:  [runpod-serverless-whisper](https://github.com/AshDavid12/runpod_serverless_whisper/tree/main)


