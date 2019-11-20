from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CatalogItem

app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

# Home page, list all categories and newest items [done]
@app.route('/')
def homepage():  
    categories = session.query(Category).all()
    return render_template('home.html', categories = categories)

# List all categories, redirect to new/edit/delete category [done]
@app.route('/category')
def listAllCategory():
    categories = session.query(Category).all()
    return render_template('allCategory.html', categories = categories)
# Create new category [done]
@app.route('/category/new', methods=['GET','POST'])
def createCategory():
    if(request.method == 'POST'):
        newCategory = Category(name=request.form['name'])
        session.add(newCategory)
        session.commit()
        return redirect(url_for('listAllCategory'))
    else:
        return render_template('newCategory.html')

# List all items in a certain category, redirect to edit/delete/new item [done]
@app.route('/category/<int:category_id>')
def showCategory(category_id):
    category = session.query(Category).filter_by(id = category_id).one()
    items = session.query(CatalogItem).filter_by(category_id = category_id)
    return render_template('showCategory.html', category = category, items = items)

# [new] edit category
@app.route('/category/<int:category_id>/edit')
def editCategory(category_id):
    return render_template('editCategory.html')

# [new] delete category
@app.route('/category/<int:category_id>/delete', methods=['GET','POST'])
def deleteCategory(category_id):
    categoryToDelete=session.query(Category).filter_by(id=category_id).one()
    if(request.method=='POST'):
        session.delete(categoryToDelete)
        session.commit()
        return redirect(url_for('listAllCategory'))
    else:
        return render_template('deleteCategory.html', category=categoryToDelete)

# Add new item in a certain category [done]
@app.route('/category/<int:category_id>/new', methods=['GET','POST'])
def createItem(category_id):
    if(request.method == 'POST'):
        newItem = CatalogItem(name=request.form['name'], category_id=category_id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('showCategory', category_id=category_id))
    else:
        return render_template("newItem.html", category_id=category_id)

# [new] edit item
@app.route('/item/<int:item_id>/edit')
def editItem(item_id):
    return render_template('editItem.html')

# [new] delete item
@app.route('/item/<int:item_id>/delete', methods=['GET','POST'])
def deleteItem(item_id):
    itemToDelete=session.query(CatalogItem).filter_by(id=item_id).one()
    if(request.method=='POST'):
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('listAllCategory'))
    else:
        return render_template('deleteItem.html',item=itemToDelete)

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)    