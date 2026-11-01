class Patient:
    def __init__(self, patient_id, name):
        self.patient_id = patient_id
        self.name = name

    def display_info(self):
        print(f"Patient ID: {self.patient_id}")
        print(f"Name: {self.name}")


class Appointment:
    def __init__(self, patient, doctor_name):
        self.patient = patient
        self.doctor_name = doctor_name

    def calculate_fee(self):
        raise NotImplementedError(
            "Subclasses must implement calculate_fee()."
        )

    def display_appointment(self):
        self.patient.display_info()
        print(f"Doctor: {self.doctor_name}")
        print(f"Consultation Fee: £{self.calculate_fee():.2f}")


class GeneralAppointment(Appointment):
    def calculate_fee(self):
        return 40.00


class SpecialistAppointment(Appointment):
    def calculate_fee(self):
        return 85.00


class Hospital:
    def __init__(self, name):
        self.name = name
        self.appointments = {}

    def book_appointment(self, appointment):
        patient_id = appointment.patient.patient_id

        if patient_id in self.appointments:
            print("This patient already has an appointment.")
            return

        self.appointments[patient_id] = appointment
        print(f"Appointment booked for {appointment.patient.name}.")

    def display_appointments(self):
        print(f"\n--- {self.name}: Appointments ---")

        if not self.appointments:
            print("No appointments found.")
            return

        for appointment in self.appointments.values():
            appointment.display_appointment()
            print("-" * 30)


# Create patients
patient1 = Patient(101, "Alex")
patient2 = Patient(102, "Sam")

# Create appointments
appointment1 = GeneralAppointment(patient1, "Dr Smith")
appointment2 = SpecialistAppointment(patient2, "Dr Patel")

# Create hospital
hospital = Hospital("City Hospital")

hospital.book_appointment(appointment1)
hospital.book_appointment(appointment2)

hospital.display_appointments()