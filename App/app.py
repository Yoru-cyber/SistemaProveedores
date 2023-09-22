from flask import Flask, jsonify, json, render_template
from dbConfig import db
from sqlalchemy import BIGINT, VARCHAR, DATE, DECIMAL, text
from sqlalchemy.orm import Mapped, mapped_column
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqldb://root:1234@localhost/ventas'
db.init_app(app)

#model
class Venta(db.Model):
    __tablename__ = 'ventas'
    id: Mapped[BIGINT] = mapped_column(BIGINT, primary_key=True)
    nameProvider: Mapped[VARCHAR] = mapped_column(VARCHAR)
    nameProduct: Mapped[VARCHAR] = mapped_column(VARCHAR)
    unitsProduct: Mapped[BIGINT] = mapped_column(BIGINT)
    pricePerUnit: Mapped[DECIMAL] = mapped_column(DECIMAL(10,2))
    date: Mapped[DATE] = mapped_column(DATE)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/Ventas')
def ventas():
    ventas = db.session.query(Venta).all()
    data = [{'id': venta.id, 'nameProvider': venta.nameProvider, 'nameProduct': venta.nameProduct, 'unitsProduct': venta.unitsProduct, 'pricePerUnit': venta.pricePerUnit, 'date': venta.date} for venta in ventas]
    return jsonify(data)

@app.route('/Venta/<int:id_venta>')
def ventaID(id_venta):
    venta = db.get_or_404(Venta, id_venta)
    ventaJSON = {'id': venta.id, 'nameProvider': venta.nameProvider, 'nameProduct': venta.nameProduct, 'unitsProduct': venta.unitsProduct, 'pricePerUnit': venta.pricePerUnit, 'date': venta.date}
    return ventaJSON