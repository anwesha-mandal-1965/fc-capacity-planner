import os
import json
import csv
import random
from datetime import datetime, timedelta

def generate_data():
    random.seed(42)
    
    # Create directories
    os.makedirs('data', exist_ok=True)
    os.makedirs('reports', exist_ok=True)

    # 1. SKU Master
    categories = {
        'Electronics': [('Samsung Galaxy M34', 15000, 0.4, 0.001, 30), ('Redmi Note 13', 18000, 0.4, 0.001, 35), ('Apple iPhone 15', 75000, 0.3, 0.001, 15), ('Sony WH-1000XM5', 25000, 0.5, 0.002, 10), ('JBL Flip 6', 8000, 0.6, 0.002, 25), ('Asus Vivobook', 45000, 1.8, 0.005, 12), ('MacBook Air M2', 95000, 1.2, 0.004, 8), ('iPad Air', 55000, 0.5, 0.002, 18), ('OnePlus 12', 65000, 0.4, 0.001, 20), ('Samsung Galaxy Watch', 22000, 0.2, 0.0005, 15)],
        'Appliances': [('Whirlpool 7.5kg Washer', 18000, 35, 0.2, 8), ('LG 1.5 Ton AC', 35000, 45, 0.3, 10), ('Samsung 253L Fridge', 26000, 50, 0.4, 12), ('Bosch Dishwasher', 40000, 40, 0.3, 5), ('Dyson V11 Vacuum', 45000, 3, 0.02, 4), ('Philips Air Fryer', 8000, 4, 0.03, 15), ('Haier Microwave', 6000, 12, 0.05, 18), ('Voltas 1 Ton AC', 28000, 40, 0.25, 12), ('Sony 55 inch TV', 60000, 15, 0.1, 8), ('LG 65 inch OLED', 120000, 20, 0.15, 4)],
        'Fashion': [('Nike Running Shoes', 4000, 0.8, 0.005, 40), ('Puma T-Shirt', 800, 0.2, 0.001, 80), ('Levis Jeans', 2500, 0.5, 0.003, 60), ('Adidas Sneakers', 5000, 1.0, 0.006, 35), ('H&M Hoodie', 1500, 0.4, 0.004, 50), ('Zara Jacket', 4500, 0.7, 0.005, 30), ('Tommy Hilfiger Shirt', 3000, 0.3, 0.002, 45), ('Under Armour Shorts', 1200, 0.2, 0.001, 55), ('Casio G-Shock', 8000, 0.1, 0.0005, 20), ('Ray-Ban Aviator', 5500, 0.1, 0.0005, 25)],
        'Home & Kitchen': [('Pigeon Gas Stove', 2500, 3.5, 0.015, 25), ('Prestige Cooker', 1500, 2.0, 0.01, 35), ('Milton Thermos', 800, 0.5, 0.003, 40), ('Bombay Dyeing Bedsheet', 1200, 0.8, 0.005, 50), ('Wakefit Mattress', 12000, 25, 0.4, 10), ('Ikea Study Table', 4500, 15, 0.1, 15), ('Nilkamal Chair', 800, 3, 0.05, 30), ('Tupperware Set', 1500, 1.0, 0.008, 45), ('Bajaj Mixer', 2800, 4, 0.02, 28), ('Wonderchef Pan', 1200, 1.2, 0.006, 35)],
        'Grocery': [('Aashirvaad Atta 5kg', 250, 5, 0.005, 150), ('India Gate Basmati 5kg', 500, 5, 0.005, 120), ('Tata Salt 1kg', 25, 1, 0.001, 200), ('Fortune Sunflower Oil 1L', 150, 1, 0.001, 180), ('Maggi Noodles', 140, 0.5, 0.002, 250), ('Brooke Bond Taj Mahal', 450, 0.5, 0.001, 140), ('Amul Butter 500g', 260, 0.5, 0.0005, 160), ('Kelloggs Corn Flakes', 300, 0.4, 0.003, 110), ('Surf Excel 3kg', 450, 3, 0.004, 130), ('Colgate Toothpaste', 110, 0.2, 0.0005, 190)]
    }

    sku_master = []
    sku_id_counter = 1
    for cat, items in categories.items():
        for item in items:
            name, cost, weight, vol, demand = item
            sku_master.append({
                'sku_id': f'SKU{sku_id_counter:03d}',
                'name': name,
                'category': cat,
                'subcategory': 'General',
                'unit_cost': cost,
                'weight_kg': weight,
                'volume_cubic_m': vol,
                'avg_daily_demand': demand
            })
            sku_id_counter += 1
            
    with open('data/sku_master.json', 'w') as f:
        json.dump(sku_master, f, indent=2)

    # 2. FC Master
    fc_master = [
        {'fc_id': 'FC_MUM', 'name': 'Mumbai FC', 'city': 'Mumbai', 'region': 'West', 'storage_capacity': 50000, 'daily_throughput': 5000},
        {'fc_id': 'FC_BLR', 'name': 'Bangalore FC', 'city': 'Bangalore', 'region': 'South', 'storage_capacity': 45000, 'daily_throughput': 4500},
        {'fc_id': 'FC_DEL', 'name': 'Delhi NCR FC', 'city': 'Delhi', 'region': 'North', 'storage_capacity': 55000, 'daily_throughput': 6000},
        {'fc_id': 'FC_HYD', 'name': 'Hyderabad FC', 'city': 'Hyderabad', 'region': 'South', 'storage_capacity': 40000, 'daily_throughput': 4000},
        {'fc_id': 'FC_KOL', 'name': 'Kolkata FC', 'city': 'Kolkata', 'region': 'East', 'storage_capacity': 35000, 'daily_throughput': 3500}
    ]
    with open('data/fc_master.json', 'w') as f:
        json.dump(fc_master, f, indent=2)

    # 3. Demand Forecast
    dates = [(datetime(2024, 1, 1) + timedelta(days=i)).strftime('%Y-%m-%d') for i in range(90)]
    
    demand_forecast = {
        'dates': dates,
        'bau_daily_demand': [0]*90,
        'bbd_daily_demand': [0]*90,
        'by_fc': {fc['fc_id']: {'bau': [0]*90, 'bbd': [0]*90} for fc in fc_master},
        'by_category': {cat: {'bau': [0]*90, 'bbd': [0]*90} for cat in categories.keys()}
    }
    
    sku_fc_daily = {}

    bbd_multipliers = {
        'Electronics': (6, 8),
        'Appliances': (4, 6),
        'Fashion': (3, 5),
        'Home & Kitchen': (2.5, 4),
        'Grocery': (2, 3)
    }

    for sku in sku_master:
        sku_id = sku['sku_id']
        cat = sku['category']
        base_d = sku['avg_daily_demand']
        
        sku_fc_daily[sku_id] = {}
        for fc in fc_master:
            fc_id = fc['fc_id']
            sku_fc_daily[sku_id][fc_id] = {'bau': [], 'bbd': []}
            
            # Regional bias
            bias = 1.0
            if fc_id == 'FC_DEL' and cat == 'Appliances': bias = 1.3
            if fc_id == 'FC_MUM' and cat == 'Electronics': bias = 1.2
            if fc_id == 'FC_BLR' and cat == 'Fashion': bias = 1.2
            
            fc_base = (base_d / 5) * bias # approx split among 5 FCs
            
            for day in range(90):
                daily_bau = max(0, int(random.gauss(fc_base, fc_base * 0.2)))
                is_bbd = 44 <= day <= 48
                if is_bbd:
                    mult = random.uniform(*bbd_multipliers[cat])
                    daily_bbd = int(daily_bau * mult)
                else:
                    daily_bbd = daily_bau
                
                sku_fc_daily[sku_id][fc_id]['bau'].append(daily_bau)
                sku_fc_daily[sku_id][fc_id]['bbd'].append(daily_bbd)
                
                demand_forecast['bau_daily_demand'][day] += daily_bau
                demand_forecast['bbd_daily_demand'][day] += daily_bbd
                
                demand_forecast['by_fc'][fc_id]['bau'][day] += daily_bau
                demand_forecast['by_fc'][fc_id]['bbd'][day] += daily_bbd
                
                demand_forecast['by_category'][cat]['bau'][day] += daily_bau
                demand_forecast['by_category'][cat]['bbd'][day] += daily_bbd

    with open('data/demand_forecast.json', 'w') as f:
        json.dump(demand_forecast, f, indent=2)
        
    with open('data/sku_fc_daily_demand.json', 'w') as f:
        json.dump(sku_fc_daily, f, indent=2)

    # 4. Current Inventory
    inventory = {}
    for sku in sku_master:
        sku_id = sku['sku_id']
        inventory[sku_id] = {}
        for fc in fc_master:
            fc_id = fc['fc_id']
            avg_d = sum(sku_fc_daily[sku_id][fc_id]['bau']) / 90
            days_supply = random.uniform(15, 25)
            inventory[sku_id][fc_id] = int(avg_d * days_supply)
            
    with open('data/inventory.json', 'w') as f:
        json.dump(inventory, f, indent=2)

    print("Data generation complete. Saved in data/ directory.")

if __name__ == '__main__':
    generate_data()
