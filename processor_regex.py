import re

def classify_with_regex(log_message):
    regex_patterns = {
        r"User User\d+ logged (out|in).": "User Action",
        r"Backup (started|ended) at.*": "System Notification",
        r"Backup completed successfully.": "System Notification",
        r"System updated to version  .*" : "System Notification",
        r"File .* uploaded successfully by user .*": "System Notification",
        r"Disk cleanup completed successfully.": "System Notification",
        r"system reboot initiated by user .*": "System Notification",
        r"Account with ID .* created by .*": "User Action"
    }
    for pattern, label in regex_patterns.items():
        if re.match(pattern, log_message, flags=re.IGNORECASE):
            return label
    return None

if __name__ == "__main__":
    print(classify_with_regex("User User123 logged in."))
    print(classify_with_regex("Backup started at 2024-06-01 10:00:00."))
    print(classify_with_regex("System updated to version 1.2.3"))
    print(classify_with_regex("File report.pdf uploaded successfully by user User456"))
    print(classify_with_regex("Disk cleanup completed successfully."))
    print(classify_with_regex("system reboot initiated by user User789"))
    print(classify_with_regex("Account with ID 12345 created by UserAdmin"))
    print(classify_with_regex("Unrecognized log message."))