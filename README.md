<h1 align="center"> <br>GPT Markdown Toggle</h1> <h4 align="center">A Python script that toggles between custom and standard markdown formats.</h4> <p align="center"> <a href="https://github.com/itsbrex/GPT-Markdown-Toggle/commits/master"> <img src="https://img.shields.io/github/last-commit/itsbrex/GPT-Markdown-Toggle.svg?style=flat-square&logo=github&logoColor=white" alt="GitHub last commit"> <a href="https://github.com/itsbrex/GPT-Markdown-Toggle/issues"> <img src="https://img.shields.io/github/issues-raw/itsbrex/GPT-Markdown-Toggle.svg?style=flat-square&logo=github&logoColor=white" alt="GitHub issues"> <a href="https://github.com/itsbrex/GPT-Markdown-Toggle/pulls"> <img src="https://img.shields.io/github/issues-pr-raw/itsbrex/GPT-Markdown-Toggle.svg?style=flat-square&logo=github&logoColor=white" alt="GitHub pull requests"> <a href="https://twitter.com/intent/tweet?text=Try this GPT Markdown Toggle:&url=https%3A%2F%2Fgithub.com%2FGPT-Markdown-Toggle%2FGPT-Markdown-Toggle"> <img src="https://img.shields.io/twitter/url/https/github.com/itsbrex/GPT-Markdown-Toggle.svg?style=flat-square&logo=twitter" alt="GitHub tweet"> <p align="center"> <a href="#overview">Overview</a> • <a href="#requirements">Requirements</a> • <a href="#usage">Usage</a> • <a href="#features">Features</a> • <a href="#contributing">Contributing</a> • <a href="#contributors">Contributors</a> • <a href="#license">License</a> </p>


## Overview

GPT Markdown Toggle is a Python script that allows you to toggle between custom markdown format and standard markdown format. The custom markdown format uses headers represented by H1, H2, H3, etc., triple single quotes (```) for fenced code blocks, and single backticks (`) for inline code snippets so that you can *actualy* get back single code blocks instead of mutliple rended markdown code blocks.

## Requirements

- Python 3.6+

## Usage

1. Place the script in the same directory as your `README.md` file.
2. Run the script using the following command:

```
python3 gpt_markdown_toggle.py
```

The script will automatically detect if your `README.md` is in custom markdown format or standard markdown format and convert it accordingly.


## Features

- Toggle between custom markdown format and standard markdown format
- Replace headers with custom format (H1, H2, H3, etc.)
- Replace triple backticks with triple single quotes for fenced code blocks
- Keep single backticks for inline code snippets

## Contributing

If you find any bugs or want to suggest new features, please feel free to contribute by submitting an [issue](https://github.com/GPT-Markdown-Toggle/issues) or a [pull request](https://github.com/GPT-Markdown-Toggle/pulls).

## Contributors ✨
Thanks goes to these wonderful people ([emoji key](https://github.com/all-contributors/all-contributorsH1emoji-key)):

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/github/all-contributors/itsbrex/GPT-Markdown-Toggle?color=ee8449&style=flat-square)](H1Contributing)
<!-- ALL-CONTRIBUTORS-BADGE:END -->

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->
This project follows the [all-contributors](https://allcontributors.org/) specification. Contributions of any kind welcome!

## License

Licensed under the MIT license. See the [LICENSE](./LICENSE) file for more information.

If you found this project interesting or helpful, please consider [sponsoring me](https://github.com/sponsors/GPT-Markdown-Toggle) or <a href="https://twitter.com/GPT-Markdown-Toggle">following me on twitter <img src="https://storage.googleapis.com/saasify-assets/twitter-logo.svg" alt="twitter" height="24px" align="center"></a>


### GPT README Prompt

<details>
<summary>🔥 Use this prompt to get single markdown code block responses</summary>

```
Write a readme for my repository named "REPOSITORY NAME" based on the following code and using the custom markdown format where headers are represented by H1, H2, H3, etc., triple single quotes (''') are used for fenced code blocks, and single backticks (`) are used for inline code snippets:

PASTE YOUR CODE HERE
```
