from flask import Flask, jsonify,render_template, request, flash, redirect
from dbConfig import db
from model.Venta import Venta as venta 
from Venta import VentaForm
import os
from dotenv import load_dotenv
load_dotenv()
DATABASE_URL = os.getenv('DATABASE_URL')
TOKEN_KEY = os.getenv('TOKEN_KEY')
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = DATABASE_URL
app.config['SECRET_KEY'] = TOKEN_KEY
db.init_app(app)
with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/Ventas', methods=['GET'])
def ventas():
    ventas = db.session.query(venta).all()
    data = [{'id': venta.id, 'nameProvider': venta.nameProvider, 'nameProduct': venta.nameProduct, 'unitsProduct': venta.unitsProduct, 'pricePerUnit': venta.pricePerUnit, 'date': venta.date} for venta in ventas]
    return jsonify(data)

@app.route('/Venta/<int:id_venta>', methods=['GET'])
def ventaID(id_venta):
    venta = db.get_or_404(venta, id_venta)
    ventaJSON = {'id': venta.id, 'nameProvider': venta.nameProvider, 'nameProduct': venta.nameProduct, 'unitsProduct': venta.unitsProduct, 'pricePerUnit': venta.pricePerUnit, 'date': venta.date}
    return ventaJSON

@app.route('/Venta/<int:id_venta>/delete', methods=['GET'])
def deleteVENTA(id_venta):
    deleteVenta = db.get_or_404(venta, int(id_venta))
    db.session.delete(deleteVenta)
    db.session.commit()
    flash('Venta Eliminada con éxito!', 'success')
    return redirect('/')

@app.route('/Venta/<int:id_venta>/edit', methods=['GET', 'POST'])
def editVenta(id_venta):
    form = VentaForm() 
    if request.method == 'POST':
        form.nameProvider.data = request.form['nameProvider']
        form.nameProduct.data = request.form['nameProduct']
        form.unitsProduct.data = request.form['unitsProduct']
        form.pricePerUnit.data = request.form['pricePerUnit']
        form.date.data = request.form['date']
        editVenta = venta.query.filter_by(id=id_venta).first()
        editVenta.nameProvider = form.nameProvider.data
        editVenta.nameProduct = form.nameProduct.data
        editVenta.unitsProduct = form.unitsProduct.data
        editVenta.pricePerUnit = form.pricePerUnit.data
        editVenta.date = form.date.data
        db.session.commit()
        flash('Venta Editada con éxito!', 'success')
        return redirect('/')
    ventaEdit = db.get_or_404(venta, id_venta)
    return render_template('edit.html', title='Edit', form=form, venta=ventaEdit)

@app.route('/Venta/new', methods=['GET', 'POST'])
def newVenta():
    form = VentaForm(request.form)
    if request.method == 'POST' and form.validate():
        newVenta = venta(nameProvider=form.nameProvider.data, nameProduct=form.nameProduct.data, unitsProduct=form.unitsProduct.data, pricePerUnit=form.pricePerUnit.data, date=form.date.data)
        db.session.add(newVenta)
        db.session.commit()
        flash('Venta Agregada con éxito!', 'success')
        return redirect('/')
    return render_template('new.html', title='New', form=form)

@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html', title='Page Not Found 404', error=error), 404