import os
import hashlib
import zlib
from pathlib import Path


def write_file(path: Path, contents: str):
    with open(path, "wb") as file:
        file.write(contents)


def read_file(path: Path):
    with open(path, "rb") as file:
        content = file.read()
    return content


def init(repo: Path):
    git_path = repo / ".git"
    try:
        os.mkdir(repo)
    except FileExistsError as e:
        print("File already exists")

    try:
        os.mkdir(git_path)
        for dir in ["objects", "refs", "refs/heads"]:
            os.mkdir(git_path / dir)
    except FileExistsError as e:
        print("Git repo already initialized")

    write_file(git_path / "HEAD", b"ref: refs/heads/main")
    print(f"Initialized empty repo {repo}")


def hash_obj(data: str, type: str, write: bool = True):
    header = f"{type} {len(data)}".encode() + b"\0x00"
    full_data = header + data
    sha1 = hashlib.sha1(full_data).hexdigest()
    if write:
        path = Path(".git" / object / sha1[:2] / sha1[2:])
        if not os.path.exists(path):
            os.makedirs(path.parent, exist_ok=True)
            write_file(path, zlib.compress(sha1))
    return sha1


if __name__ == "__main__":
    init(Path("new"))
