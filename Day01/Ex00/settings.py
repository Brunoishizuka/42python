import sys
import os
import re

def render_template(template_file, settings_file):
    # Check if template file exists
    if not os.path.exists(template_file):
        print("Error: Template file not found.")
        return
    
    # Check if template file has correct extension
    if not template_file.endswith('.template'):
        print("Error: Template file must have .template extension.")
        return
    
    # Check if settings file exists
    if not os.path.exists(settings_file):
        print("Error: Settings file not found.")
        return
    
    # Read template content
    with open(template_file, 'r') as template:
        template_content = template.read()
    
    # Read settings
    with open(settings_file, 'r') as settings:
        settings_content = settings.read()
    
    # Extract settings from settings_content
    settings_dict = {}
    exec(settings_content, settings_dict)
    
    # Replace patterns in template with settings values
    for key, value in settings_dict.items():
        template_content = re.sub(r'\{' + key + r'\}', value, template_content)
    
    # Write result to html file
    output_file = os.path.splitext(template_file)[0] + '.html'
    with open(output_file, 'w') as output:
        output.write(template_content)
    
    print(f"File '{output_file}' successfully created.")

if __name__ == "__main__":
    # Check if correct number of arguments provided
    if len(sys.argv) != 2:
        print("Usage: python3 render.py <template_file>")
        sys.exit(1)
    
    template_file = sys.argv[1]
    settings_file = "settings.py"  # Assuming settings.py is in the same directory
    
    render_template(template_file, settings_file)
