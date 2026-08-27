from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    failures = []

    for path in sorted(root.rglob("*.py")):
        if ".venv" in path.parts:
            continue
        try:
            compile(path.read_text(encoding="utf-8"), str(path), "exec")
        except SyntaxError as exc:
            failures.append((path, exc))

    if failures:
        for path, exc in failures:
            print(f"FOUT: {path}: {exc}")
        raise SystemExit(1)

    print("Alle Python-bestanden zijn syntactisch geldig.")


if __name__ == "__main__":
    main()
