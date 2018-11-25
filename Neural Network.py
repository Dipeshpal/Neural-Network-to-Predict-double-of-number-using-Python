# Neural Network to predict double of number
# Instead of getting input from user you can initialize list of multiples input
li = []
inputs = input("Enter a number: ")
inputs = int(inputs)
li.append(inputs)
t = 2

def correct_ans(li):
    return t*li

def neural_network(ip):
    weight = 5
    #cost = 0
    for j in range(1000):
        #print("Input: ", ip, ", Weight: ", weight, ", cost: ", cost)
        pred_ans = ip * weight
        cost = corr_ans - pred_ans
        weight = weight + 0.1*cost
    return pred_ans

def accuracyfun(corr_ans, pred_ans):
    return (corr_ans/pred_ans)*100

for i in li:
    corr_ans = correct_ans(i)
    pred_ans = neural_network(i)
    accuracy = accuracyfun(corr_ans, pred_ans)
    print("Correct Ans: ", corr_ans)
    print("Predicted Ans: ", pred_ans)
    print("Accuracy: ", accuracy)

