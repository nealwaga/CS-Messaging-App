import csv
from datetime import datetime
from django.utils.timezone import make_aware

from messaging.models.messages import Customers, Chats, Messages
from messaging.management.commons import bcolors


csv_file_path = 'customer_data.csv'

customers = {}
chats = {}

with open(csv_file_path, 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    for row in csv_reader:
        user_id = row['User ID']

        if user_id not in customers:
            # Create new customers
            customer = Customers(full_name=f"Customer {user_id}")
            customer.save()
            customers[user_id] = customer

            # Create new chats
            chat = Chats(sender=customer)
            chat.save()
            chats[user_id] = chat

        # Create a new Messages instance
        timestamp = make_aware(datetime.strptime(row['Timestamp (UTC)'], '%Y-%m-%d %H:%M:%S'))
        message = Messages(
            sender_type='customer',
            sender=customers[user_id],
            chat=chats[user_id],
            message_body=row['Message Body'],
            timestamp=timestamp
        )
        message.save()

print(f"{bcolors.OKGREEN} ✓ DONE! SAVED ALL DATA!{bcolors.ENDC}")