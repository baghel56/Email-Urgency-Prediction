from keyword_urgency import keyword_based_urgency

def hybrid_test():
    text = "Payment failed urgently, please refund immediately"
    result = keyword_based_urgency(text)
    print("Predicted urgency:", result)

if __name__ == "__main__":
    hybrid_test()



