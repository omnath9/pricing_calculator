def get_positive_float_input(prompt_message):
    while True:
        try:
            user_input = input(prompt_message)
            value = float(user_input)
            if value >= 0:
                return value
            else:
                print("Input cannot be negative. Please try again.")
        
        except ValueError:
            print(f"Invalid input: '{user_input}' is not a valid number. Please try again.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

def calculate_final_price(base_price, tax_rate, discount_rate):
    discount_amount = base_price * (discount_rate / 100)
    price_after_discount = base_price - discount_amount
    tax_amount = price_after_discount * (tax_rate / 100)
    final_price = price_after_discount + tax_amount
    return {
        "base_price": base_price,
        "discount_amount": discount_amount,
        "price_after_discount": price_after_discount,
        "tax_amount": tax_amount,
        "final_price": final_price,
        "tax_rate": tax_rate,
        "discount_rate": discount_rate
    }

def display_receipt(results):
    print("\n--- TRANSACTION RECEIPT ---")
    
    print(f"{'Base Price:':<25} ${results['base_price']:>10.2f}")
    
    discount_label = f"Discount ({results['discount_rate']}%):"
    print(f"{discount_label:<25} -${results['discount_amount']:>10.2f}")
    
    print(f"{'Price Before Tax:':<25} ${results['price_after_discount']:>10.2f}")
    
    tax_label = f"Tax ({results['tax_rate']}%):"
    print(f"{tax_label:<25} +${results['tax_amount']:>10.2f}")
    
    print("-" * 37)
    
    print(f"{'Final Total:':<25} ${results['final_price']:>10.2f}")
    print("---------------------------\n")

def main():
    """
    Main function to run the price calculator.
    """
    print("=== Basic Price Calculator ===")
    print("Calculates the final price including tax and discounts.\n")
    
    base_price = get_positive_float_input("Enter the base price: ")
    discount_rate = get_positive_float_input("Enter the discount rate (e.g., 10 for 10%): ")
    tax_rate = get_positive_float_input("Enter the tax rate (e.g., 8.5 for 8.5%): ")

    calculation_results = calculate_final_price(base_price, tax_rate, discount_rate)
    display_receipt(calculation_results)
if __name__ == "__main__":
    main()
