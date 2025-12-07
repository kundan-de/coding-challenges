import json

FILE_PATH = "log.log"
OUTPUT_FILE = "structured_logs.jsonl"


def convert_jsonl(path: str) -> None:
    with open(path, "r", encoding="utf-8") as f:
        with open(OUTPUT_FILE, "w", encoding="utf-8", newline="\n") as w:
            for line in f:
                line = line.strip()
                if not line:
                    continue

                splitted_line = line.split()
                if len(splitted_line) >= 4:
                    log_dict = {}

                    log_dict["timestamp"] = " ".join(splitted_line[:2])
                    log_dict["level"] = splitted_line[2]
                    log_dict["message"] = " ".join(splitted_line[3:])

                    json_write = json.dumps(log_dict, ensure_ascii=False) + "\n"
                    w.write(json_write)


def main() -> None:
    convert_jsonl(FILE_PATH)


if __name__ == "__main__":
    main()
