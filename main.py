import json

from fastapi import FastAPI

from models import Patient

app = FastAPI()

with open("patients.json", "r") as f:
    patient_list = json.load(f)

# Use the first name as the unique identifier. For example, in the PUT route, you'd have something like this: "/patients/{first_name}"

patients: list[Patient] = [Patient(**patient) for patient in patient_list]


@app.get("/")
async def get_patients() -> list[Patient]:
    return patients


@app.post("/")
async def create_patient(patient: Patient) -> None:
    patients.append(patient)


@app.put("/{first_name}")
async def update_patient(first_name: str, updated_patient: Patient) -> None:
    for i, patient in enumerate(patients):
        if first_name == patient.first_name:
            patients[i] = updated_patient


@app.delete("/{first_name}")
async def delete_patient(first_name: str) -> None:
    for i, patient in enumerate(patients):
        if first_name == patient.first_name:
            patients.pop(i)
