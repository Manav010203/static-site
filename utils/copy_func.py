import os
import shutil
def content_func(src,dst):
    if not os.path.exists(src):
        raise FileNotFoundError("no file at the given source path")
    if not os.path.exists(dst):
        os.mkdir(dst)
    src_content = os.listdir(src)
    for item in src_content:
        src_path = os.path.join(src,item)
        dst_path = os.path.join(dst,item)
        if os.path.isfile(src_path):
            shutil.copy(src_path,dst_path)
        else:
            content_func(src_path,dst_path)

def main():
    # Copy static → public
    content_func("static", "public")
    print("✅ Site build complete: static → public")


if __name__ == "__main__":
    main()
