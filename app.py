from flask import Flask, render_template, request, flash, redirect, url_for, session
from database import Meat, Hesabu

app = Flask(__name__)
app.secret_key = "ghgvfkhsgfshdgfhjsfgef"


@app.route('/')
def index():
    return render_template("index.html")


@app.route('/Shop', methods=['GET', 'POST'])
def Shop():
    if request.method == "POST":
        name = request.form["jina"]
        quantity = request.form["wingi"]
        if name == "p1":
            my_name = "Pork Prime Shoulders Ribs"
            my_price = 790
            total_cost = my_price * int(quantity)
            # Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            # flash("Submitted")
            try:
                available_product = Hesabu.get(Hesabu.name == "Pork Prime Shoulders Ribs")
                available_product.quantity += int(quantity)
                available_product.total_cost += total_cost
                available_product.name = my_name
                available_product.price = my_price
                available_product.save()
                flash("Submitted on update")
            except FileNotFoundError:
                Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
                flash("Submitted")
                return redirect(url_for("Shop"))

        if name == "p2":
            my_name = "Pork belly slices"
            my_price = 820
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "p3":
            my_name = "Pork Hand Boneless"
            my_price = 720
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "p4":
            my_name = "Pork Loin Chops"
            my_price = 1130
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "p5":
            my_name = "Pork Fillet"
            my_price = 735
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "p6":
            my_name = "Pork Belly Ribs"
            my_price = 820
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "p7":
            my_name = "Pork Leg Steaks"
            my_price = 790
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "p8":
            my_name = "Pork Shoulder Chops "
            my_price = 1360
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "p9":
            my_name = "Pork Baby Ribs "
            my_price = 690
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "l1":
            my_name = "Lamb Casserole "
            my_price = 620
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "l2":
            my_name = "Lamb Leg Bone In Sliced "
            my_price = 690
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "l3":
            my_name = "Lamb Shoulder Chops "
            my_price = 785
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "l4":
            my_name = "Lamb Leg Bone In Whole (2.5-4kg) "
            my_price = 1130
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "g1":
            my_name = "Mbuzi Chops"
            my_price = 650
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "g2":
            my_name = "Whole Mbuzi Leg-Sliced (2.5-4kg)-Price per kg"
            my_price = 750
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "g3":
            my_name = "Mbuzi Leg-Whole/Unsliced (2.5-4kg)-Price per kg"
            my_price = 650
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "b1":
            my_name = "Beef Barbecue Ribs"
            my_price = 520
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "b2":
            my_name = "Gichiri (Chuck on bone)"
            my_price = 550
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "b3":
            my_name = "Boneless Succulent Cubes"
            my_price = 670
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "b4":
            my_name = "Striploin"
            my_price = 990
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "b5":
            my_name = "Beef Liver"
            my_price = 535
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "b6":
            my_name = "Soup Bones (Comes in 5-6kg)"
            my_price = 80
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "b7":
            my_name = "Minced Beef High Grade- 1kg pack"
            my_price = 595
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "b8":
            my_name = "Osubuko (Shin on bone)"
            my_price = 480
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "b9":
            my_name = "T bone"
            my_price = 1100
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "b10":
            my_name = "Rump Steak"
            my_price = 850
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "b11":
            my_name = "Beef Fillet"
            my_price = 1250
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "b12":
            my_name = "Ox- Tail"
            my_price = 535
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "b13":
            my_name = "Meaty Soup Bones (Comes in 2kg pack)"
            my_price = 320
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))
        if name == "b14":
            my_name = "Minced Beef High Grade- 500g pack"
            my_price = 405
            total_cost = my_price * int(quantity)
            Hesabu.create(name=my_name, price=my_price, quantity=quantity, total_cost=total_cost)
            flash("Submitted")
            return redirect(url_for("Shop"))

    return render_template("Shop.html")


@app.route('/Cart')
def Cart():
    all_products = Hesabu.select()
    total_amount = 0
    for a_product in all_products:
        total_amount += int(a_product.total_cost)
    return render_template("Cart.html", my_product=all_products, total_amount=total_amount)


@app.route('/delete/<int:id>')
def my_delete(id):
    Hesabu.delete().where(Hesabu.id == id).execute()
    flash("Product deleted successfully")
    return redirect(url_for("Cart"))


@app.route('/add_one/<int:id>')
def add_one_item(id):
    try:
        item = Hesabu.get(Hesabu.id == id)
        item.quantity += 1
        new_total_price = item.price * item.quantity
        item.total_cost = new_total_price
        item.save()
        flash(item.price)
        return redirect(url_for("Cart"))
    except FileNotFoundError:
        flash("Adding product failed")
        return redirect(url_for("Cart"))

@app.route('/minus_one/<int:id>')
def minus_one_item(id):
    try:
        item = Hesabu.get(Hesabu.id == id)
        item.quantity -= 1
        new_total_price1 = item.price * item.quantity
        item.total_cost = new_total_price1
        item.save()
        flash(item  .price)
        return redirect(url_for("Cart"))
    except FileNotFoundError:
        flash("Removing product failed")
        return redirect(url_for("Cart"))


if __name__ == '__main__':
    app.run()
