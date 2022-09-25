from math import sin, cos, tan, radians

angle = float(input("Digite o valor do ângulo: "))
seno = sin(radians(angle))
cosceno = cos(radians(angle))
tangente = tan(radians(angle))

print(f"Seno de {angle}°: {seno:.2f}")
print(f"Cosceno de {angle}°: {cosceno:.2f}")
print(f"Tangente de {angle}°: {tangente:.2f}")