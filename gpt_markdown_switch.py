import re
import os

def modify_readme(readme_content):
    # Replace headers
    def replace_header(match):
        header, title = match.groups()
        return f'H{len(header)} {title.strip()}'


    header_pattern = re.compile(r'^(#+)(.*)$', re.MULTILINE)
    modified_content = header_pattern.sub(replace_header, readme_content)

    # Replace triple backticks, including the ones followed by a word
    modified_content = re.sub(r'```(\w*)', r"'''\1", modified_content)

    return modified_content

def reverse_modifications(modified_content):
    # Replace ''' with ``` and also restore the ones followed by a word
    reversed_content = re.sub(r"'''(\w*)", r'```\1', modified_content)

    # Replace header names (H1, H2, etc.) with header symbols (#, ##, etc.)
    def replace_reversed_header(match):
        header_level, title = int(match.group(1)), match.group(2)
        return f"{'#' * header_level} {title.strip()}"


    reversed_header_pattern = re.compile(r'^H(\d)(.*)$', re.MULTILINE)
    reversed_content = reversed_header_pattern.sub(replace_reversed_header, reversed_content)

    return reversed_content

if __name__ == '__main__':
    if os.path.exists('README.md'):
        with open('README.md', 'r') as file:
            readme_content = file.read()

        # Determine if the content needs to be modified or restored
        if 'H1' in readme_content or 'H2' in readme_content:
            updated_readme = reverse_modifications(readme_content)
        else:
            updated_readme = modify_readme(readme_content)

        with open('README.md', 'w') as file:
            file.write(updated_readme)
    else:
        print("README.md not found.")
