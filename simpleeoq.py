import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import math


def max_ord_quant(D, k, h):
  return math.sqrt((2*D*k)/h)
  
  
def max_ord_cycle(y_max, D):
  return (y_max / D)
  
  
def eff_lead_time(L, t0_max):
  n = np.floor(L/t0_max)

  return L - (n*t0_max)
  
  
  
def reordering_point(Le, D):
  return Le*D
  
  
  
def cost(D, k, h):
  return math.sqrt(2*D*k*h)
  
  
  
k = [100]  #setup cost
h = [0.02]   #holding cost
D = [100]  # demand
L = 12  #lead time



for i in range(len(k)):
  y_max = max_ord_quant(D[i],k[i],h[i])
  t0_max = max_ord_cycle(y_max,D[i])
  print("\n\n**********************  D=",D[i]," , K = ",k[i],", h = ",h[i],"********************")
  print("Maximum ordering quantity : ", y_max)

  print("Maximum ordering cycle : ", t0_max)


  if t0_max < L:
    print("Since L > t0_max calculate effective lead time")
    Le = eff_lead_time(L, t0_max)
    print("Effective lead time : ", Le)

  else:
    Le = L

  reord_pt = reordering_point(Le, D[i])

  print("Reordering point : ", reord_pt)

  print("Policy :  order",D,"units when the inventory goes below", reord_pt)

  print("Cost associated with policy:", cost(D[0],k[0],h[0]))
