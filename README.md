# Difference Calculator

Runs from the command line, compares two configuration files and shows a difference.
Working with JSON and YAML.

## Usage

**help:**

```bash
$ gendiff -h
```

**Running the script with default settings:**

```bash
$ gendiff <file_path1> <file_path2>
```

## DEMO

Comparison of two files in the JSON format:
[![asciicast](https://asciinema.org/a/ejkADXLd9g2msAOn69mFGF4QA.svg)](https://asciinema.org/a/ejkADXLd9g2msAOn69mFGF4QA)

Comparison of two nested files in the YAML format:
[![asciicast](https://asciinema.org/a/GPsU3IE88CcxFpnzOwH9sSgqN.svg)](https://asciinema.org/a/GPsU3IE88CcxFpnzOwH9sSgqN)

Comparison of two files in the JSON format with plain output:
[![asciicast](https://asciinema.org/a/HP4Y0O4C2tGsWBXspZRYU5BJK.svg)](https://asciinema.org/a/HP4Y0O4C2tGsWBXspZRYU5BJK)

### Links

This project was built using these tools:

| Tool                                                                        | Description                                             |
|-----------------------------------------------------------------------------|---------------------------------------------------------|
| [poetry](https://poetry.eustace.io/)                                        | "Python dependency management and packaging made easy"  |
| [Py.Test](https://pytest.org)                                               | "A mature full-featured Python testing tool"            |

### Hexlet tests and linter status:
[![Actions Status](https://github.com/NikGor/python-project-50/workflows/hexlet-check/badge.svg)](https://github.com/NikGor/python-project-50/actions)
[![Github Actions Status](https://github.com/NikGor/python-project-50/workflows/main/badge.svg)](https://github.com/NikGor/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/ea0a78c5e95e083ec768/maintainability)](https://codeclimate.com/github/NikGor/python-project-50/maintainability)
[![Test Coverage](https://api.codeclimate.com/v1/badges/ea0a78c5e95e083ec768/test_coverage)](https://codeclimate.com/github/NikGor/python-project-50/test_coverage)