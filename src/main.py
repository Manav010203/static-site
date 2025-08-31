from textnode import TextNode
import sys, os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from utils.copy_func import content_func
from gencontent import generate_page,generate_pages_recursive
import shutil
dir_path_static = "./static"
dir_path_public = "./public"
dir_path_content = "./content"
template_path = "./template.html"
default_basepath = "/"

def main():
    basepath = default_basepath
    if len(sys.argv) > 1:
        basepath = sys.argv[1]

    if not os.path.exists(dir_path_static):
        raise Exception(f"Source {dir_path_static} doesn't exists")

    if os.path.exists(dir_path_public):
        print(f"Destination {dir_path_public} already exists - REMOVING")
        shutil.rmtree(dir_path_public)

    content_func(dir_path_static, dir_path_public)
    print("Generating content...")
    generate_pages_recursive(dir_path_content, template_path, dir_path_public, basepath)
if __name__=="__main__":
    main()