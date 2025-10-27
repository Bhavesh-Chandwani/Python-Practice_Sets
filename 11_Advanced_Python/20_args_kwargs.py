def process_orders(order_id, *items, **customer_details):
    print(f"Processing Order Id : {order_id} ")
    
    print(f"\n Items in order: ")
    for item in items:
        print(f"- {item}")
    
    print(f"\n Customer Details: ")
    for key, value  in customer_details.items():
        print(f"- {key} : {value}")
process_orders(101, "Mobile Phone", "Earphone", "Charger", 
             name="John Doe", delivery_address="123 Python Lane, Mumbai")