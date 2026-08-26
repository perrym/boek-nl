def train_gewicht(start: float, learning_rate: float, epochs: int) -> float:
    gewicht = start
    doel = 3.0
    for epoch in range(1, epochs + 1):
        fout = gewicht - doel
        gradient = 2 * fout
        gewicht -= learning_rate * gradient
        loss = (gewicht - doel) ** 2
        print(f"epoch={epoch:02d}, gewicht={gewicht:.4f}, loss={loss:.6f}")
    return gewicht

print("Rustige learning rate")
train_gewicht(start=0.0, learning_rate=0.1, epochs=12)

print("\nTe hoge learning rate")
train_gewicht(start=0.0, learning_rate=1.1, epochs=8)
