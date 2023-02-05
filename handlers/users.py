import tornado.web

import model.users as usersModel


class Users(tornado.web.RequestHandler):
    def get(self, userID):
        self.write(f"Hello World --> , Id: {userID}")

        # db = Connect(dbParams)
        # user = usersModel.getUser (userID)