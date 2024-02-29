import sys
from pydub import utils
from pydub import AudioSegment

args = sys.argv[1::]
allowed_ext :list[str] = [
    "mp3",
    "wav"
]

def get_file_ext(name :str) -> str:
    sp = name.split(".")
    return sp[len(sp)-1] if len(sp) > 0 else ""

def get_level(base_sound) -> float:
    target_peak = base_sound.max_possible_amplitude
    return 0 - round(utils.ratio_to_db(target_peak / base_sound.max), 3)

def test_args() -> bool:
    if(len(args) >= 1):
        return True
    return False

def test_file_ext(filenames :list[str]) -> bool:
    for name in filenames:
        if get_file_ext(name) in allowed_ext:
            continue
        else:
            return False
    return True


def main():
    if test_args() != True:
        print("Not enough arguments")
        print("Using: showgain.py [filename...]")
        exit(1)

    filenames = args[0::]

    if test_file_ext(filenames) != True:
        print("Contains unsupported file formats")
        print("Supported .mp3 .wav")
        exit(1)

    for name in filenames:
        ext = get_file_ext(name)
        input_base = AudioSegment.from_file(name, format=ext)
        original_level = get_level(input_base)
        print(f"{name} Level = {original_level}")

if __name__ == '__main__':
    main()