from database.utilits.CRUD import CRUDInterface

def_insert_user = CRUDInterface.insert_single_user()
def_insert_data = CRUDInterface.insert_data()
def_get_elem = CRUDInterface.retrieve_elem()
def_del_old_elem = CRUDInterface.del_olf_el()

if __name__ == '__main__':
    print('test')
