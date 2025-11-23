import ecommerce.shipping       #we are importing shipping from ecommerce package
#or
from ecommerce import shipping
#or
from ecommerce.shipping import calculate_shipping #(if needed more than one module just use ,)

ecommerce.shipping.calculate_shipping() # will print the thing inside calculate shipping function
calculate_shipping()
shipping.calculate_shipping()
