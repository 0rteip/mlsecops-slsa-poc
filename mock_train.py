print("Training Model")

with open("yolo_trained_model.pt", "w") as y:
  y.write("super well trained model")

with open("mlbom.json", "w") as m:
  m.write(' {"bomFormat": "CycloneDX", "specVersion": "1.5", "metadata": {"component": {"name" : "yolo_final"}}}')

