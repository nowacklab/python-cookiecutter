from .{{cookiecutter.project_slug}} import {{cookiecutter.project_slug}}

def main():
    {{cookiecutter.project_slug}}()
    return 0

if __name__ == "__main__":
    import sys
    sys.exit(main())

