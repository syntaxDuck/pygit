# pygit

A minimal Python implementation of Git, built for learning purposes.

## Current Status

This project is in early development. Only the most basic functionality is implemented.

## Implemented Features

- **`init`** - Initialize a new Git repository with the standard `.git` directory structure

## Usage

```bash
python main.py
```

This will initialize a new repository in the `new/` directory.

## Project Structure

```
pygit/
├── main.py          # Entry point with core functions
└── .git/            # Git directory (created on init)
    ├── objects/     # Git objects
    ├── refs/        # References
    │   └── heads/   # Branch heads
    └── HEAD         # Current reference
```

## Roadmap

- [ ] Complete `hash-object` implementation
- [ ] Add `cat-file` command
- [ ] Add `commit` functionality
- [ ] Add `log` command
- [ ] Add branch support

## Learning Resources

This project follows the [Build Your Own Git](https://github.com/codecrafters-io/build-your-own-x#build-your-own-git) approach to understanding how Git works under the hood.
