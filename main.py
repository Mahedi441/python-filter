from flask import Flask,render_template,request,redirect,url_for,session,jsonify
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils  import secure_filename
import os
import datetime
import json
import re
import random
import string
import math
local_server = True

with open('config.json','r') as c:
    params = json.load(c)["params"]

app = Flask(__name__) 
app.secret_key='mahedi441'  
app.config["Upload_location"] =  "C:\\Users\\Dell\\Desktop\\flsak\\static"
app.config["UPLOAD_FOLDER"] =  "C:\\Users\\Dell\\Desktop\\flsak\\static"

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost:3300/fashionkart?connect_timeout=10'
db = SQLAlchemy(app)
class Products(db.Model):
    # id , name ,Image,descriptionn,color,category,price
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=False)
    Image = db.Column(db.String(1000), unique=False)
    description = db.Column(db.String(80), unique=False)
    color = db.Column(db.String(15), unique=False)
    category = db.Column(db.String(20), unique=False)
    price = db.Column(db.Integer, unique=False)
    slug = db.Column(db.String(25), unique=True)
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "Image": self.Image,
            "description": self.description,
            "color": self.color,
            "category": self.category,
            "price": self.price,
            "slug": self.slug
        }
    
class Cart(db.Model):
    # id , name ,Image,descriptionn,color,category,price
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    productId = db.Column(db.String(10), primary_key=False)
    userId = db.Column(db.String(10),unique=False)

   
class User(db.Model):
    id = db.Column(db.String(20), primary_key=True)
    email = db.Column(db.String(25), unique=True)
    password = db.Column(db.String(25), unique=False)
    role =  db.Column(db.String(25), unique=False)

# import math  # Make sure to import math for the math.ceil function
@app.route("/", methods = ['GET','POST'])
def Home():
    u = False
    if 'user' in session:
        u = True
    else:
        u = False
    no_of_posts = 10
    # if 'user' in session:
    #     print(session['user'])
    #     sessionUser = session['user']
    #     # print(sessionUser)
    #     userData = User.query.filter_by(email=sessionUser).first()
    #     # print(userData.id)
    #     # print(userData.role)
    #     # print("User Role: ", userData.role)
    #     userRole = userData.role

    #     if userRole == "admin":  # Check user and role
    #         admin = True
    #         # print(admin )
    #     else:
    #         admin = False
            # print(admin )
            # Fetch all posts from Posts table
        # all_posts = Products.query.all()[0:params['no_of_posts']]  # Use a different variable name to avoid conflict
    all_posts = Products.query.all() # Use a different variable name to avoid conflict
    # last = math.ceil(len(all_posts)/no_of_posts)
    # print(last)
    # page =  request.args.get('page')
    # print(page)
    # if(not str(page).isnumeric()):
    #     page = 1
    # page = int(page)
    # print(page)
    # posts = all_posts[(page-1)*no_of_posts : (page-1)*no_of_posts + no_of_posts ]
    # print(posts)
    # if(page==1):
    #     prev = "#"
    #     next =  "/home?page="+str(page+1)
    # elif(page==last):
    #     prev =  "/home?page="+str(page-1)
    #     next = "#"
    # else:
    #     prev =  "/home?page="+str(page-1)
    #     next =  "/home?page="+str(page+1)
    sort_lh =  "/?sort="+str("Low to High")
    sort_hl =  "/?sort="+str("Hight to Low")
    sort_all =  "/?sort="+str("All")
    # sort_hl =  "/home?sort=High to Low"
    sort_option = request.args.get('sort',default="All")

    # Fetch all products
    

    # Sorting logic based on the sorting option from the client
    if sort_option == "Low to High":
        all_posts = sorted(all_posts, key=lambda x: x.price)
    elif sort_option == "High to Low":
        all_posts = sorted(all_posts, key=lambda x: x.price, reverse=True)
    

    unique_categories = db.session.query(Products.category).distinct().all()
    unique_color = db.session.query(Products.color).distinct().all()
    # for item in unique_categories:
    
        # print(item[0])
    # def btn():
        # print('succesfully btn clicked')
    return render_template('main_filter.html',Posts=all_posts,unique_categories=unique_categories,unique_color=unique_color,params=params,sort_lh=sort_lh,sort_hl=sort_hl,admin=admin,u=u)
    # else:
    #     return redirect(url_for('Signup'))

@app.route("/data", methods = ['GET','POST'])
def data():
    all_posts = Products.query.all()
    posts = [post.to_dict() for post in all_posts]
    return jsonify(posts)

@app.route("/cart", methods = ['GET','POST'])
def Cart_page():
    if 'user' in session:
           # Fetch all items added to the cart
        cart_items = Cart.query.all()
        sessionUser = session['user']
  
        userData = User.query.filter_by(email=sessionUser).first()
    
        userId = userData.id
        findId_items = Cart.query.filter_by(userId=userId).all()
        if not findId_items:
            # If there are no items in the cart
            # flash("Your cart is empty.", "info")
            return render_template('cart_filter.html', cart_items=[])
         # Fetch the corresponding product details for each cart item
        products_in_cart = []
        total_price = 0
        for cart_item in findId_items:
            product = Products.query.filter_by(id=cart_item.productId).first()
            if product:
                products_in_cart.append(product)

        for x in products_in_cart:
            print(x.price)
            total_price += x.price
                
        print('total_price')
        print(total_price)
        return render_template('cart_filter.html',cart_items=products_in_cart,total=total_price)
    else:
        return redirect(url_for('Signup'))

@app.route("/signup", methods = ['GET','POST'])
def Signup():
    if 'user' in session:
        # User already logged in, redirect to main_filter
        return redirect(url_for('Home'))
    
    if request.method == 'POST':
        em = request.form.get('email')
        con_pas = request.form.get('confirm password')
        pas = request.form.get('password')
        random_id = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
        print(random_id)

        def check_email(email):
                # Define the regex for validating an email
                email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
                
                # Use re.match() to check if the email matches the regex
                if re.match(email_regex, email):
                    return True
                else:
                    return False

# Test the function
        
        if check_email(em):
            print(f"'{em}' is a valid email address")
        else:
            print(f"'{em}' is not a valid email address")

        if pas == con_pas:
            print('password is acceptable')
        else:
            print('password is not acceptable')
        if check_email(em) and pas == con_pas:
           
            existing_user = User.query.all()
            
            # existing_code = User.query.filter_by(id=random_code).first()
                
            if random_id != existing_user :
                try:
                    # Insert the user into the database
                    ent = User(id=random_id,email=em,password=pas)

                    db.session.add(ent)
                    db.session.commit()

                    print('Signup successful!')
                    
                    session['user'] = em
                    return redirect(url_for('Home'))  # Redirect to login page after successful signup

                except Exception as ex:
                    # If there's an error during insertion, log the error
                    db.session.rollback()
                    print(f"Error during signup: {str(ex)}")
                    return "An error occurred during signup. Please try again."



    else:

        return render_template('signup.html')
    
    return render_template('signup.html')

@app.route("/dashboard", methods=['GET', 'POST'])
def Dashboard():
    if 'user' in session:
        # User already logged in, redirect to main_filter
        return redirect(url_for('Home'))
    if request.method == 'POST':
        # Get email, password, and remember me values from the form
        em = request.form.get('email')
        pas = request.form.get('password')

        # Print for debugging purposes
        print(f"Email: {em}, Password: {pas}")

        # Fetch the stored user by email
        data = User.query.filter_by(email=em).first()

        if data:
            # Print the stored password for debugging purposes
            print(f"Stored Email: {data.email}")
            print(f"Stored Password: {data.password}")

            # Check if the password matches
            if em == data.email and pas == data.password and data.role != "admin":
                  session['user'] = em
                  print("already exist!")
                  
                  return redirect(url_for('Home'))
                # Set up session or any logic for the admin after login
                # return render_template('main_filter.html', success=True)
            elif em == data.email and pas == data.password and data.role == "admin":
                    session['user'] = em
                    return redirect(url_for('admin'))
            else:
                  print("Please signup !")
                  return "Invalid password. Please try again.", 401
        else:
            print("User not found")
            return redirect(url_for('Signup'))

    # GET request, show the login form
    return render_template('login.html')

@app.route("/add_product", methods = ['GET','POST'])
def add_product():
    if 'user' in session:
        if(request.method=='POST'):
            name = request.form.get('name')
            # try:
            f = request.files['file']
            file = f.filename

            file_path = os.path.join(app.config["Upload_location"], secure_filename(f.filename))
            f.save(file_path)
            # except:
            #     return 'No select file'
            price = request.form.get('price')
            color = request.form.get('color')
            categories = request.form.get('categories')
            description = request.form.get('description')
            print(file)
            entry = Products(name=name, Image=file, description=description, color=color,
                            category=categories, price=price)
            db.session.add(entry)
            db.session.commit()
            return render_template('add_pro_filter.html', success=True)
        

        return render_template('add_pro_filter.html')
    else:
        return redirect(url_for('Signup'))

# ------------Filter Color------------
@app.route("/item/name/<string:item_name>", methods = ['GET'])
def name(item_name):
    
    find_name = Products.query.filter_by(name=item_name)
    if find_name is None:
        return "Item not found", 404 
   
    unique_categories = db.session.query(Products.category).distinct().all()
    unique_color = db.session.query(Products.color).distinct().all()
    return render_template('filter_category.html',Posts_name=find_name,unique_categories=unique_categories,unique_color=unique_color)

# ------------Filter Color------------
@app.route("/item/color/<string:item_color>", methods = ['GET'])
def color(item_color):
    
    find_color = Products.query.filter_by(color=item_color)
    if find_color is None:
        return "Item not found", 404 
    unique_categories = db.session.query(Products.category).distinct().all()
    unique_color = db.session.query(Products.color).distinct().all()
    return render_template('filter_category.html',Posts_color=find_color,unique_categories=unique_categories,unique_color=unique_color)

# ------------Filter Category------------
@app.route("/item/category/<string:item_category>", methods = ['GET'])
def category(item_category):
    find_category = Products.query.filter_by(category=item_category)
    if find_category is None:
        return "Item not found", 404 
    unique_categories = db.session.query(Products.category).distinct().all()
    unique_color = db.session.query(Products.color).distinct().all()
    return render_template('filter_category.html',Posts_c=find_category,unique_categories=unique_categories,unique_color=unique_color)

# -----------------items pages------------
@app.route("/item/<string:item_slug>", methods=['GET'])
def item(item_slug):


    find = Products.query.filter_by(slug=item_slug).first() # Fetch the first matching item
   
    if find is None:
        return "Item not found", 404  # Return a 404 error if the item is not found
    return render_template('item.html', item=find)  # Pass the item to the template

    # ---------------------add cart------------------------------------
@app.route("/item/add_cart/<string:item_slug>", methods=['GET'])
def Ad_cart(item_slug):
    if 'user' not in session:
        return redirect(url_for('Signup'))
    
    # Fetch the product using the slug
    find = Products.query.filter_by(slug=item_slug).first()  # Fetch the first matching item
    if find is None:
        return "Item not found", 404  # Return a 404 error if the item is not found
    
    sessionUser = session['user']
    userData = User.query.filter_by(email=sessionUser).first()
    userId = userData.id

    # Check if the product is already in the cart for the user
    existing_item_in_cart = Cart.query.filter_by(userId=userId, productId=find.id).first()

    if existing_item_in_cart:
        return 'Item is already added to the cart'
    
    # Generate a random two-digit number for id
    random_number = random.randint(10, 99)

    # Insert the new item into the cart
    cart_entry = Cart(id=random_number, productId=find.id, userId=userId)
    db.session.add(cart_entry)
    db.session.commit()

    print('Cart added successfully!')
    return redirect(url_for('Home'))

   


# # ---------------------------add cart-----------------
# @app.route("/item/add_cart/<string:item_slug>", methods=['GET'])
# def Ad_cart(item_slug):
    # Fetch the product using the slug
    find = Products.query.filter_by(slug=item_slug).first() # Fetch the first matching item
    sessionUser = session['user']
  
    userData = User.query.filter_by(email=sessionUser).first()
   
    userId = userData.id
    if find is None:
        return "Item not found", 404  # Return a 404 error if the item is not found
    else:
        print(find.id)
        # Check if the product already exists in the cart
        existing_item_in_cart = Cart.query.filter_by(productId=find.id).first()

        print(find.name)
        if existing_item_in_cart is None:
            cart_entry = Cart(productId=find.id,userId=userId)
            db.session.add(cart_entry)
            db.session.commit()
            print('cart added successfuly!')

         
            return redirect(url_for('Home'))
        else:
            return 'item is already added'

    return render_template('item.html', item=find)  # Pass the item to the template

# -----------------------Log out --------------------
@app.route("/logout")
def logout():
   if 'user' in session:
        session.pop('user', None)
    
   return redirect(url_for('Home'))
       
#    return redirect(url_for('Dashboard'))

# ================================Delete Data From DataBase=================================
@app.route('/cart/deleteData', methods=['POST'])
def cart_deleteData():
    data = request.get_json()
    sessionUser = session['user']
  
    userData = User.query.filter_by(email=sessionUser).first()
    userId = userData.id
  
    delId = data["delData"] 
    delData = Cart.query.filter_by(productId=delId).all()
  
    # Ensure you iterate through the list and delete matching items
    for x in delData:
        if x.userId == userId:
            db.session.delete(x)
            db.session.commit()

    return jsonify({"success": True, "message": "Item(s) deleted"})  # Return outside the loop


@app.route('/admin', methods=['GET','POST'])
def admin():
    u = False
    if 'user' in session:
            u = True
       
       
            return render_template('python_js2.html',u=u)
      
    else:
        return redirect('dashboard')
       

        

@app.route('/api/Products', methods=['GET','POST'])
def api_product():
   # Sample data to send as a response
    data = [
        {"id": 1, "name": "Item 1", "price": 10},
        {"id": 2, "name": "Item 2", "price": 20},
        {"id": 3, "name": "Item 3", "price": 30},
    ]
    data2 = Products.query.all()
    data3 =[product.to_dict() for product in data2]
    print(type(data))
    print(type(data2))
    return jsonify(data3) 

@app.route('/upload', methods=['POST'])
def upload():
    if 'file' not in request.files:
        # print(f)
        return jsonify({'error': 'No file part'}), 400
    print(request.files)

    f = request.files['file']
    print(f)

    if f.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    print(f.name)
    filename = secure_filename(f.filename)
    print(filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    # print(file_path)
    f.save(file_path)
    
    return jsonify({'message': 'File uploaded successfully', 'filename': filename})


@app.route('/api/add_data', methods=['POST'])
def api_add_data():
    
    data = request.get_json()   
    Image = data["add_data"]["Image"]
    random_id = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    print(random_id)
    id = random_id
    # id = data["add_data"]["id"]
    name = data["add_data"]["name"]
    color = data["add_data"]["color"]
    price = data["add_data"]["price"]
    slug = data["add_data"]["slug"]
    category = data["add_data"]["category"]
    description = data["add_data"]["description"]
    print(f"{id} {Image} {name} {color} {price} {slug} {category} {description}")
    entry = Products(id=id,Image=Image,name=name,color=color,price=price,slug=slug,category=category,description=description)
    db.session.add(entry)
    db.session.commit()
    # Print the data to check what keys are available
    print(f"Data received from JS: {data}")

    # Process other data as needed
    response = {"status": "Success", "message": f"Data received: {data}"}
    return jsonify("pass")


# ================================Receive-data==================
@app.route('/api/receive_data', methods=['POST'])
def receive_data():

    data = request.get_json()   
    random_id = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    print(random_id)
    id = random_id
    # id = data["inputData"]["id"]
    name = data["inputData"]["name"]
    color = data["inputData"]["color"]
    price = data["inputData"]["price"]
    slug = data["inputData"]["slug"]
    category = data["inputData"]["category"]
    description = data["inputData"]["description"]
    print(f"{id} {name} {color} {price} {slug} {category} {description}")
    
    # Print the data to check what keys are available
    print(f"Data received from JS: {data}")

    # Process other data as needed
    response = {"status": "Success", "message": f"Data received: {data}"}
    return jsonify("pass")

# ================================Delete Data From DataBase=================================
@app.route('/api/deleteData', methods=['POST'])
def deleteData():
    data = request.get_json()
    print(data)
    print(data["delData"])
    delId = data["delData"] 
    print(delId)
    delData = Products.query.filter_by(id=delId).first()
    print(delData)
    # delDataId = delData.id
    # print(delDataId)
    
    
    db.session.delete(delData)
    db.session.commit()
    # session.commit()
    return jsonify(data)
# ======================update data===============
@app.route('/api/updateData', methods=['POST'])
def updateData():
    
    data = request.get_json()   
    # Image = data["update_data"]["Image"]
    # random_id = ''.join(random.choices(string.ascii_letters + string.digits, k=4))
    # print(random_id)
    # id = random_id
    id = data["update_data"]["id"]
    name = data["update_data"]["name"]
    color = data["update_data"]["color"]
    price = data["update_data"]["price"]
    slug = data["update_data"]["slug"]
    category = data["update_data"]["category"]
    description = data["update_data"]["description"]

    product_to_update = Products.query.get(id)
    print(product_to_update)
    product_to_update.name = name
    product_to_update.color = color
    product_to_update.price = price
    product_to_update.slug = slug
    product_to_update.category = category
    product_to_update.description = description
    # product_to_update.Image = Image

    
    db.session.commit()
    # Print the data to check what keys are available
    print(f"Data received from JS: {data}")

    # Process other data as needed
    response = {"status": "Success", "message": f"Data received: {data}"}
    return jsonify("pass")
   




app.run(debug=True)
