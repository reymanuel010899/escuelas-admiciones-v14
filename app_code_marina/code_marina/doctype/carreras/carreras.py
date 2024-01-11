# Copyright (c) 2024, reymanuel and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Carreras(Document):
    def after_insert(self):
        self.add_carrera_school()


    def add_carrera_school(self):
        escuela = frappe.get_doc('Escuela', self.escuela)
        escuela.append('carreras_name', {
            'carrera_name': self.name
        })
        escuela.save()  
        frappe.db.commit()