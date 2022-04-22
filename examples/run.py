import sqlcrud

import connection
import models
import schemas


def main():
    class User(sqlcrud.CrudBase[models.User, schemas.UserCreate, schemas.UserUpdate]):
        def __init__(self):
            sqlcrud.CrudBase.__init__(self, model=models.User, engine=connection.engine)

    user = User()
    # Create user
    # create_user_data = schemas.UserCreate(name="Johan", password="password")
    # user.create(model=create_user_data)

    # List all users
    # print("\n All users \n", user.all())

    # Find a user by its primary key
    # one_user = user.find(primaryKey=1)
    # print("\n Found by id \n", one_user)

    # Update a user that already exist in the database.
    # update_me = schemas.UserUpdate(name="Hejkkhej")
    # user.update(model=one_user, data=update_me)
    # print(one_user)

    # Find a one user by a matching value in a column.
    # new_one_user = user.findBy(column="name", value="Hejkkhej")
    # print("\n FIND ONE BY \n", new_one_user)

    # Find many users by a matching value in a column.
    # new_many_users = user.findBy(column="name", value="Johan")
    # print("\n FOUND MANY BY \n", new_many_users)

    # Delete user from database.
    # user.delete(model=user.find(primaryKey=1))

    # users = user.all()
    # print(users)
    # user.deleteMany(models=users)
    # print("delete delete")
    # print(user.all())


if __name__ == "__main__":
    main()
