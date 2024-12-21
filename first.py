def main():
    greeting = input("enter expression: ")
    if greeting.startswith("hello"):
        print("$0")
    if greeting.startswith("how"):
        print("$100")

if __name__ == "__main__":
    main()

