from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('home.html')

# category related pages
@app.route('/category')
def list_category():
    return render_template('allCategory.html')

@app.route('/category/new')
def create_category():
    return render_template('newCategory.html')

@app.route('/category/<int:id>/edit')
def edit_category():
    return render_template('editCategory.html')

@app.route('/category/<int:id>/delete')
def delete_category():
    return render_template('deleteCategory.html')

# Item related pages
@app.route('/item/new')
def create_item():
    return render_template('newItem.html')

@app.route('/item/<int:id>/edit')
def edit_item():
    return render_template('editItem.html')

@app.route('/item/<int:id>/delete')
def delete_item():
    return render_template('deleteItem.html')



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)    