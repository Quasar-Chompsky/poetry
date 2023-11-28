#ANSI escape codes for formatting
bold = "\033[1m"
italic = "\033[3m"
reset = "\033[0m"

def print_poem(poem_dict):
    for key, value in poem_dict.items():
        print(f"{bold}{key}{reset}\n{italic}{value}{reset}\n")

def add_to_poem(poem_dict): 
    key = input("Enter a key for the poem: ")
    value = input("Enter a poetic description: ")
    poem_dict[key] = value
    print(f"\n'{key}' added to the poem!\n")

#initialize dictionary    
sky_ocean = {
    'darkest night':'infinite light',
    'no':'straight lines',
    'band':'scraping chairs, adjusting stands',
    'bird':'jagged chatter',
    'sand':'coarse on my soul',
    'sky':'ocean',
    'love':'melting snowcones',
    'jazz':'honey from my mouth'
    }

#allow user to interact
while True:
    print("\nOptions:")
    print("1. Print Poem")
    print("2. Add to Poem")
    print("3. Exit")

    choice = input("Select an option (1/2/3): ")

    if choice == '1':
        print_poem(sky_ocean)
    elif choice == '2':
        add_to_poem(sky_ocean)
    elif choice == '3':
        print("Thank you so much for joining.")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")


