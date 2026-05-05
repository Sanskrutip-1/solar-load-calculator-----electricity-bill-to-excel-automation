import re

def extract_bill_data(text):

    data = {}

    # Units Consumed
    units = re.findall(r'\b\d{2,4}\b', text)
    data['units'] = int(units[0]) if units else 0

    # Load (kW)
    load = re.search(r'(\d+\.?\d*)\s?KW', text)
    data['load'] = float(load.group(1)) if load else 0

    # Amount
    amount = re.search(r'Rs\.?\s?(\d+)', text)
    data['amount'] = int(amount.group(1)) if amount else 0

    return data