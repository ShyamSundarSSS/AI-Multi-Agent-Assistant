from graph import app


def main():

    print("=" * 50)
    print("      AI Multi-Agent Assistant")
    print("=" * 50)

    print("\nAvailable Tasks:")
    print("- Weather Information")
    print("- Currency Conversion")
    print("- General Questions")
    print("\nType 'exit' to quit.\n")

    while True:

        user_input = input("You: ")

        if user_input.lower() == "exit":
            print("\nGoodbye!")
            break

        initial_state = {
            "user_input": user_input,
            "agent": "",
            "result": ""
        }

        response = app.invoke(initial_state)

        print("\nAssistant:")
        print(response["result"])
        print()


if __name__ == "__main__":
    main()