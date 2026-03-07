from cron_descriptor import get_description

if __name__ == "__main__":
    print(get_description("0 9 * * 1-5"))  # ➞ "At 9:00 AM, Monday through Friday"
    print(get_description("0 0 * * *"))    # ➞ "At 12:00 AM"
    print(get_description("0 12 * * MON")) # ➞ "At 12:00 PM, only on Monday"