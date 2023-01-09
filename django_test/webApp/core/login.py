
from webApp.models import Administrators


def post_login(login_data):
        name = login_data["name"]
        password = login_data['password']
        user = Administrators.objects.filter(name=name).filter(password=password).first()
        return user

def post_admin(id):
        user = Administrators.objects.filter(id=id).first()
        return user