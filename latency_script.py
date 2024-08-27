import os
import time

# Define your test file and settings
test_file = "test_hebrew.wav"
audio_length_in_seconds = 36.94  # Replace this with the actual length of your audio file in seconds
language = "he"
min_chunk_size = 1
vac_chunk_size = 512


# Function to run the test
def run_test(mode="none"):
    if mode == "voice_control":
        print("Running test with Voice Control")
        command = f"poetry run python whisper_online.py {test_file} --language {language} --vac-chunk-size {vac_chunk_size}"
    elif mode == "vad":
        print("Running test with Voice Activity Detection (VAD)")
        command = f"poetry run python whisper_online.py {test_file} --language {language} --min-chunk-size {min_chunk_size} --vad"
    else:
        print("Running test without Voice Control")
        command = f"poetry run python whisper_online.py {test_file} --language {language} --min-chunk-size {min_chunk_size}"

    # Start the test and capture the start time
    start_time = time.time()

    # Run the command using os.system
    os.system(command)

    end_time = time.time()

    # Calculate total latency
    total_latency = end_time - start_time
    latency_per_second = total_latency / audio_length_in_seconds

    # Log latency
    print(f"Command: {command}")
    print(f"Total Latency: {total_latency:.3f} seconds")
    print(f"Latency per second of audio: {latency_per_second:.3f} seconds\n")

    return total_latency, latency_per_second


# Run the test without the voice control
total_latency_without_vc, latency_per_sec_without_vc = run_test(mode="none")

# Run the test with the voice control
total_latency_with_vc, latency_per_sec_with_vc = run_test(mode="voice_control")

# Run the test with Voice Activity Detection (VAD)
total_latency_with_vad, latency_per_sec_with_vad = run_test(mode="vad")

# Print summary of results
print(f"Total Latency without Voice Control: {total_latency_without_vc:.3f} seconds")
print(f"Latency per second without Voice Control: {latency_per_sec_without_vc:.3f} seconds")
print(f"Total Latency with Voice Control: {total_latency_with_vc:.3f} seconds")
print(f"Latency per second with Voice Control: {latency_per_sec_with_vc:.3f} seconds")
print(f"Total Latency with VAD: {total_latency_with_vad:.3f} seconds")
print(f"Latency per second with VAD: {latency_per_sec_with_vad:.3f} seconds")
