<h1 align="center"> <br>GPT Markdown Switch 🪄</h1> <h4 align="center">A simple tool that enables ChatGPT to output raw markdown without rendering code blocks.</h4> <p align="center"> <a href="https://github.com/itsbrex/gpt-markdown-switch/commits/master"> <img src="https://img.shields.io/github/last-commit/itsbrex/gpt-markdown-switch.svg?style=flat-square&logo=github&logoColor=white" alt="GitHub last commit"> <a href="https://github.com/itsbrex/gpt-markdown-switch/issues"> <img src="https://img.shields.io/github/issues-raw/itsbrex/gpt-markdown-switch.svg?style=flat-square&logo=github&logoColor=white" alt="GitHub issues"> <a href="https://github.com/itsbrex/gpt-markdown-switch/pulls"> <img src="https://img.shields.io/github/issues-pr-raw/itsbrex/gpt-markdown-switch.svg?style=flat-square&logo=github&logoColor=white" alt="GitHub pull requests"> <a href="https://twitter.com/intent/tweet?text=Try this GPT Markdown Toggle:&url=https%3A%2F%2Fgithub.com%2Fgpt-markdown-switch%2Fgpt-markdown-switch"> <img src="https://img.shields.io/twitter/url/https/github.com/itsbrex/gpt-markdown-switch.svg?style=flat-square&logo=twitter" alt="GitHub tweet"> <p align="center"> <a href="#overview">Overview</a> • <a href="#requirements">Requirements</a> • <a href="#usage">Usage</a> • <a href="#features">Features</a> • <a href="#contributing">Contributing</a> • <a href="#contributors">Contributors</a> • <a href="#license">License</a> </p>


## Overview

GPT Markdown Switch has two main components. The first is a custom prompt to generate *actual* single codeblock README files that can easily be copy and pasted into your project. The second is a Python script that allows you to toggle between custom markdown format and standard markdown format. The custom markdown format uses headers represented by `H1`, `H2`, `H3`, etc., triple single quotes `'''` for fenced code blocks, and single backticks for inline code snippets so that you *actually* get back single code blocks instead of multiple rendered markdown code blocks.

### Why did I make this? 
It's annoying when ChatGPT renders fenced code blocks within Markdown directly on the page, making it hard to copy everything at once. I wanted a way to create README files for my projects that I could easily copy and paste, so I created a custom prompt that tells ChatGPT to replace traditional Markdown syntax with custom syntax so it doesn't render on the page. This worked, but the custom Markdown format still needed to be converted back to regular markdown for the actual README file. To fix this, I made a Python script that automatically detects the current format and switches everything accordingly. Badabing! With GPT Markdown Switch, you can now generate full code block README files (or any other Markdown content) that are easy to copy and paste.
## Features

- Toggle between custom markdown format and standard markdown format
- Replace headers with custom format (H1, H2, H3, etc.)
- Replace triple backticks with triple single quotes for fenced code blocks
- Keep single backticks for inline code snippets

## Requirements

- Python 3.6+

## Usage
### GPT README Prompt
<details>
<summary>🔥 Use this prompt to get a single markdown code block responses 🔥</summary>

```
Write a readme for my repository named "REPOSITORY NAME" based on the following code and using the custom markdown format where headers are represented by H1, H2, H3, etc., triple single quotes (''') are used for fenced code blocks, and single backticks (`) are used for inline code snippets:

PASTE YOUR CODE HERE
```
</details>

1. Once you are ready to generate a `README` for your project, go to [ChatGPT](https://chat.openai.com/) and enter the prompt above, followed by the code for your main script and/or `package.json` file to provide more context.
2. Save the response as `README.md` in the root of your project directory.
3. Run the script in the same directory as your `README.md` file with the following command:

```
python3 gpt_markdown_toggle.py
```

The script will automatically detect if your `README.md` is in custom markdown format or standard markdown format and convert it accordingly.

## Contributing

If you find any bugs or want to suggest new features, please feel free to contribute by submitting an [issue](https://github.com/gpt-markdown-switch/issues) or a [pull request](https://github.com/gpt-markdown-switch/pulls).

## Contributors ✨
Thanks goes to these wonderful people ([emoji key](https://github.com/all-contributors/all-contributorsH1emoji-key)):

<!-- ALL-CONTRIBUTORS-BADGE:START - Do not remove or modify this section -->
[![All Contributors](https://img.shields.io/github/all-contributors/itsbrex/gpt-markdown-switch?color=ee8449&style=flat-square)](H1Contributing)
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

If you found this project interesting or helpful, please consider [sponsoring me](https://github.com/sponsors/gpt-markdown-switch) or <a href="https://twitter.com/gpt-markdown-switch">following me on twitter <img src="https://storage.googleapis.com/saasify-assets/twitter-logo.svg" alt="twitter" height="24px" align="center"></a>
