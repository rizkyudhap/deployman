from cli.prompts import main_menu
from generator.renderer import render_yaml

def main():
    choice, answers = main_menu()
    render_yaml(choice, answers)

if __name__ == "__main__":
    main()
