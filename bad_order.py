def process_order_bad():
    error = "SUCCESS"

    if validate_customer():
        if check_inventory():
            if process_payment():
                if update_inventory():
                    if send_confirmation():
                        print("Order processed successfully!")
                    else:
                        error = "CONFIRMATION_FAILED"
                else:
                    error = "INVENTORY_UPDATE_FAILED"
            else:
                error = "PAYMENT_FAILED"
        else:
            error = "INVENTORY_CHECK_FAILED"
    else:
        error = "CUSTOMER_VALIDATION_FAILED"

    return error

def validate_customer():
    return True  

def check_inventory():
    return True

def process_payment():
    return True

def update_inventory():
    return True

def send_confirmation():
    return True

def rollback_payment():
    print("Rolling back payment...")

def rollback_inventory():
    print("Rolling back inventory changes...")