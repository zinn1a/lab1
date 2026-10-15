def show_animation():
    frames = [
        "0---",
        "-0--",
        "--0-",
        "---0",
        "--0-",
        "-0--",
        "0---"
    ]
    for frame in frames:
        print(f"\r{frame}", end="", flush=True)
        time.sleep(0.6)
    print()