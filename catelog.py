from flask import Flask, render_template
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CatalogItem

app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

@app.route('/')
def homepage():  
    categories = session.query(Category).all()
    return render_template('home.html', categories = categories)

# category related pages
@app.route('/category')
def listAllCategory():
    return render_template('allCategory.html')

@app.route('/category/new')
def createCategory():
    return render_template('newCategory.html')

@app.route('/category/<int:category_id>')
def showCategory(category_id):
    category = session.query(Category).filter_by(id = category_id).one()
    items = session.query(CatalogItem).filter_by(category_id = category_id)
    return render_template('showCategory.html', category = category, items = items)

@app.route('/category/<int:category_id>/edit')
def editCategory(category_id):
    return render_template('editCategory.html')

@app.route('/category/<int:category_id>/delete')
def deleteCategory(category_id):
    return render_template('deleteCategory.html')

# Item related pages
@app.route('/item/new')
def createItem():
    return render_template('newItem.html')

@app.route('/item/<int:item_id>/edit')
def editItem(item_id):
    return render_template('editItem.html')

@app.route('/item/<int:item_id>/delete')
def deleteItem(item_id):
    return render_template('deleteItem.html')



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)    