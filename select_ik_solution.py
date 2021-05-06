#选取逆运动学求解的8组结果中和position最接近的值
def select_ik_solution(position, solution):
          #weight各关节角的权重因子
          weight = [1]*6
          #kpi:solution中各解的得分，得分越低越好
          kpi = [0]*len(solution)
          for i in range(len(solution)):
                    kpi[i] = weight[0]*abs(solution[i][0]-position[0])+weight[1]*abs(solution[i][1]-position[1])+weight[2]*abs(solution[i][2]-position[2])+weight[3]*abs(solution[i][3]-position[3])+weight[4]*abs(solution[i][4]-position[4])+weight[5]*abs(solution[i][5]-position[5])
          for i in range(len(kpi)):
                    if kpi[i] == min(kpi):
                              break

          return solution[i]

if __name__ == "__main__":
          position = [1]*6
          solution = [[2]*3+[1]*3,[1]*3+[2]*3,[3]*6,[3]*6,[3]*6,[3]*6,[3]*6,[3]*6]
          print(select_ik_solution(position, solution))