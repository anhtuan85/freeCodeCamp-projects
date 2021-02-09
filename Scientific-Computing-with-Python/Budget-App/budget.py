class Category:
  def __init__(self, name):
    self.name = name
    self.budget = 0
    self.ledger = list()

  def deposit(self, amount, description= ""):
    self.budget += amount
    self.ledger.append({"amount": amount, "description": description})
  
  def withdraw(self, amount, description= ""):
    if self.budget >= amount:
      self.budget -= amount
      self.ledger.append({"amount": -amount, "description": description})
      return True
    else:
      return False

  def get_balance(self):
    return self.budget

  def transfer(self, amount, category):
    draw = self.withdraw(amount, "Transfer to " + category.name)

    if draw:
      category.deposit(amount, "Transfer from " + self.name)
    
    return draw

  def check_funds(self, amount):
    return True if self.budget >= amount else False

  def __str__(self):
    #set the title line
    title_num = len(self.name)
    padding = int( (30 - title_num) / 2 )
    info = ("*"*padding) + self.name + ("*"*padding)

    #set the ledger entry lines
    for entry in self.ledger:
      x = 23 - len(entry['description'])
      
      #entry description
      desc = entry['description'] + (" "*x) if x > 0 else entry['description'] if x == 0 else entry['description'][:23]  
      info += "\n" + desc

      #entry amount
      amount = "{:.2f}".format(entry['amount'])
      x = 7 - len(amount)
      info += amount if x == 0 else (" "*x) + amount

    #calculate & include total
    info += "\nTotal: " + "{:.2f}".format(self.get_balance())
    return info

  def get_withdrawals(self):
    total = 0
    for transaction in self.ledger:
      if transaction['amount'] < 0: total += transaction['amount']
    
    return total

def create_spend_chart(categories):
  output = "Percentage spent by category"
  x = len(categories)
  y = 100
  
  #calculate total & percentages for each category
  percentages = list()
  total_spent = 0
  for cat in categories: total_spent += cat.get_withdrawals()
  for cat in categories: 
    raw = cat.get_withdrawals() / total_spent
    percentages.append( int( (raw // .1) * 10 ) )
  

  while y >= 0:
    output += "\n"
    #input the correct right aligned Y axis value
    output += str(y) + "| " if y == 100 else " " + str(y) + "| " if y < 100 and y > 0 else "  0| "

    #loop through each category column and check if a bar value exists
    col = 0
    while col < x:
      if percentages[col] >= y:
        # print(percentages[col], y) 
        output += "o  "
      else: output += " "*3
      col += 1

    y -= 10  

  output += "\n" + " "*4 + "-" + "-"*x*3

  #label x access using double loop for names
  max_name_length = 0
  for cat in categories: 
    if len(cat.name) > max_name_length: max_name_length = len(cat.name) 
  
  z = 0
  while z < max_name_length: 
    output += "\n" + " "*5
    for cat in categories:
      try: output += cat.name[z] + " "*2
      except: output += " "*3

    z += 1

  return output