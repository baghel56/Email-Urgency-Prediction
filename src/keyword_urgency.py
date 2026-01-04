# keyword_urgency.py

def keyword_based_urgency(text):
    urgent_keywords = [
        "urgent",
        "immediately",
        "asap",
        "refund",
        "failed",
        "failure",
        "not working",
        "error",
        "payment failed",
        "deducted"
    ]

    text = text.lower()

    for word in urgent_keywords:
        if word in text:
            return "High"

    return "Low"

if __name__ == "__main__":
    test_text = "Payment failed urgently, please refund immediately"
    print(keyword_based_urgency(test_text))

