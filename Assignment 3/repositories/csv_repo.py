import csv
from typing import List, Optional
from repositories.base import BaseRepository
from routes.patients import Patient  # Example: Adjust for other models

CSV_FILE = "patients.csv"

class CSVRepository(BaseRepository[Patient]):
    def create(self, item: Patient) -> Patient:
        with open(CSV_FILE, mode="a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([item.id, item.name, item.email, item.phone])
        return item

    def get(self, item_id: int) -> Optional[Patient]:
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and int(row[0]) == item_id:
                    return Patient(id=int(row[0]), name=row[1], email=row[2], phone=row[3])
        return None

    def get_all(self) -> List[Patient]:
        patients = []
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    patients.append(Patient(id=int(row[0]), name=row[1], email=row[2], phone=row[3]))
        return patients

    def update(self, item_id: int, item: Patient) -> Optional[Patient]:
        rows = []
        updated = False
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and int(row[0]) == item_id:
                    rows.append([item.id, item.name, item.email, item.phone])
                    updated = True
                else:
                    rows.append(row)
        
        if updated:
            with open(CSV_FILE, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            return item
        return None

    def delete(self, item_id: int) -> bool:
        rows = []
        deleted = False
        with open(CSV_FILE, mode="r") as file:
            reader = csv.reader(file)
            for row in reader:
                if row and int(row[0]) != item_id:
                    rows.append(row)
                else:
                    deleted = True
        
        if deleted:
            with open(CSV_FILE, mode="w", newline="") as file:
                writer = csv.writer(file)
                writer.writerows(rows)
            return True
        return False
