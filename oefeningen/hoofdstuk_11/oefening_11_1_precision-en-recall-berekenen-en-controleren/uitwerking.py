from sklearn.metrics import precision_score, recall_score

TP, FP, FN = 80, 20, 40
precision_handmatig = TP / (TP + FP)
recall_handmatig = TP / (TP + FN)

# 80 true positives, 20 false positives, 40 false negatives en 60 true negatives
y_true = [1] * 80 + [0] * 20 + [1] * 40 + [0] * 60
y_pred = [1] * 80 + [1] * 20 + [0] * 40 + [0] * 60

print(f"Precision handmatig: {precision_handmatig:.3f}")
print(f"Recall handmatig: {recall_handmatig:.3f}")
print(f"Precision sklearn: {precision_score(y_true, y_pred):.3f}")
print(f"Recall sklearn: {recall_score(y_true, y_pred):.3f}")
