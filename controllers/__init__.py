from controllers.customers_controller import customers 
from controllers.order_controller import order 
from controllers.product_controller import products 
# from controllers.cpu_controller import cpu 
# from controllers.gpu_controller import gpu 
# from controllers.psu_controller import psu
from controllers.ram_controller import ram
from controllers.motherboards_controller import motherboards
# from controllers.ratings_controller import ratings
# from controllers.mobo_cpu_compat_controller import mobo_cpu_compat
# from controllers.gpu_psu_compat_controller import gpu_psu_compat

#register controllers here 

registerable_controllers = [customers,order,products,motherboards,ram]