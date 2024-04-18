import sys
import os
import re

def replace_patterns(template_content, settings):
    for key, value in settings.items():
        placeholder = '{' + key + '}'
        if placeholder in template_content:
            template_content = template_content.replace(placeholder, value)
    return template_content

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 render.py <file.template>")
        return

    template_file = sys.argv[1]

    if not template_file.endswith('.template'):
        print("Error: Input file must have a .template extension")
        return

    if not os.path.exists(template_file):
        print("Error: Input file does not exist")
        return

    output_file = template_file.replace('.template', '.html')

    with open(template_file, 'r') as file:
        template_content = file.read()

    settings = {}
    with open('settings.py', 'r') as settings_file:
        exec(settings_file.read(), settings)

    rendered_content = replace_patterns(template_content, settings)

    with open(output_file, 'w') as file:
        file.write(rendered_content)


if __name__ == '__main__':
    main()
