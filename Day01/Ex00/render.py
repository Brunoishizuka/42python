import sys
import os

def render_template(template_file):
    if not template_file.endswith('.template'):
        raise Exception("Invalid file extension. The file should end with.template")

    if not os.path.exists(template_file):
        raise FileNotFoundError("The file does not exist")

    if len(sys.argv)!= 2:
        raise Exception("Wrong number of arguments. The program should be called with one argument")

    with open(template_file, 'r') as file:
        content = file.read()

    with open('settings.py', 'r') as file:
        exec(file.read())

    rendered_content = content.format(**locals())

    html_file = os.path.splitext(template_file)[0] + '.html'
    with open(html_file, 'w') as file:
        file.write(rendered_content)

if __name__ == '__main__':
    try:
        render_template(sys.argv[1])
    except Exception as e:
        print(e)