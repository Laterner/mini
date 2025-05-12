from flask import Flask, render_template, session, redirect, url_for, request, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Замените на что-то более безопасное

# Пример товаров
products_list = {
    1: {"name": "iPhone 14", "price": 1000, "description": "Мощный смартфон от Apple"},
    2: {"name": "Samsung Galaxy S23", "price": 950, "description": "Флагман от Samsung"},
    3: {"name": "Xiaomi 13", "price": 700, "description": "Бюджетный смартфон с топовыми характеристиками"}
}

@app.route('/')
def index():
    return render_template("index.html", products_list=products_list)

@app.route('/products')
def products():
    return render_template("products.html", products_list=products_list)

@app.route('/sell_phone', methods=['GET', 'POST'])
def sell_phone():
    if request.method == 'POST':
        model = request.form.get('model')
        ram = request.form.get('ram')
        rom = request.form.get('rom')
        condition = request.form.get('condition')
        comment = request.form.get('comment')

        # Можно добавить сохранение в БД, отправку на email и т.д.
        flash("Спасибо! Мы рассмотрим предложение и свяжемся с вами.")

        return redirect(url_for('sell_phone'))

    return render_template("sell_phone.html")

@app.route('/product/<int:product_id>')
def product(product_id):
    product = products_list.get(product_id)
    return render_template("product.html", product=product, product_id=product_id)

@app.route('/add_to_cart/<int:product_id>')
def add_to_cart(product_id):
    cart = session.get('cart', {})
    cart[str(product_id)] = cart.get(str(product_id), 0) + 1
    session['cart'] = cart
    return redirect(url_for('index'))

@app.route('/cart')
def cart():
    cart = session.get('cart', {})
    items = []
    total = 0
    for pid, qty in cart.items():
        product = products_list.get(int(pid))
        if product:
            items.append({"product": product, "quantity": qty})
            total += product["price"] * qty
    return render_template("cart.html", items=items, total=total)

@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    cart = session.get('cart', {})
    if str(product_id) in cart:
        del cart[str(product_id)]
        session['cart'] = cart
    return redirect(url_for('cart'))

if __name__ == '__main__':
    app.run(debug=True)
