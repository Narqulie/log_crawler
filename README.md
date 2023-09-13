

# Python Log Crawler

**Python Log Crawler** is a command-line utility designed to aid developers, system administrators, and curious users alike in their file management and analysis tasks. By crawling through directories, this tool quickly identifies and processes files based on search terms, giving immediate feedback on matches. If you've ever been in a situation where you needed to sift through log files or documents in search of specific content, this tool can save you ample time.

## Features

* **File Search**: Search for any term within files of a specific extension in a given directory.
* **Case Sensitivity Toggle**: By default, the search is case-insensitive, but can easily be switched to a case-sensitive mode using the `-c` or `--case-sensitive` flag.
* **Robust Logging**: The tool not only searches but logs the process, making it easy to review and understand the search progression and results.

## Usage

1. Clone the repository:

```
git clone https://github.com/Narqulie/log_crawler.git
cd log_crawler
```

2. Run the program:

```
python log_crawler.py [search_term] [file_ext] [directory] (optional flags)
```

### Example:

To search for the term "ERROR" within `.log` files in the `./logs` directory:

```
python log_crawler.py ERROR log ./logs
```

To conduct the same search but in a case-sensitive manner:

```
python log_crawler.py ERROR log ./logs --case-sensitive
```

## Contribute

Feel free to dive in! [Open an issue](https://github.com/Narqulie/log_crawler/issues) or submit PRs.

## License

[MIT](LICENSE) © [Narqulie](https://github.com/Narqulie)

---
