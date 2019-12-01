from flask import Flask, render_template, request, redirect, url_for
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, CatalogItem

app = Flask(__name__)

engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()

# Home page
# List all categories and newest items [done]
@app.route('/')
def homepage():  
    categories = session.query(Category).all()
    return render_template('home.html', categories = categories)

# Category landing page:
# List all items in a certain category, redirect to edit/delete/new item [done]
@app.route('/<category_name>/')
def showCategory(category_name):
    category = session.query(Category).filter_by(name = category_name).one()    
    items = session.query(CatalogItem).filter_by(category_id = category.id)
    return render_template('categoryLandingPage.html', category = category, items = items)

# New category page 
@app.route('/new_category/', methods=['GET','POST'])
def createCategory():
    if(request.method == 'POST'):
        newCategory = Category(name=request.form['name'])
        session.add(newCategory)
        session.commit()
        return redirect(url_for('homepage'))
    else:
        return render_template('newCategory.html')

# Edit category page 
@app.route('/<category_name>/edit/', methods=['GET','POST'])
def editCategory(category_name):
    categoryToEdit=session.query(Category).filter_by(name=category_name).one()
    if(request.method=='POST'):
        categoryToEdit.name = request.form['name']
        session.add(categoryToEdit)
        session.commit()
        return redirect(url_for('homepage'))
    else:    
        return render_template('editCategory.html', category=categoryToEdit)

# Delete category page [done]
@app.route('/<category_name>/delete/', methods=['GET','POST'])
def deleteCategory(category_id):
    categoryToDelete=session.query(Category).filter_by(name=category_name).one()
    if(request.method=='POST'):
        session.delete(categoryToDelete)
        session.commit()
        return redirect(url_for('homepage'))
    else:
        return render_template('deleteCategory.html', category=categoryToDelete)

# Item landing page:
# List detail of an item
@app.route('/<category_name>/<item_name>')
def showItem(category_name, item_name):
    category = session.query(Category).filter_by(name = category_name).one()
    item = session.query(CatalogItem).filter_by(name = item_name).one()
    return render_template('itemLandingPage.html', item = item)

# New item page
@app.route('/<category_name>/new_item/', methods=['GET','POST'])
def createItem(category_name):
    if(request.method == 'POST'):
        category = session.query(Category).filter_by(name = category_name).one()
        newItem = CatalogItem(name=request.form['name'], category_id=category.id)
        session.add(newItem)
        session.commit()
        return redirect(url_for('showCategory', category_id=category.id))
    else:
        return render_template("newItem.html", category_id=category.id)

# Edit item page
@app.route('/<category_name>/<item_name>/edit/', methods = ['POST', 'GET'])
def editItem(category_name, item_name):
    category = session.query(Category).filter_by(name = category_name).one()
    itemToEdit = session.query(CatalogItem).filter_by(name = item_name).one()
    if(request.method == 'POST'):        
        return redirect(url_for('homepage'))
    else:
        return render_template('editItem.html', item =itemToEdit)

# Delete item page
@app.route('/<category_name>/<item_name>/delete/', methods=['GET','POST'])
def deleteItem(category_name, item_name):
    itemToDelete = session.query(CatalogItem).filter_by(name = item_name).one()
    if(request.method=='POST'):
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('homepage'))
    else:
        return render_template('deleteItem.html',item=itemToDelete)

# Login page

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)    