from flask import Flask, render_template, request,jsonify, json
import re
import pandas as pd

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route("/")
def home():
    return render_template('index_1.html')  ##login/signup only

@app.route("/index.html")
def home_return():
    return render_template('index.html')

USER_NAME = "Tanmay@gmail.com"
USER_MAIL = "Chu123"

@app.route("/login.html",  methods=['POST' , 'GET'])
def login():
    if request.method == 'POST' and 'email' in request.form and 'password' in request.form:
        email = request.form['email']
        password = request.form['password']
        if email == USER_NAME and password == USER_MAIL:
            reg = "You have successfully registered !!"
            return render_template('index.html', reg = reg)
        elif not re.fullmatch(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', email):
            err = "Invalid Email Address !!"
            return render_template('login.html' , err = err)
        elif not email or not password:
            err = "Please fill out all the fields"
            return render_template('login.html' , err = err)
    else:
        return render_template('login.html')

@app.route("/Signup.html")
def signup():
    if request.method == 'POST' and 'name' in request.form and 'email' in request.form and 'password' in request.form:
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        csv_data = [name, email, password]

        df = pd.DataFrame(columns=['Name', 'Email', 'Password'])
        df.loc[len(df)] = csv_data

        df.to_csv("User_Data.csv", mode='a', index=False, header=False)
        return render_template('index.html')
    else:
        return render_template('Signup.html')

@app.route("/about.html")
def about():
    return render_template('about.html')

@app.route("/contact.html")
def contact():
    return render_template('contact.html')

@app.route("/cart.html")
def cart():
    return render_template('cart.html')

@app.route("/thankyou.html")
def thankyou():
    return render_template('thankyou.html')

@app.route("/GirlsFashion.html")
def girlfashion():
    return render_template('GirlsFashion.html')

@app.route("/Grocery.html")
def grocery():
    return render_template('Grocery.html')

@app.route("/BoysFashion.html")
def boyfashion():
    return render_template('BoysFashion.html')

@app.route("/Fruits.html")
def fruits():
    return render_template('Fruits.html')



# Json list
# ---------Boys--------------

boysfashion_list = [
    {
        "id": 40,
        "title": "Chinos",
        "type": "boysfashihon",
        "imgpath": "https://img.freepik.com/free-photo/man-wearing-brown-pants-close-up_53876-102239.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 1500,
        "Rating": 4
    },
    {
        "id": 41,
        "title": "Cargo Pants",
        "type": "boysfashihon",
        "imgpath": "https://img.freepik.com/free-photo/pants-hanger-with-green-background_23-2150264165.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 1000,
        "Rating": 3
    },
    {
        "id": 42,
        "title": "Jeans",
        "type": "boysfashihon",
        "imgpath": "https://img.freepik.com/free-photo/fast-fashion-vs-slow-sustainable-fashion_23-2149133969.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 800,
        "Rating": 3.5
    },
    {
        "id": 43,
        "title": "Formal Pants",
        "type": "boysfashihon",
        "imgpath": "https://img.freepik.com/free-photo/business-african-american-happy-man_1303-2179.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 2000,
        "Rating": 4.5
    },
    {
        "id": 44,
        "title": "Shirts",
        "type": "boysfashihon",
        "imgpath": "https://img.freepik.com/free-photo/still-life-with-classic-shirts-hanger_23-2150828622.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 999,
        "Rating": 3
    },
    {
        "id": 45,
        "title": "Formal Shirts",
        "type": "boysfashihon",
        "imgpath": "https://img.freepik.com/free-photo/vertical-shot-concentrated-businessman-listening-carefully-with-crossed-hands_181624-29443.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 1299,
        "Rating": 3.5
    },
    {
        "id": 46,
        "title": "Cargo Shirts",
        "type": "boysfashihon",
        "imgpath": "https://img.freepik.com/free-photo/hands-holding-shirt-second-hand-market_23-2149338414.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 1400,
        "Rating": 4.5
    },
    {
        "id": 47,
        "title": "Printed Shirts",
        "type": "boysfashihon",
        "imgpath": "https://img.freepik.com/free-photo/clothing-rack-with-floral-hawaiian-shirts-hangers-hat_23-2149366019.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 1150,
        "Rating": 2.5
    },
    {
        "id": 48,
        "title": "Tshirts",
        "type": "boysfashihon",
        "imgpath": "https://img.freepik.com/free-photo/shirt-mockup-concept-with-plain-clothing_23-2149448748.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 650,
        "Rating": 2.5
    },
    {
        "id": 49,
        "title": "Baggy Tshirts",
        "type": "boysfashihon",
        "imgpath": "https://img.freepik.com/free-photo/portrait-handsome-asian-man-posing-outdoors-city-with-headphones_23-2149086958.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 800,
        "Rating": 3
    },
    {
        "id": 50,
        "title": "Polo Tshirts",
        "type": "boysfashihon",
        "imgpath": "https://img.freepik.com/free-photo/man-wearing-blank-shirt_23-2149347508.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 800,
        "Rating": 3.5
    },
    {
        "id": 51,
        "title": "Hoodies",
        "type": "boysfashihon",
        "imgpath": "https://img.freepik.com/free-photo/men-s-apparel-hoodie-rear-view_53876-97228.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 1350,
        "Rating": 4.5
    }   
]
# -------Boys End-----------

# main function of boy
@app.route('/boysfashion', methods=['GET', 'POST'])
def boysfashion():
    if request.method == 'GET':
        if len(boysfashion_list) > 0:
            return jsonify(boysfashion_list)
        else:
            'Nothing Found', 404
        
    if request.method == 'POST':
        new_title = request.form['title']
        iD = boysfashion_list[-1]['id']+1

        new_obj = {
            'id': iD,
            'title': new_title
        }
        boysfashion_list.append(new_obj)
        return jsonify(boysfashion_list), 201

# main function of boy end
    
# ---------Girls--------------
girlsfashion_list = [
    {
        "id": 52,
        "title": "Jeans",
        "type": "girlsfashihon",
        "imgpath": "https://img.freepik.com/free-photo/young-woman-posing-street_1303-31808.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 999,
        "Rating": 3
    },
    {
        "id": 53,
        "title": "Trouser Pants",
        "type": "girlsfashihon",
        "imgpath": "https://img.freepik.com/free-photo/girl-town_1157-7261.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 1250,
        "Rating": 3.5
    },
    {
        "id": 54,
        "title": "Skirts",
        "type": "girlsfashihon",
        "imgpath": "https://img.freepik.com/free-photo/smiling-beautiful-elegant-woman-posing-camera_259150-58979.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 999,
        "Rating": 3.5
    },
    {
        "id": 55,
        "title": "Shots",
        "type": "girlsfashihon",
        "imgpath": "https://img.freepik.com/free-photo/stylish-girl_1157-8856.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 850,
        "Rating": 4.5
    },
    {
        "id": 56,
        "title": "Satin Top",
        "type": "girlsfashihon",
        "imgpath": "https://img.freepik.com/free-photo/fashion-portrait-young-elegant-woman_1328-2615.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 650,
        "Rating": 3.5
    },
    {
        "id": 57,
        "title": "Puffed Sleve Top",
        "type": "girlsfashihon",
        "imgpath": "https://img.freepik.com/free-photo/teen-girl-portrait-close-up_23-2149231203.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 550,
        "Rating": 3
    },
    {
        "id": 58,
        "title": "Crop Top",
        "type": "girlsfashihon",
        "imgpath": "https://img.freepik.com/free-photo/front-view-smiley-woman-posing-outdoors_23-2150360974.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 600,
        "Rating": 3
    },
    {
        "id": 59,
        "title": "Tank Top",
        "type": "girlsfashihon",
        "imgpath": "https://img.freepik.com/free-photo/blonde-young-girl-amusement-park_23-2147919070.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 700,
        "Rating": 3.5
    },
    {
        "id": 60,
        "title": "Kurti",
        "type": "girlsfashihon",
        "imgpath": "https://img.freepik.com/premium-photo/cute-girl-standing-house-lawn-wearing-desi-dress-fashion-photoshoot_658768-283.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 999,
        "Rating": 4
    },
    {
        "id": 61,
        "title": "Saree",
        "type": "girlsfashihon",
        "imgpath": "https://img.freepik.com/premium-photo/beautiful-girl-saree_872233-111.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 2500,
        "Rating": 4.5
    },
    {
        "id": 62,
        "title": "Flared Dress",
        "type": "girlsfashihon",
        "imgpath": "https://img.freepik.com/free-photo/elegant-pretty-woman-wearing-fashionable-trendy-blue-maxi-dress-posing-city-park_291049-197.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 2300,
        "Rating": 4
    },
    {
        "id": 63,
        "title": "One Piece",
        "type": "girlsfashihon",
        "imgpath": "https://img.freepik.com/free-photo/portrait-asian-woman-yellow-summer-dress-stands-with-plumeria-thai-flower-hair-round-earrings_343596-2131.jpg?w=360&t=st=1707487973~exp=1707488573~hmac=fff3969f568ee4bff32932006dbaf6b141bf98a10f3dd57d2d3d8f5f3d625dbb",
        "price": 1500,
        "Rating": 4.5
    }
]
# ------Girls End ------------

#main function girl start
@app.route('/girlsfashion', methods=['GET', 'POST'])
def girlsfashion():
    if request.method == 'GET':
        if len(girlsfashion_list) > 0:
            return jsonify(girlsfashion_list)
        else:
            'Nothing Found', 404
        
    if request.method == 'POST':
        new_title = request.form['title']
        iD = girlsfashion_list[-1]['id']+1

        new_obj = {
            'id': iD,
            'title': new_title
        }
        girlsfashion_list.append(new_obj)
        return jsonify(girlsfashion_list), 201
    
#main function girl end
    
#----- grocery list start --------
grocery_list = [
    {
        "id": 0,
        "title": "Raisins (Kala Manuka)",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/free-photo/raisins-dried_1368-9146.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 200,
        "Rating": 4.5
    },
    {
        "id": 1,
        "title": "Dried Grapes (Kismis)",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/free-photo/raisin-currant_1339-7227.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 200,
        "Rating": 4.5
    },
    {
        "id": 2,
        "title": "Semolina (Rava)",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/free-photo/stashed-flour-used-cooking_23-2149517215.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 47,
        "Rating": 4
    },
    {
        "id": 3,
        "title": "Dates (Kharik)",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/free-photo/yellow-dry-dates-isolated-wooden-platter_114579-25180.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 380,
        "Rating": 3.5
    },
    {
        "id": 4,
        "title": "Wheat Flour (Maida)",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/free-photo/ingredient-bag-full-flour_23-2149482594.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 30,
        "Rating": 2.5
    },
    {
        "id": 5,
        "title": "GroundNut Oil",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/free-photo/macadamia-oil-relaxing-treatment_1150-42742.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 230,
        "Rating": 3
    },
    {
        "id": 6,
        "title": "Tata Salt",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/free-photo/spoon-heap-salt-table_144627-11035.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 23,
        "Rating": 4
    },
    {
        "id": 7,
        "title": "Sabudana",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/premium-photo/sago-sabudana-served-bowl-as-pile-with-wooden-spoon-moody-background-selective-focus_466689-58062.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 94,
        "Rating": 4.5 
    },
    {
        "id": 8,
        "title": "Bengal Dal (Futana)",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/free-photo/top-view-raw-orange-lentil-inside-round-pot-with-wooden-spoon-dark-blue-surface_140725-49142.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 45,
        "Rating": 2
    },
    {
        "id": 9,
        "title": "Black Gram Dal(Urad)",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/premium-photo/husked-brown-gram-pulse_57665-3782.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 76,
        "Rating": 2.5
    },
    {
        "id": 10,
        "title": "Rajma",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/free-photo/red-kidney-beans-small-wooden-plate-place-sack-fabric_1150-35295.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 99,
        "Rating": 3.5
    },
    {
        "id": 11,
        "title": "Green Beans(Moong)",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/free-photo/green-mung-beans_74190-7161.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 70,
        "Rating": 4.5
    },
    {
        "id": 12,
        "title": "Ground Nuts",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/free-photo/food-white-background_1417-1653.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 162,
        "Rating": 3
    },
    {
        "id": 13,
        "title": "Dried Peas (Vatana)",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/premium-photo/green-peas-wooden-plate-wooden-background-top-view-free-space-your-text_187166-37861.jpg?size=626&ext=jpg",
        "price": 62,
        "Rating": 2.5
    },
    {
        "id": 14,
        "title": "Ajowan Caraway (Ajwain)",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/premium-photo/fresh-dried-thyme-leaves-isolated-white_978921-4994.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 138,
        "Rating": 3.5
    },
    {
        "id": 15,
        "title": "Chick Peas (Kabuli)",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/free-photo/chick-pea-wooden-bowl-wooden-surface-close-up_2829-8223.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais", 
        "price": 44,
        "Rating": 3
    },
    {
        "id": 16,
        "title": "Moth Beans (Matki)",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/free-photo/brown-beans-ceramic-plate-concrete_114579-25053.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 126,
        "Rating": 4
    },
    {
        "id": 17,
        "title": "Sugar",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/free-photo/world-diabetes-day-sugar-wooden-bowl-dark-surface_1150-26666.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 44,
        "Rating": 4.5
    },
    {
        "id": 18,
        "title": "Pigeon Beans (Tur Dal)",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/free-photo/raw-soybeans-white-glass-placed-floor_1150-17299.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 198,
        "Rating": 3.5
    },
    {
        "id": 19,
        "title": "Coriandar Powder(Dhania)",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/free-photo/spices-are-placed-spoon-placed-cement-ground_1150-20774.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 96,
        "Rating": 2
    },
    {
        "id": 20,
        "title": "Wheat",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/free-photo/wheat-grains-bowl-wheat-popcorn-bowl-wheat-seed-rustic_114579-1316.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 40,
        "Rating": 3.5
    },
    {
        "id": 21,
        "title": "Rice",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/free-photo/top-view-raw-rice-inside-bag-plate-grey-surface_140725-90597.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 60,
        "Rating": 4.5
    },
    {
        "id": 22,
        "title": "Sorghum (Jowar)",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/free-photo/soybean-seeds-wooden-floor-hemp-sacks-food-nutrition-concept_1150-26328.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 65,
        "Rating": 3
    },
    {
        "id": 23,
        "title": "Bajric (Bajri)",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/free-photo/top-view-quinoa-with-wooden-spoon_140725-9086.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 75,
        "Rating": 2.5
    },
    {
        "id": 24,
        "title": "Bread",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/free-photo/bread-wooden-tray-red-white-cloth_1150-23896.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 49,
        "Rating": 3
    },
    {
        "id": 25,
        "title": "Eggs",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/free-photo/raw-fresh-white-chicken-eggs-placed-stone-surface_2831-8598.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 84,
        "Rating": 4.5
    },
    {
        "id": 26,
        "title": "Milk",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/free-photo/milk-healthy-dairy-products-table_1150-17646.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 56,
        "Rating": 3.5
    },
    {
        "id": 27,
        "title": "Cornflakes",
        "type": "grocery",
        "imgpath": "https://img.freepik.com/free-photo/high-angle-breakfast-corn-flakes-bowl-with-milk-wheat_23-2148417362.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 195,
        "Rating": 4
    }
]
#-----grocery list end ----------

#main function of grocery start
@app.route('/grocery', methods=['GET', 'POST'])
def grocery_api():
    if request.method == 'GET':
        if len(grocery_list) > 0:
            return jsonify(grocery_list)
        else:
            'Nothing Found', 404
        
    if request.method == 'POST':
        new_title = request.form['title']
        iD = grocery_list[-1]['id']+1

        new_obj = {
            'id': iD,
            'title': new_title
        }
        grocery_list.append(new_obj)
        return jsonify(grocery_list), 201
#main function of grocery end
    
#-------fruits list start-----------
fruit_list = [
    {
        "id": 28,
        "title": "Apple",
        "type": "fruits",
        "imgpath": "https://img.freepik.com/free-photo/red-apples-falling-out-bucket-marble-table_114579-20097.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 220,
        "Rating": 3.5
    },
    {
        "id": 29,
        "title": "Banana",
        "type": "fruits",
        "imgpath": "https://img.freepik.com/free-photo/bunch-juicy-yellow-banana-placed-stone-table_114579-46666.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 60,
        "Rating": 4
    },
    {
        "id": 30,
        "title": "Orange",
        "type": "fruits",
        "imgpath": "https://img.freepik.com/free-photo/wooden-board-full-juicy-slices-orange-fruit-stone-table_114579-40329.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 100,
        "Rating": 3 
    },
    {
        "id": 31,
        "title": "Mango",
        "type": "fruits",
        "imgpath": "https://img.freepik.com/free-photo/apricots-wicker-baskets-wooden-table-side-view_176474-9167.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 150,
        "Rating": 4
    },
    {
        "id": 32,
        "title": "Strawberry",
        "type": "fruits",
        "imgpath": "https://img.freepik.com/free-photo/fresh-strawberries-bowl-old-dark-background_1150-37964.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 380,
        "Rating": 2.5
    },
    {
        "id": 33,
        "title": "Grapes",
        "type": "fruits",
        "imgpath": "https://img.freepik.com/free-photo/green-grapes-wicker-basket-textile-plaster-high-angle-view_176474-10557.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 80,
        "Rating": 3.5
    },
    {
        "id": 34,
        "title": "Watermelon",
        "type": "fruits",
        "imgpath": "https://img.freepik.com/free-photo/watermelon-with-slices-grey-grunge-table_176474-7242.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 76,
        "Rating": 4
    },
    {
        "id": 35,
        "title": "Kiwi",
        "type": "fruits",
        "imgpath": "https://img.freepik.com/free-photo/fresh-kiwi-cut-into-half-put-silver-plate_1150-28121.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 120,
        "Rating": 4.5
    },
    {
        "id": 36,
        "title": "Pineapple",
        "type": "fruits",
        "imgpath": "https://img.freepik.com/free-photo/front-view-pineapple-with-one-piece-cut-out-from-whole-fruit-pineapple-slices-cutting-board-with-knife-green-surface_141793-13929.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 65,
        "Rating": 4
    },
    {
        "id": 37,
        "title": "Pear",
        "type": "fruits",
        "imgpath": "https://img.freepik.com/free-photo/green-pears-with-kitchen-towel-basket-white-grungy_176474-8570.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 147,
        "Rating": 3
    },
    {
        "id": 38,
        "title": "Dragon Fruit",
        "type": "fruits",
        "imgpath": "https://img.freepik.com/free-photo/dragon-fruit-with-juice-flat-lay-wooden-cutting-board_176474-9417.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=ais",
        "price": 120,
        "Rating": 3.5
    },
    {
        "id": 39,
        "title": "Pomogranate",
        "type": "fruits",
        "imgpath": "https://img.freepik.com/free-photo/sliced-ripe-pomegranate-wooden-board_114579-55513.jpg?size=626&ext=jpg&uid=R134213934&ga=GA1.1.179978688.1707481184&semt=sph",
        "price": 122,
        "Rating": 2.5
    }
]
#-------fruits list end ------------

#main function of fruits start
@app.route('/fruit', methods=['GET', 'POST'])
def fruit_api():
    if request.method == 'GET':
        if len(fruit_list) > 0:
            return jsonify(fruit_list)
        else:
            'Nothing Found', 404
        
    if request.method == 'POST':
        new_title = request.form['title']
        iD = fruit_list[-1]['id']+1

        new_obj = {
            'id': iD,
            'title': new_title
        }
        fruit_list.append(new_obj)  
        return jsonify(fruit_list), 201
#main function of fruits end

@app.route('/create_json', methods=['POST'])
def create_json():
    json_data = request.json
    if json_data:
        # Process the received JSON data and save it to a file
        with open('localStorageData.json', 'w') as json_file:
            json.dump(json_data, json_file, indent=2)
        return jsonify({'message': 'JSON file created successfully'}), 200
    else:
        return jsonify({'error': 'No JSON data received'}), 400

@app.route('/get_json_data', methods=['GET'])
def get_json_data():
    try:
        # Open and read the JSON file
        with open('localStorageData.json', 'r') as json_file:
            json_data = json.load(json_file)
        # Return the JSON data as a response
        return jsonify(json_data), 200
    except Exception as e:
        # Handle any errors that occur
        return jsonify({'error': str(e)}), 500


@app.route('/empty_json', methods=['POST'])
def empty_json():
    try:
        # Open the JSON file
        with open('localStorageData.json', 'w') as json_file:
            # Clear the contents of the file by writing an empty string
            json_file.write('')

        # Return a success message
        return jsonify({'message': 'JSON file emptied successfully'}), 200
    except Exception as e:
        # Return an error message if an exception occurs
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)