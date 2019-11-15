from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Home page!! Show list of categories and the most recent items.'


# category related pages
@app.route('/category')
def list_category():
    return 'List all categories here.'

@app.route('/category/new')
def create_category():
    return 'Create a new category here.'

@app.route('/category/<int:id>/edit')
def edit_category():
    return 'Edit a category here.'

@app.route('/category/<int:id>/delete')
def delete_category():
    return 'Delete a category here.'    

# Item related pages
@app.route('/item/new')
def create_item():
    return 'Create a new item here.'

@app.route('/item/<int:id>/edit')
def edit_item():
    return 'Edit an item here.'

@app.route('/item/<int:id>/delete')
def delete_item():
    return 'Delete an item here.'



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)    