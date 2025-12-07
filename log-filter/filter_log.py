FILE_PATH = "text.txt"


def log_filter(path: str) -> None:
    error_logs = []
    with open(path, "r") as f:
        for line in f:
            if "error" in line.lower():
                error_logs.append(line)
            yield line

    with open("error.log", "w") as f:
        for log in error_logs:
            f.write(log)


def main() -> None:
    log_filter(FILE_PATH)


if __name__ == "__main__":
    main()
