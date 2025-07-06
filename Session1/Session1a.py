# Below are the few example of  if / elif else

# ////////First //////////////

stock_price = float(input("Enter current stock price: "))    # This is input command /syntax #
if (stock_price >= 2000 and stock_price <= 3000):
    print("Stock is too expensive, consider selling.")
elif stock_price > 1000:
    print("Stock is moderately priced, hold for now.")
elif stock_price > 500:
    print("Stock is reasonably priced, you may buy more.")
else:
    print("Stock is very cheap, strong buy signal!")


# ####################
current_price = 150
previous_price = 140

if current_price > previous_price * 1.02:  # >2% rise
    print("📈 BUY → Price is rising!")
    print("Stock price increased: \U0001F680")  # Up Arrow

elif current_price < previous_price * 0.98:  # >2% drop
    print("📉 SELL ↓ Price is dropping!")
    print("Stock price decreased: \u2193")  # Down Arrow

else:
    print("➖ HOLD → Price is stable.")
    print("Target reached: \u2714")  # Check Mark250

print("Profit increased 🚀 \U0001F4C8")  # Rocket + Chart Up
print("Loss occurred 🔴 \U0001F4C9")  # Red Circle + Chart Down
print("All good! 😄")  # Smiling Face

print(f"{current_price=}") ## Using f-string in print