class KitchenOrderQueue:
    def __init__(self):
        self.queue = []
    
    def is_empty(self):
        return len(self.queue) == 0

    def add_order(self, order):
        self.queue.append(order)

    def pop_order(self):
        if not self.is_empty():
            return self.queue.pop(0)
        else:
            raise IndexError('Cannot remove from queue with no orders')
        

kitchen_queue = KitchenOrderQueue()
kitchen_queue.add_order("Burger")
kitchen_queue.add_order("Pizza")

print(kitchen_queue.pop_order())

class CustomerOrderQueue:
    def __init__(self):
        self.queue = []

    def add_order(self, order, priority):
        self.queue.append((order, priority))
        self.queue.sort(key=lambda x: x[1])

    def process_order(self):
        if self.queue:
            return self.queue.pop(0)[0]
        else:
            return "No orders to process."
        
    def notify_customer(self, order):
        print(f"Order {order} is ready for pickup/delivery.")

customer_queue = CustomerOrderQueue()
customer_queue.add_order("Bamiya", 2)
customer_queue.add_order("Mansaf", 1)

while customer_queue.queue:
    processed_order = customer_queue.process_order()
    customer_queue.notify_customer(processed_order)

print(customer_queue.process_order())
