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
def listCategory():
    return render_template('allCategory.html')

@app.route('/category/new')
def createCategory():
    return render_template('newCategory.html')

@app.route('/category/<int:id>/edit')
def editCategory():
    return render_template('editCategory.html')

@app.route('/category/<int:id>/delete')
def deleteCategory():
    return render_template('deleteCategory.html')

# Item related pages
@app.route('/item/new')
def createItem():
    return render_template('newItem.html')

@app.route('/item/<int:id>/edit')
def editItem():
    return render_template('editItem.html')

@app.route('/item/<int:id>/delete')
def deleteItem():
    return render_template('deleteItem.html')



if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)    