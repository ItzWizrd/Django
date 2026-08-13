import random
from decimal import Decimal
from django.contrib.auth.hashers import make_password
from django.core.management.base import BaseCommand
from django.db import transaction
from faker import Faker

from order.models import Order
from customer.models import Customer
from product.models import Category, Product
from suppliers.models import Supplier
from user.models import Role, User

CATEGORY_NAMES = [
    "Electronics", "Groceries", "Furniture", "Apparel", "Stationery",
    "Toys", "Beauty", "Automotive", "Sports", "Books",
    "Home Appliances", "Garden", "Pet Supplies", "Health", "Music",
]
ROLE_NAMES = ["Admin", "Manager", "Staff"]


class Command(BaseCommand):
    help = "Seed the database with fake data (roles, users, categories, products, suppliers, customers, orders)."

    def add_arguments(self, parser):
        parser.add_argument("--users", type=int, default=10)
        parser.add_argument("--categories", type=int, default=10)
        parser.add_argument("--products", type=int, default=20)
        parser.add_argument("--suppliers", type=int, default=8)
        parser.add_argument("--customers", type=int, default=15)
        parser.add_argument("--orders", type=int, default=10)
        parser.add_argument("--flush", action="store_true", help="Delete existing rows before seeding.")

    @transaction.atomic
    def handle(self, *args, **options):
        fake = Faker()

        if options["flush"]:
            Order.objects.all().delete()
            Product.objects.all().delete()
            Category.objects.all().delete()
            User.objects.all().delete()
            Role.objects.all().delete()
            Supplier.objects.all().delete()
            Customer.objects.all().delete()
            self.stdout.write(self.style.WARNING("Cleared existing seeded data."))

        roles = [Role.objects.get_or_create(name=name)[0] for name in ROLE_NAMES]

        users = self._seed_users(fake, options["users"], roles)
        categories = self._seed_categories(fake, options["categories"])
        products = self._seed_products(fake, options["products"], categories)
        suppliers = self._seed_suppliers(fake, options["suppliers"])
        customers = self._seed_customers(fake, options["customers"])
        orders = self._seed_orders(fake, options["orders"], customers, products)

        self.stdout.write(self.style.SUCCESS(
            f"Seeded {len(users)} users, {len(categories)} categories, {len(products)} products, "
            f"{len(suppliers)} suppliers, {len(customers)} customers, {len(orders)} orders."
        ))

    def _seed_users(self, fake, count, roles):
        created = []
        for _ in range(count):
            user, is_new = User.objects.get_or_create(
                email=fake.unique.email(),
                defaults={
                    "username": fake.user_name()[:100],
                    "phone_number": fake.phone_number()[:15],
                    "password": make_password("password123"),
                    "address": fake.address(),
                    "role": random.choice(roles),
                },
            )
            if is_new:
                created.append(user)
        return created

    def _seed_categories(self, fake, count):
        names = random.sample(CATEGORY_NAMES, k=min(count, len(CATEGORY_NAMES)))
        while len(names) < count:
            names.append(fake.unique.word().capitalize())
        created = []
        for name in names:
            category, _ = Category.objects.get_or_create(
                category_name=name, defaults={"description": fake.sentence()}
            )
            created.append(category)
        return created

    def _seed_products(self, fake, count, categories):
        categories = categories or list(Category.objects.all())
        created = []
        for _ in range(count):
            created.append(Product.objects.create(
                product_name=fake.unique.catch_phrase()[:100],
                description=fake.sentence(),
                price=Decimal(f"{random.uniform(5, 999):.2f}"),
                quantity=random.randint(1, 100),
            ))
        return created

    def _seed_suppliers(self, fake, count):
        created = []
        for _ in range(count):
            supplier, is_new = Supplier.objects.get_or_create(
                email=fake.unique.company_email(),
                defaults={
                    "name": fake.company(),
                    "phone_number": fake.phone_number()[:15],
                    "address": fake.address(),
                    "is_active": True,
                },
            )
            if is_new:
                created.append(supplier)
        return created

    def _seed_customers(self, fake, count):
        created = []
        for _ in range(count):
            customer, is_new = Customer.objects.get_or_create(
                email=fake.unique.email(),
                defaults={
                    "username": fake.user_name()[:100],
                    "phone_number": fake.phone_number()[:15],
                    "password": make_password("password123"),
                    "address": fake.address(),
                },
            )
            if is_new:
                created.append(customer)
        return created

    def _seed_orders(self, fake, count, customers, products):
        if not customers or not products:
            self.stdout.write(self.style.WARNING("Skipping orders: need at least one customer and one product."))
            return []
        statuses = [choice[0] for choice in Order.OrderStatus.choices]
        created = []
        for _ in range(count):
            order = Order.objects.create(
                customer=random.choice(customers),
                order_date=fake.date_this_year(),
                status=random.choice(statuses),
            )
            order.order_details.set(random.sample(products, k=min(len(products), random.randint(1, 4))))
            created.append(order)
        return created
