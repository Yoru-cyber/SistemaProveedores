from dbConfig import db
from sqlalchemy import BIGINT, VARCHAR, DATE, DECIMAL
from sqlalchemy.orm import Mapped, mapped_column
class Venta(db.Model):
    __tablename__ = 'ventas'
    id: Mapped[BIGINT] = mapped_column(BIGINT, primary_key=True)
    nameProvider: Mapped[VARCHAR] = mapped_column(VARCHAR)
    nameProduct: Mapped[VARCHAR] = mapped_column(VARCHAR)
    unitsProduct: Mapped[BIGINT] = mapped_column(BIGINT)
    pricePerUnit: Mapped[DECIMAL] = mapped_column(DECIMAL(8,2))
    date: Mapped[DATE] = mapped_column(DATE)
