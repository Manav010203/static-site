from markdown_block import markdown_to_html_node
import os
from pathlib import Path
def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    for filename in os.listdir(dir_path_content):
        from_path = os.path.join(dir_path_content, filename)
        dest_path = os.path.join(dest_dir_path, filename)
        if os.path.isfile(from_path):
            dest_path = Path(dest_path).with_suffix(".html")
            generate_page(from_path, template_path, dest_path,basepath)
        else:
            generate_pages_recursive(from_path, template_path, dest_path,basepath)
def extract_title(md):
    lines = md.split("\n")
    for line in lines:
        if line.startswith("#"):
            return line[2:]
        raise ValueError("no title found")


def generate_page(from_path,template_path,dest_path,basepath):
    print(f"Generating from {from_path} to {dest_path} using {template_path}.")
    with open(from_path,"r") as f:
        md_content  = f.read()
    with open(template_path,"r") as f:
        temp_content = f.read()

    content_html = markdown_to_html_node(md_content).to_html()
    # temp_content_html = markdown_to_html_node(temp_content).to_html()
    title = extract_title(md_content)
    temp = temp_content.replace("{{ Title }}",title)
    temp_content = temp.replace("{{ Content }}",content_html)

    os.makedirs(os.path.dirname(dest_path),exist_ok=True)

    with open(dest_path,"w") as f:
        f.write(temp_content)
    