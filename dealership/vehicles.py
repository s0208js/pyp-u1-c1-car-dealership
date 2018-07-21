class Vehicle(object):
  s=1.2
  p=0.004
  i=1.07
  l=1.2
  def __init__(self, maker, model, year, base_price, miles):
    self.maker = maker
    self.model=model
    self.year=year
    self.base_price=base_price
    self.miles=miles
     
  def sale_price(self):
    return self.base_price*self.s
  
  def purchase_price(self):
    return self.sale_price()-(self.miles*self.p)


class Car(Vehicle):
  s=1.2
  p=0.004
  i=1.07
  l=1.2
  


class Motorcycle(Vehicle):
  s=1.1
  p=0.009
  i=1.03
  l=1
  


class Truck(Vehicle):
  s=1.6
  p=0.02
  i=1.11
  l=1.7
  
