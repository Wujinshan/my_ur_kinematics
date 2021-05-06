from math import pi
def control_angles(solution):
          for i in range(len(solution)):
                    while True:
                              if solution[i] < -1*pi:
                                        solution[i] = solution[i]+2*pi
                              if solution[i] > pi:
                                        solution[i] = solution[i]-2*pi
                              if abs(solution[i]) <= pi:
                                        break
          return solution