Estimate big-O running time

import timeit

def estimate_big_o(fun):
  range = [2**5, 2**6]
  time = []

  for n in range:
    seconds = timeit.timeit(
    stmt   = '%s(%d)' % (fun.__name__, n),
    setup  = 'from __main__ import %s' % fun.__name__,
    number = 10
    )
    time.append(seconds)
  average = round((time[1] / time[0]), 2)
  print average

  if (average > 0.0) and (average  <= 1.1): return "O(1)"
  elif (average > 1.1) and (average <= 1.5): return "O(log n)"
  elif (average > 1.5) and (average <= 2.0): return "O(n)"
  elif (average > 2.0) and (average <= 3.0): return "O(n log n)"
  elif (average > 3.0) and (average <= 5.0): return "O(n**2)"

  return "No range fits."

