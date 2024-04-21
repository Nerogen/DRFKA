import django
from faker import Faker
from link_manager_project.link_manager.models import User, Link
from link_manager_project.link_manager_project import settings

django.setup()
fake = Faker()
settings.configure()

def create_users(num_users):
    for _ in range(num_users):
        email = fake.email()
        password = fake.password()
        registration_date = fake.date_time_between(start_date='-2y', end_date='now')
        User.objects.create(email=email, password=password, registration_date=registration_date)


def create_links(num_links_per_user):
    users = User.objects.all()
    for user in users:
        for _ in range(num_links_per_user):
            title = fake.text(max_nb_chars=50)
            description = fake.text(max_nb_chars=200)
            url = fake.url()
            image = fake.image_url()
            created_at = fake.date_time_between(start_date='-2y', end_date='now')
            Link.objects.create(user=user, title=title, description=description, url=url, image=image,
                                created_at=created_at)


def generate_test_data(num_users, num_links_per_user):
    create_users(num_users)
    create_links(num_links_per_user)


if __name__ == '__main__':
    num_users = 20
    num_links_per_user = 5
    generate_test_data(num_users, num_links_per_user)
    print(f'Test data generated: {num_users} users with {num_links_per_user} links each.')
