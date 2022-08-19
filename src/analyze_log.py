import csv
from collections import Counter


def csv_reader(path: str) -> list:
    if 'csv' not in path:
        raise FileNotFoundError(f"Extensão inválida: '{path}'")
    try:
        with open(path, encoding='utf-8') as file:
            restaurant_logs = csv.reader(file)
            logs_list = []
            for log in restaurant_logs:
                logs_list.append(log)
        return logs_list
    except FileNotFoundError:
        raise FileNotFoundError(f"Arquivo inexistente: '{path}'")


def get_client_orders_by_name(client: str, orders: list) -> list:
    return [order[1] for order in orders if order[0] == client]


def get_client_most_commom_order(client: str, orders: list):
    client_orders = get_client_orders_by_name(client, orders)
    most_commom = Counter(client_orders).most_common()[0][0]
    return most_commom


def client_meal_counter(client: str, orders: list, meal: str) -> int:
    client_orders = get_client_orders_by_name(client, orders)
    meal_counter = [order for order in client_orders if order == meal]
    return len(meal_counter)


def client_never_ordered_meals(client: str, orders: list) -> dict:
    dict_orders = {order[1] for order in orders}
    client_orders = get_client_orders_by_name(client, orders)
    unique_orders = set(client_orders)
    return dict_orders.difference(unique_orders)


def client_never_gone_days(client: str, orders: list) -> dict:
    week_days_dict = {day[2] for day in orders}
    client_days = [day[2] for day in orders if day[0] == client]
    unique_days = set(client_days)
    return week_days_dict.difference(unique_days)


def analyze_log(path_to_file):
    orders = csv_reader(path_to_file)
    with open('data/mkt_campaign.txt', 'w') as file:
        file.write(
            f'{get_client_most_commom_order("maria", orders)}\n'
            f'{client_meal_counter("arnaldo", orders, "hamburguer")}\n'
            f'{client_never_ordered_meals("joao", orders)}\n'
            f'{client_never_gone_days("joao", orders)}\n'
        )
