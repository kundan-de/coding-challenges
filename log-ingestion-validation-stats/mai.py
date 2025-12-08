INPUT_FILE = "log.log"
VALIDATED_RECORDS = "structured_logs.jsonl"
BAD_RECORDS = "bad_logs.txt"


def process(path: str) -> None:
    stats = {"lines_processes": 0, "valid_line": 0, "malformed_line": 0}
    with open("path", "r", encoding="utf-8") as f:
        with open(VALIDATED_RECORDS, "w", encoding="utf-8") as valid_writer:
            with open(BAD_RECORDS, "w", encoding="utf-8") as bad_writer:
                for line in f:
                    stats["lines_processes"] += 1
                    line = line.strip()

                    if not line:
                        stats["malformed_line"] += 1
                        bad_writer.write(line)
                        continue

                    splited_line = line.split()
                    if len(splited_line) >= 4:
                        pass
                    else:
                        stats["malformed_line"] += 1
                        bad_writer.write(line)


def main() -> None:
    process(INPUT_FILE)


if __name__ == "__main__":
    main()
