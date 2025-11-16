#include <iostream>
#include <string>
#include <utility>
#include <limits>    // for std::numeric_limits
#include <climits>   // for INT_MAX

class Item {
private:
    std::string name;
    int quantity;
    float price;

public:
    // Constructor
    Item(std::string name, int quantity, float price)
        : name{std::move(name)}, quantity{quantity}, price{price} {}

    // Getters and setters
    std::string get_name() const { return name; }
    int get_quantity() const { return quantity; }
    void set_quantity(int new_quantity) { quantity = new_quantity; }
    float get_price() const { return price; }

    bool is_match(const std::string &other) const {
        return name == other;
    }
};

class Inventory {
private:
    Item* items[20];     // Fixed array of pointers
    float total_money;
    int item_count;

    // Static helper to display a single item
    static void display_data(const Item &item) {
        std::cout << "\nItem name: " << item.get_name();
        std::cout << "\nQuantity: " << item.get_quantity();
        std::cout << "\nPrice: " << item.get_price();
    }

public:
    Inventory() : items{}, total_money{0}, item_count{0} {}

    // Destructor to clean up memory
    ~Inventory() {
        for (int i = 0; i < item_count; i++) {
            delete items[i];
        }
    }

    void add_item() {
        if (item_count >= 20) {
            std::cout << "\nInventory full. Cannot add more items.\n";
            return;
        }

        std::string name;
        int quantity;
        float price;

        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n'); //Clear buffer
        std::cout << "\nEnter item name: ";
        std::cin >> name;
        std::cout << "Enter quantity: ";
        std::cin >> quantity;
        std::cout << "Enter price: ";
        std::cin >> price;

        items[item_count] = new Item(name, quantity, price);
        item_count++;
        std::cout << "\nItem added successfully!\n";
    }

    void sell_item() {
        if (item_count == 0) {
            std::cout << "\nInventory empty. Nothing to sell.\n";
            return;
        }

        std::string item_to_check;
        std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
        std::cout << "\nEnter item name: ";
        std::cin >> item_to_check;

        for (int i = 0; i < item_count; i++) {
            if (items[i]->is_match(item_to_check)) {
                remove_item(i);
                return;
            }
        }
        std::cout << "\nThis item is not in your Inventory.\n";
    }

    void remove_item(int item_index) {
        int input_quantity;
        Item *item = items[item_index];
        std::cout << "\nEnter number of items to sell: ";
        std::cin >> input_quantity;

        int quantity = item->get_quantity();
        if (input_quantity <= quantity) {
            float price = item->get_price();
            float money_earned = price * input_quantity;
            item->set_quantity(quantity - input_quantity);
            total_money += money_earned;

            std::cout << "\nItems sold.";
            std::cout << "\nMoney received: " << money_earned << "\n";

            //Remove item if quantity becomes zero
            if (item->get_quantity() == 0) {
                delete items[item_index];
                for (int j = item_index; j < item_count - 1; j++) {
                    items[j] = items[j + 1];
                }
                item_count--;
                std::cout << "Item removed from inventory (quantity 0).\n";
            }
        } else {
            std::cout << "\nCannot sell more items than you have.\n";
        }
    }

    void list_items() const {
        if (item_count == 0) {
            std::cout << "\nInventory empty.\n";
            return;
        }

        std::cout << "\n=== Current Inventory ===\n";
        for (int i = 0; i < item_count; i++) {
            display_data(*items[i]);
            std::cout << "\n";
        }
        std::cout << "\nTotal Money Earned: " << total_money << "\n";
    }
};

// No need to modify main()
int main() {
    int choice;
    Inventory inventory_system;
    std::cout << "Welcome to the inventory!";

    while (true) {
        std::cout << "\n\nMENU\n"
                  << "1. Add new item\n"
                  << "2. Sell item\n"
                  << "3. List items\n"
                  << "4. Exit\n\n"
                  << "Enter your choice: ";
        std::cin >> choice;

        switch (choice) {
            case 1:
                inventory_system.add_item();
                break;
            case 2:
                inventory_system.sell_item();
                break;
            case 3:
                inventory_system.list_items();
                break;
            case 4:
                std::cout << "\nExiting program. Goodbye!\n";
                return 0;
            default:
                std::cout << "\nInvalid choice entered.\n";
                std::cin.clear();
                std::cin.ignore(INT_MAX, '\n');
                break;
        }
    }
}
