#---------------------------------------------------------------------
#----------------------------Schema Models----------------------------
#---------------------------------------------------------------------

from pydantic import BaseModel, Field, validator
from typing import Optional
from datetime import datetime

# Constates
DATE_FORMAT = '%m/%d/%Y %H:%M'

# Modelo de una venta
class Sale(BaseModel):
    ORDERNUMBER: int
    QUANTITYORDERED: int
    PRICEEACH: float
    ORDERLINENUMBER: int
    SALES: float
    ORDERDATE: str = Field(
        example=datetime.strftime(datetime.now(), DATE_FORMAT),
        description='Fecha en formato "mes/día/año hora:minuto"',
    )
    STATUS: str = Field(
        default='In Process',
        example=['Shipped', 'Disputed', 'In Process', 'Cancelled', 'On Hold', 'Resolved'],
        description='Estado del envío de la orden (ej. “En proceso”).'
    )
    QTR_ID: int = Field(
        default=(datetime.now().month-1) // 3 + 1,
        example=[1, 2, 3, 4],
        description='Identificador del trimestre del año en que se realizó la orden.'
    )
    MONTH_ID: int = Field(
        default=datetime.now().month,
        example=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12],
        description='Identificador del mes del año en que se realizó la orden.'
    )
    YEAR_ID: int = Field(
        default=datetime.now().year,
        description='Año en que se realizó la orden.'
    )
    PRODUCTLINE: str = Field(
        default='Motorcycles',
        example=['Motorcycles', 'Classic Cars', 'Trucks and Buses', 'Vintage Cars', 'Planes', 'Ships', 'Trains'],
        description='Tipo de producto'
    )
    MSRP: int
    PRODUCTCODE: str
    CUSTOMERNAME: str
    PHONE: Optional[str] = None
    ADDRESSLINE1: Optional[str] = None
    ADDRESSLINE2: Optional[str] = None
    CITY: Optional[str] = None
    STATE: Optional[str] = None
    POSTALCODE: Optional[str] = None
    COUNTRY: Optional[str] = None
    TERRITORY: Optional[str] = None
    CONTACTLASTNAME: str
    CONTACTFIRSTNAME: str
    DEALSIZE: str = Field(
        default='Small',
        example=['Small', 'Medium', 'Large'],
        description='Tamaño de la transacción (ej. "Pequeño", "Mediano", "Grande").'
    )

    # Validaciones
    @validator('ORDERDATE')
    @classmethod
    def validate_date(cls, date):
        try:
            datetime.strptime(date, DATE_FORMAT)
            return date
        except ValueError:
            raise ValueError('El formato de fecha debe ser "mes/día/año hora" (ejemplo: 01/15/2023 09:30)')

    @validator('STATUS')
    @classmethod
    def validate_status(cls, status):
        if status not in ['Shipped', 'Disputed', 'In Process', 'Cancelled', 'On Hold', 'Resolved']:
            raise ValueError('El estado debe ser ["Shipped" "Disputed" "In Process" "Cancelled" "On Hold" "Resolved"]')
        return status

    @validator('DEALSIZE')
    @classmethod
    def validate_dealsize(cls, dealsize):
        if dealsize not in ['Small', 'Medium', 'Large']:
            raise ValueError('El estado debe ser ["Small" "Medium" "Large"]')
        return dealsize

    @validator('QTR_ID')
    @classmethod
    def validate_qtr_id(cls, qtr_id):
        if qtr_id < 1 or qtr_id > 4:
            raise ValueError('El identificador del trimestre debe ser [1 2 3 4]')
        return qtr_id

    @validator('MONTH_ID')
    @classmethod
    def validate_qtr_id(cls, month_id):
        if month_id < 1 or month_id > 12:
            raise ValueError('El identificador del mes debe ser [1 2 3 4 5 6 7 8 9 10 11 12]')
        return month_id

    @validator('PRODUCTLINE')
    @classmethod
    def validate_dealsize(cls, productline):
        if productline not in ['Motorcycles', 'Classic Cars', 'Trucks and Buses', 'Vintage Cars', 'Planes', 'Ships', 'Trains']:
            raise ValueError("El producto debe ser ['Motorcycles' 'Classic Cars' 'Trucks and Buses' 'Vintage Cars' 'Planes' 'Ships' 'Trains']")
        return productline

    @validator('SALES')
    @classmethod
    def validate_sales(cls, sales, values):
        quantity = values.get('QUANTITYORDERED')
        price = values.get('PRICEEACH')
        if sales != quantity*price:
            raise ValueError('La venta no se corresponde con cantidad y precio')
        return sales
