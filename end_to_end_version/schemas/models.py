#---------------------------------------------------------------------
#----------------------------Schema Models----------------------------
#---------------------------------------------------------------------

from pydantic import BaseModel
from typing import Optional

class Sale(BaseModel):
    ORDERNUMBER: int
    QUANTITYORDERED: int
    PRICEEACH: float
    ORDERLINENUMBER: int
    SALES: float
    ORDERDATE: str  # "mes/día/año hora"
    STATUS: str     # ['Shipped' 'Disputed' 'In Process' 'Cancelled' 'On Hold' 'Resolved']
    QTR_ID: int
    MONTH_ID: int
    YEAR_ID: int
    PRODUCTLINE: str
    MSRP: int
    PRODUCTCODE: int
    CUSTOMERNAME: str
    PHONE: str
    ADDRESSLINE1: str
    ADDRESSLINE2: str
    CITY: str
    STATE: str
    POSTALCODE: int
    COUNTRY: str
    TERRITORY: str
    CONTACTLASTNAME: str
    CONTACTFIRSTNAME: str
    DEALSIZE: str   # ['Small' 'Medium' 'Large']

    
