import os

# Access the secret from environment variables
my_secret = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")

if my_secret:
    print(f"The secret is added to the environment")
else:
    print("MY_SECRET is not set in the environment.")
