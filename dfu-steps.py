import time
import os

def get_device_model():
    print("Select your iPhone model:")
    print("1. iPhone 5s - iPhone 6s")
    print("2. iPhone 7")
    print("3. iPhone 8 - iPhone X")
    
    choice = input("Enter the number corresponding to your device: ")
    return choice

def show_dfu_instructions(model):
    if model == "1":
        steps = [
            "Step 1: Connect your iPhone to your computer using a USB cable.",
            "Step 2: Make sure your iPhone is turned on.",
            "Step 3: Press and hold both the Power (or Side) button and the Home button for 8 seconds.",
            "Step 4: After 8 seconds, release the Power button but keep holding the Home button.",
            "Step 5: Continue holding the Home button until iTunes (or Finder on macOS Catalina and later) detects the iPhone in recovery mode.",
            "Step 6: If the screen stays black, your iPhone is now in DFU mode.",
            "Step 7: To exit DFU mode, press and hold both the Power button and the Home button until the Apple logo appears."
        ]
    
    elif model == "2":
        steps = [
            "Step 1: Connect your iPhone to your computer using a USB cable.",
            "Step 2: Make sure your iPhone is turned on.",
            "Step 3: Press and hold both the Volume Down button and the Power (or Side) button for 8 seconds.",
            "Step 4: After 8 seconds, release the Power button but keep holding the Volume Down button.",
            "Step 5: Continue holding the Volume Down button until iTunes (or Finder on macOS Catalina and later) detects the iPhone in recovery mode.",
            "Step 6: If the screen stays black, your iPhone is now in DFU mode.",
            "Step 7: To exit DFU mode, press and hold both the Volume Down button and the Power button until the Apple logo appears."
        ]
    
    elif model == "3":
        steps = [
            "Step 1: Connect your iPhone to your computer using a USB cable.",
            "Step 2: Make sure your iPhone is turned on.",
            "Step 3: Quickly press and release the Volume Up button, then quickly press and release the Volume Down button.",
            "Step 4: Press and hold the Side button until the screen goes black.",
            "Step 5: As soon as the screen goes black, press and hold both the Volume Down button and the Side button for 5 seconds.",
            "Step 6: After 5 seconds, release the Side button but keep holding the Volume Down button.",
            "Step 7: Continue holding the Volume Down button until iTunes (or Finder on macOS Catalina and later) detects the iPhone in recovery mode.",
            "Step 8: If the screen stays black, your iPhone is now in DFU mode.",
            "Step 9: To exit DFU mode, press and hold both the Side button and the Volume Down button until the Apple logo appears."
        ]
    
    else:
        print("Invalid choice. Please run the script again and select a valid option.")
        return
    
    print("\n--- DFU Mode Instructions for Your iPhone ---\n")
    
    for step in steps:
        print(step)
    
    print("\n--- End of Instructions ---\n")

def check_dfu_mode():
    time.sleep(20)  # Wait for 20 seconds
    in_dfu = input("Are you in DFU mode? y/n: ")
    
    if in_dfu.lower() == 'y':
        os.system("python ipwndfu -p")
    elif in_dfu.lower() == 'n':
        print("Let's try the steps again.")
        main()
    else:
        print("Invalid input. Please enter 'y' or 'n'.")
        check_dfu_mode()

def main():
    device_model = get_device_model()
    show_dfu_instructions(device_model)
    check_dfu_mode()

if __name__ == "__main__":
    main()
