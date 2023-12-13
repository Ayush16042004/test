# test.py
import os

# Get the current counter value from the environment variable
counter = int(os.getenv("COUNTER", 0))

# Increment the counter
counter += 1

# Print the updated counter
print(f"Counter: {counter}")

# Set the counter as an environment variable for the next run
os.environ["COUNTER"] = str(counter)
