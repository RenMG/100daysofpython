# List to Dict Fantasy Game Inventory. Page 120
# Day 6 of 100, building on day 5

def displayInventory(inventory):
    print("Inventory:")
    item_total = 0
    for k, v in sorted(inventory.items()):
        print(v, k)
        item_total+=v
    print("Total number of items: " + str(item_total))


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']

def addToInventory(inventory, addedItems):
    # your code goes here
    for item in addedItems:
        if item in inventory.keys():
            inv_cnt_update = inventory[item]
            inv_cnt_update += 1
            inventory[item] = inv_cnt_update
        else:
            inv_cnt_update = 1
            inventory[item] = inv_cnt_update
            
    return inventory  


inv = {'gold coin': 42, 'rope': 1}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)
displayInventory(inv)

"""
The gochya here was really in spacing of the return, a lot of my issue was second guessing my for loop, when it really was where i put the last return.

"""