from flask import Flask
from src.view.controller.userController import UserController

app = Flask(__name__)

@app.route('/users', methods=['POST'])
def create_user():
    return UserController.createUser()

@app.route('/users', methods=['GET'])
def list_users():
    return UserController.listsUsers()
    

if __name__ == '__main__':
    app.run(debug=True)
