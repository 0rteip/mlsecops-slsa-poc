print("Training Model")

with open("yolo_trained_model.pt", "w") as y:
  y.write("super well trained model")

with open("mlbom.json", "w") as m:
  m.write("""{
    "components": [
        {
            "bom-ref": "pkg:huggingface/DEEL-AI/LARD_V2@c3b138e",
            "description": "Small training set from LARD V2",
            "name": "LARD_V2 dataset",
            "purl": "pkg:huggingface/DEEL-AI/LARD_V2@c3b138ebf53278a0466dc43030d2cfad0f750f82",
            "type": "data",
            "version": "c3b138ebf53278a0466dc43030d2cfad0f750f82"
        },
        {
            "bom-ref": "pkg:huggingface/Ultralytics/YOLO26",
            "description": "The original YOLOv26 model used for fine tuning by the DEEL Project.",
            "licenses": [
                {
                    "license": {
                        "id": "AGPL-3.0"
                    }
                }
            ],
            "name": "Ultralytics/YOLO26",
            "publisher": "Ultralytics",
            "purl": "pkg:huggingface/Ultralytics/YOLO26",
            "type": "machine-learning-model",
            "version": "unknown"
        }
    ],
    "dependencies": [
        {
            "dependsOn": [
                "pkg:huggingface/DEEL-AI/LARD_V2@c3b138e"
            ],
            "ref": "pkg:data/fina.ptl@9419795"
        },
        {
            "ref": "pkg:huggingface/DEEL-AI/LARD_V2@c3b138e"
        },
        {
            "ref": "pkg:huggingface/Ultralytics/YOLO26"
        }
    ],
    "metadata": {
        "component": {
            "bom-ref": "pkg:data/fina.ptl@9419795",
            "description": "Fine tuned model",
            "hashes": [
                {
                    "alg": "SHA-256",
                    "content": "9419795ce5f4cbfa728174bbc14716a5282b7c76e01f35f3c63da485cc3e21bb"
                }
            ],
            "modelCard": {
                "modelParameters": {
                    "approach": {
                        "type": "supervised"
                    },
                    "datasets": [
                        {
                            "ref": "pkg:huggingface/DEEL-AI/LARD_V2@c3b138e"
                        }
                    ],
                    "inputs": [
                        {
                            "format": "image"
                        }
                    ],
                    "outputs": [
                        {
                            "format": "image"
                        }
                    ],
                    "task": "object detection"
                }
            },
            "name": "fine_tuned_model",
            "properties": [
                {
                    "name": "mlsecops:serialization_format",
                    "value": "pickle"
                },
                {
                    "name": "mlsecops:vulnerability_status",
                    "value": "requires_hash_validation"
                }
            ],
            "purl": "pkg:data/fina.ptl@9419795ce5f4cbfa728174bbc14716a5282b7c76e01f35f3c63da485cc3e21bb",
            "type": "machine-learning-model",
            "version": "9419795ce5f4cbfa728174bbc14716a5282b7c76e01f35f3c63da485cc3e21bb"
        },
        "timestamp": "2026-08-19T10:11:45.802079+00:00"
    },
    "serialNumber": "urn:uuid:68ba6bed-4433-410b-b2c1-ed894897570f",
    "version": 1,
    "$schema": "http://cyclonedx.org/schema/bom-1.5.schema.json",
    "bomFormat": "CycloneDX",
    "specVersion": "1.5"
}""")

