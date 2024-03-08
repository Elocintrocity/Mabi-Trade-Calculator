import time
def get_town():
    """Gets the town by presenting a numbered list."""
    towns = [
        "Tir Chonaill", "Dunbarton", "Bangor", "Emain Macha", "Taillteann",
        "Tara", "Port Cobh", "Commonwealth of Belvast", "Qilla", "Filia", "Vales", "Cor"
    ]

    print("Available Towns:")
    for i, town_name in enumerate(towns):
        print(f"{i+1}. {town_name}")

    while True:
        try:
            town_choice = int(input("Enter the number corresponding to your town: "))
            if 1 <= town_choice <= len(towns):
                return towns[town_choice - 1]  
            else:
                print("Invalid choice. Please enter a number from the list.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def calculate_profit(buy_price, sell_price, quantity):
    """Calculates profit for a single trade."""
    total_cost = buy_price * quantity
    total_revenue = sell_price * quantity
    profit = total_revenue - total_cost
    return profit

def find_trade_data(town):
    """Gets trade data for items in a specific town."""
    town_items = {
        "Tir Chonaill": ["Baby Potion", "Diet Potion", "Snore Prevention Potion", 
                         "Wild Ginseng Potion", "Lovely Potion"],
        "Dunbarton": ["Spider Gloves", "Wool Boots", "Ogre Executioner Mask", 
                      "Incubus Suit", "Succubus Swimsuit"],
        "Bangor": ["Bangor Coal", "Marble", "Topaz", "Highlander Ore", "Lead"],
        "Emain Macha": ["Berry Granola", "Butter Beer", "Smoked Wild Animal", 
                        "Triple Pasta", "Whole BBQ Bear"],
        "Taillteann": ["Heat Crystal", "Music Box Preservation Stone", "Palala Crystal", 
                       "Circle Barrier Spike Crystal", "Alchemy Crystal"],
        "Tara": ["Mini Dressing Table", "Tea Table", "Rocking Chair", 
                 "Bunk Bed", "Giant Wine Rack"],
        "Port Cobh": ["Cobh Seaweed", "Cobh Oyster", "Shark Fin", "Jelly Fish", "Neid Scales"],
        "Commonwealth of Belvast": ["Iron Whip", "Dark Sword", "Safe", "Skeleton Ogre Armor", "Fake Morgant Helmet"],
        "Qilla": ["Mint Chocolate Powder", "Fresh Pomegranate", "Mana Tunnel Figure", 
                  "Exploration Rescue Kit", "Kaypi Cactus Essence"],
        "Filia": ["Small Glass Chunk", "Cinnamon Perfume", "Dried Saffron", 
                  "Longa Natural Rock Salt", "Filia-Style Jerky"],
        "Vales": ["Vales Padded Coat", "Natural Glacial Water", "Ice Skates", "Snowboard", 
                  "Vales Vodka"],
        "Cor": ["Courcle Ruins Souvenir", "Large Ritual Mask", "La Terra Raspberry", 
                "Artifact Restoration Tool Set", "Courcle Natural Rubber"],
    }

    trade_results = []
    for item_name in town_items.get(town, []):
        buy_price_str = input(f"Enter the buying price of {item_name} (or press Enter to skip): ")
        if not buy_price_str:
            break  # Stop asking if the user pressed Enter

        buy_price = float(buy_price_str)
        quantity = int(input("Enter the quantity of items bought: "))
        sell_price = float(input("Enter the sell price in the desired town: "))

        profit = calculate_profit(buy_price, sell_price, quantity)
        trade_results.append((item_name, profit))

    return trade_results

# --- Main Part ---
print("Mabinogi Commerce Calculator")

while True:  
    town = get_town()
    trade_results = find_trade_data(town)

    # Display trade comparisons
    print("\n--- Trade Comparisons (Most profitable first) ---")
    trade_results.sort(key=lambda x: x[1], reverse=True)
    for item_name, profit in trade_results:
        print(f"{item_name}: {profit} gold")

    another_trade = input("\nWould you like to do another trade? (1 for yes, 2 for no): ")
    if another_trade != '1':  
        break 

print("\nHope you made lots of Ducats! Exiting now", end='') 
for _ in range(3):  # Loop for 3 seconds
    print(".", end='', flush=True)  # Print a dot, don't go to a new line, and flush
    time.sleep(1)   # Wait for one second 
