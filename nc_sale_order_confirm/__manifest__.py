

{
    "name": "Sale order confirm only manager",
    "version": "16.0.1.0.6",
    "category": "Sales Management",
    'price': 20.00,
    'currency':'USD',
    'support':'gtnorw@yahoo.com', 
    'author': 'NICA-CREATOR',  
    'summary': 'Blocks the action of confirming sales orders for those who are not authorized',        
    'license': 'OPL-1',
    "depends": ["sale_stock", "account", "sale_management"],  
    'images': ['static/description/main_screenshot.png'],      
    "data": [
       
        "views/sale_order_view.xml","views/user_vista.xml",
        
        
    ],
    "installable": True,
}
