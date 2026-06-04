import sounddevice as sd


def check_input_devices():
    found = False

    for d in sd.query_devices():
        if d["max_input_channels"] > 0:
            print("INPUT:", d["name"])
            found = True

    if not found:
        print("Kein Input Device gefunden")


def check_output_devices():
    found = False

    for d in sd.query_devices():
        if d["max_output_channels"] > 0:
            print("OUTPUT:", d["name"])
            found = True

    if not found:
        print("Kein Output Device gefunden")


def selected_device():
    try:
        input_idx, output_idx = sd.default.device

        print("\nDefault Input:")
        print(sd.query_devices(input_idx)["name"])

        print("\nDefault Output:")
        print(sd.query_devices(output_idx)["name"])

    except Exception:
        print("Kein Default Device gesetzt")