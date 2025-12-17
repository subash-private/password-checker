from zxcvbn import zxcvbn
import getpass

password = getpass.getpass("Enter password: ")

result = zxcvbn(password)

print("Score (0–4):", result["score"])
print("Estimated crack time (offline fast hash):",
      result["crack_times_display"]["offline_fast_hashing_1e10_per_second"])

if result["feedback"]["warning"]:
    print("Warning:", result["feedback"]["warning"])

if result["feedback"]["suggestions"]:
    print("Suggestions:")
    for s in result["feedback"]["suggestions"]:
        print("-", s)
