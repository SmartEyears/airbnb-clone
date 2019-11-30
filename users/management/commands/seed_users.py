from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):

    help = "이 명령어는 가상 데이터 User를 만들어 주는 명령어 입니다."

    def add_arguments(self, parser):
        parser.add_argument("--number", default=1, type=int, help="몇명이나 생성하시겠습니까?")

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number}명의 User가 생성되었습니다!"))
