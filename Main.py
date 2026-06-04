import audioRecorder as voice
import audio_devices as devices
from VoiceState import VoiceState


def main():
    state = VoiceState()

    # Geräte
    print("Checking audio devices...\n")
    devices.check_input_devices()
    devices.check_output_devices()
    devices.selected_device()

    # Stream
    stream = voice.start_stream(state)

    print("Push-to-talk")

    #PushToTalk TODO: ERSETZTEN DURCH TOGGLE SCHALTER...
    while True:
        cmd = input("talk? (y/n/exit): ")

        if cmd == "y":
            state.is_talking = True
        elif cmd == "n":
            state.is_talking = False
        elif cmd == "exit":
            break
    stream.stop()
    stream.close()


if __name__ == "__main__":
    main()