from controllers.customers_controller import customers 
from controllers.order_controller import order 
from controllers.product_controller import products 
from controllers.cpu_controller import cpu
from controllers.gpu_controller import gpu
from controllers.psu_controller import psu
from controllers.ram_controller import ram
from controllers.motherboards_controller import motherboards
from controllers.admin_controller import admin
from controllers.mobo_cpu_compat_controller import compatibility
from controllers.ratings_controller import rating
from controllers.voltage_req_controller import voltages

#!controllers are registerd in this file.

registerable_controllers = [customers,order,products,motherboards,ram,cpu,gpu,psu,admin,compatibility, rating, voltages]