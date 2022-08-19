from collections import Counter


class TrackOrders:
    def __init__(self) -> None:
        self.orders = []

    def __len__(self):
        return len(self.orders)

    def add_new_order(self, customer, order, day):
        self.orders.append({"customer": customer, "order": order, "day": day})

    def get_filtered_elements(self, filter):
        return [element[filter] for element in self.orders]

    def get_client_record(self, client, filter):
        return [el[filter] for el in self.orders if el['customer'] == client]

    def get_most_ordered_dish_per_customer(self, customer):
        orders = self.get_client_record(customer, 'order')
        most_commom = Counter(orders).most_common()[0][0]
        return most_commom

    def get_never_ordered_per_customer(self, customer):
        orders = {order['order'] for order in self.orders}
        client_orders = self.get_client_record(customer, 'order')
        return orders.difference(client_orders)

    def get_days_never_visited_per_customer(self, customer):
        week_days_dict = {order['day'] for order in self.orders}
        client_days = self.get_client_record(customer, 'day')
        unique_days = set(client_days)
        return week_days_dict.difference(unique_days)

    def get_busiest_day(self):
        days = self.get_filtered_elements('day')
        busiest_day = Counter(days).most_common()[0][0]
        return busiest_day

    def get_least_busy_day(self):
        days = self.get_filtered_elements('day')
        least_busy_day = Counter(days).most_common()[-1][0]
        return least_busy_day
