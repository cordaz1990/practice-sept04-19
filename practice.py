#polymorphism

def histogram(s):
    d = dict()
    for c in s:
      if c not in d:
          d[c] = 1
      else:
        d[c] = d[c] + 1
        
    return d
  
  
  t = ['spam', 'egg', 'spam', 'spam', 'spam', 'bacon', 'spam']
  histograms(t)
  {'bacon' : 1, 'egg':1, 'spam': 4}
  
