from database.utilits.CRUD import CRUDInterface
from database.models.models import db, FilmsBase, User

def_insert_user = CRUDInterface.insert_single_user()
def_insert_data = CRUDInterface.insert_data()
def_get_elem = CRUDInterface.retrieve_elem()

if __name__ == '__main__':
    print('test')
