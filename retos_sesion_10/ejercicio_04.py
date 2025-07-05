postres_jane = {"Lemon Pie", "Brownie", "Tarta de Manzana", "Helado de Chocolate", "Flan"}
postres_jhon = {"Carrot Cake", "Croissant de Chocolate", "Lemon Pie", "Tarta de Manzana", "Pudding"}
postres_comunes = postres_jane.intersection(postres_jhon)
porcentaje_comunes = (len(postres_comunes) / len(postres_jane)) * 100
print("Postres en común:", postres_comunes)
print(f"Porcentaje de postres en común (sobre Jane): {porcentaje_comunes:.2f}%")
if porcentaje_comunes > 50:
    print("¡Son compatibles! 💖")
else:
    print("Quizás deban replantear su relación... 🤔")