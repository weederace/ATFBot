import pyautogui
import time
import random
import threading

mouse_lock = threading.Lock()

def click_coin(coin_x, coin_y):
    """Clicks on the coin every 9 seconds"""
    while True:
        time.sleep(9) # Wait for exactly 9 seconds
        
        # Small random offset to prevent bot detection
        offset_x = random.randint(-20, 20)
        offset_y = random.randint(-20, 20)
        
        with mouse_lock:
            pyautogui.click(coin_x + offset_x, coin_y + offset_y)
            print("[*] Clicked ATF Coin. Next in 9 seconds.")

def click_claim(claim_x, claim_y):
    """Clicks the Claim button exactly every 10 minutes"""
    while True:
        time.sleep(600) # 600 seconds = 10 minutes
        
        # Small random offset for the claim button
        offset_x = random.randint(-40, 40)
        offset_y = random.randint(-5, 5)
        
        with mouse_lock:
            pyautogui.click(claim_x + offset_x, claim_y + offset_y)
            print("[!] Clicked CLAIM button.")

if __name__ == "__main__":
    print("--- Bot Initial Setup ---")
    
    # 1. Get coin coordinates with a timer
    print("\n1. Move the mouse over the ATF coin. You have 5 seconds...")
    for i in range(5, 0, -1):
        print(f"Time remaining: {i} seconds...", end="\r")
        time.sleep(1)
    COIN_X, COIN_Y = pyautogui.position()
    print(f"\n✅ Coin coordinates saved: (X: {COIN_X}, Y: {COIN_Y})")
    
    # 2. Get Claim button coordinates with a timer
    print("\n2. Now move the mouse over the CLAIM button. You have 5 seconds...")
    for i in range(5, 0, -1):
        print(f"Time remaining: {i} seconds...", end="\r")
        time.sleep(1)
    CLAIM_X, CLAIM_Y = pyautogui.position()
    print(f"\n✅ Button coordinates saved: (X: {CLAIM_X}, Y: {CLAIM_Y})\n")
    
    print("-" * 50)
    print("🚀 Bot has started! Press Ctrl+C in this window to stop it.")
    
    # Run the tasks concurrently
    coin_thread = threading.Thread(target=click_coin, args=(COIN_X, COIN_Y), daemon=True)
    claim_thread = threading.Thread(target=click_claim, args=(CLAIM_X, CLAIM_Y), daemon=True)
    
    coin_thread.start()
    claim_thread.start()
    
    # Keep the main program running
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 Bot stopped.")