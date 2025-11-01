## argparse
### The argparse module makes it easy to write user-friendly command-line interfaces

# Context: serial tool: needs PORT (positional) and optional --baud
import argparse

def main():
    p = argparse.ArgumentParser(prog="serial-tool")
    p.add_argument("port", help="serial port path")     # positional
    p.add_argument("--baud", type=int, default=115200, help="baud rate")
    args = p.parse_args()
    print(f"Connecting to {args.port} @ {args.baud}")

if __name__ == "__main__":
    main()
# run: python3 argparse_script.py /dev/ttyUSB0 --baud 57600
# Help: python3 argparse_script.py -h