from pathlib import Path
import shutil

FILE_CATEGORIES: dict[str, set[str]] = {
    "Images": {".jpg", ".jpeg", ".png", ".gif", ".webp", ".svg"},
    "Documents": {".pdf", ".docx", ".txt", ".md", ".xlsx", ".csv"},
    "Code": {".py", ".js", ".ts", ".java", ".cpp", ".html", ".css"},
    "Archives": {".zip", ".tar", ".gz", ".rar", ".7z"},
    "Media": {".mp3", ".wav", ".mp4", ".mkv", ".mov"},
}


def get_category(extension: str) -> str:
    ext = extension.lower()
    for category, extensions in FILE_CATEGORIES.items():
        if ext in extensions:
            return category
    return "Other"


def resolve_collision(destination: Path) -> Path:
    """Append an incrementing counter if a file with the same name already exists."""
    if not destination.exists():
        return destination

    counter = 1
    while True:
        candidate = destination.with_name(
            f"{destination.stem}_{counter}{destination.suffix}"
        )
        if not candidate.exists():
            return candidate
        counter += 1


def organize_directory(target_dir: str | Path, dry_run: bool = False) -> dict[str, int]:
    """Sort files in target_dir into subfolders by file type."""
    base_path = Path(target_dir).expanduser().resolve()
    if not base_path.is_dir():
        raise NotADirectoryError(f"Directory not found: {base_path}")

    summary: dict[str, int] = {}

    for item in base_path.iterdir():
        if not item.is_file() or item.name.startswith("."):
            continue

        category = get_category(item.suffix)
        category_dir = base_path / category
        destination = resolve_collision(category_dir / item.name)

        if not dry_run:
            category_dir.mkdir(exist_ok=True)
            shutil.move(str(item), str(destination))

        summary[category] = summary.get(category, 0) + 1

    return summary


if __name__ == "__main__":
    counts = organize_directory(".", dry_run=True)
    for folder, count in counts.items():
        print(f"{folder}: {count} file(s)")