from pynput import keyboard #how we be controlling

global keys, opend, INDEX
keys = []
opend = False

#the INDEX. Add your own bindings here
INDEX = {"mult": "×", #multiplication sign which doesn't get confused with x!
  "dot": "·", #dot
  "plusm": "±", #plus-minus
  "minusp": "∓",#opposite way around
  "notequal": "≠", #not equal
  "approx": "≈", #approximately
  "ident": "≡", # identity (hamburger mmm)
  "<=": "≤",
  ">>": "≫",
  ">=": "≥",
  "<<": "≪", 
  "integral": "∫", #integral sign
  "exists": "∃", #there exists a value
  "inf": "∞",
  "aleph": "ℵ", #fancy infinity
  "prop": "∝", #proportionality
  #LOGIC
  "or": "∨",
  "and": "∧",
  "if": "⇒", #if A then B is A ⇒ B
  "onlyif": "⇐", #if B then A is A ⇐ B
  "iff": "⇔", #both ways: A⇔B
  #SETS
  "partof": "∈", # is part of a set
  "natural": "ℕ", #set of natural numbers (positive integers)
  "complex": "ℂ", #complex (all numbers)
  "rational": "ℚ", #rationals (all non-irrational non-complex numbers)
  "real": "ℝ", #reals (all non-complex numbers)
  "integers": "ℤ", #integers (all whole numbers (incl. negatives))
  #GREEK LETTAHS
  "DELTA": "Δ",
  "alpha": "α",
  "beta": "β",
  "gamma": "γ",
  "delta": "δ",
  "epsilon":"ε",
  "zeta": "ζ",
  "pi": "π",
  "PI": "∏",
  "rho": "ρ",
  "SIGMA": "∑",
  "sigma": "σ",
  "theta": "θ",
  "tau": "τ",
  "phi": "φ",
  "lambda": "λ",
  "mu": "μ",
  "omega": "ω",
  "OMEGA": "Ω"}

def on_press(key, injected):
  global opend, keys
  try:
    #print('alphanumeric key {} pressed; it was {}'.format(key.char, 'faked' if injected else 'not faked'))
    if not injected: #if the user actually typed this
      if key.char == "]" and opend == True:
        print("Closing combo")
        print("".join(keys))
        print("Beginning sub...")
        cont = keyboard.Controller()
        #backspace twice to remove the two brackets
        cont.press(keyboard.Key.backspace)
        cont.release(keyboard.Key.backspace)
        cont.press(keyboard.Key.backspace)
        cont.release(keyboard.Key.backspace)
        sub_value("".join(keys).removeprefix("["))
        opend = False
        keys = []
      if key.char == "[":
        opend = True
        print("Reading combo now")
      if opend == True:
        keys.append(key.char)
        print(f"Added {key.char} to combo")
      else:
        pass
  except AttributeError:
    #print('special key {} pressed'.format(key))
    #ignore special keys
    if key == keyboard.Key.backspace and opend:
      keys.pop()
      print(f"Deleted last thing: last letter should be {keys[len(keys)-1]}")
    pass
def on_release(key, injected):
    print('{} released; it was {}'.format(key, 'faked' if injected else 'not faked'))
    if key == keyboard.Key.esc:
        # Stop listener
        return False


def sub_value(string_to_find, ):
  "Replaces the 'string_to_find' with the appropiate list in INDEX"
  global INDEX
  cont = keyboard.Controller()
  for i in string_to_find: #delete existing letters
    cont.press(keyboard.Key.backspace)
    cont.release(keyboard.Key.backspace)
  try:
    new_symbol = INDEX[string_to_find]
    print(f"Swapping '{string_to_find}' to '{new_symbol}'.")
    cont.press(new_symbol)
    cont.release(new_symbol)    
  except:
    print(f"Unknown token '{string_to_find}', ignoring")
    cont.type("NO")


# Collect events until released
with keyboard.Listener(on_press=on_press,on_release=on_release) as listener: listener.join()

''' 

'''
