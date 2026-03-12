import pandas as pd

from processor_regex import classify_with_regex
from processor_llm import classify_with_llm
from processor_bert import classify_with_bert

def classify(logs):
    labels= []
    for source, log_msgs in logs:
        label = classify_log_message(source, log_msgs)
        labels.append(label)
    return labels




def classify_log_message(source, log_message):
    if source == 'LegacyCRM':
        label = classify_with_llm(log_message)
    
    else:
        label = classify_with_regex(log_message)
        if label is None:
            label = classify_with_bert(log_message)
    return label

def classify_csv(input_file):
    df = pd.read_csv(input_file)
    df['target_label'] = classify(list(zip(df['source'], df['log_message'])))

    # log = df[['source', 'log_message']].values.tolist()

    output_file = "Classification_project/resources/output.csv"
    df.to_csv(output_file, index=False)


if __name__ == "__main__":
    classify_csv("Classification_project/resources/test.csv")
    
    
    
    
    # log_messages = [
    #     ("BillingSystem", "User User123 logged in."),
    #     ("ModernCRM", "IP address 192.168.133.114 bloked due to potential attack."),
    #     ("AnalyticalEngine", "File data_6957.csv uploaded successfully by user User265"),
    #     ("AnalyticalEngine", "Backup completed successfully."),
    #     ("ModernHR", "GET /v2/54fab8e-9c1a-4c3e-8f2b-7d5e6f8a9b0c/servers/details HTTP/1.1 RCODE 200 len: 1583 time: 0.1287"),
    #     ("ModernHR", "Admin access escalation detected fpr user 9429"),
    #     ("LegacyCRM", "Case escalation for ticket ID 98765 failed because the assigned agent is no longer active."),
    #     ("LegacyCRM", "Invoice generation process aborted for order ID 8910 due to invalid tax calculation module."),
    #     ("LegacyCRM", "The 'BulkEmailSender' feature is no longer supported. Use 'EmailCampaignManager' for improved functionality.")
    # ]


    # classified_logs = classify(log_messages)
    # print(classified_logs)