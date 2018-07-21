class Contract(object):
    def __init__(self, vehicle, customer, monthly_payments=0,length_in_months=0):
      self.vehicle=vehicle
      self.customer=customer
      self.monthly_payments=monthly_payments
      self.length_in_months=length_in_months
      
    def monthly_value(self):
      return self.total_value()\
             /(self.monthly_payments if self.monthly_payments>0 else self.length_in_months)

      
      

class BuyContract(Contract):
  #sale_price() + (1.07 * monthly_payments * sale_price() / 100) - (discount if employee)
    def total_value(self):
      return (self.vehicle.sale_price()+\
             (self.vehicle.i*self.monthly_payments*self.vehicle.sale_price()/100))\
             *(0.9 if self.customer.is_employee() else 1)


class LeaseContract(Contract):
  #sale_price() + (sale_price() * 1.2 / length_in_months)
    def total_value(self):
      return (self.vehicle.sale_price()+\
             (self.vehicle.l/self.length_in_months*self.vehicle.sale_price()))*\
             (0.9 if self.customer.is_employee() else 1)

