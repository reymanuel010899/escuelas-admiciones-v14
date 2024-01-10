# Copyright (c) 2024, reymanuel and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Materias(Document):
    def after_insert(self):
        self.add_materia_semester()
        


    def add_materia_semester(self):
        semestre = frappe.get_doc('Semestre', {"name": self.semestre, "carrera": self.carrera })
        semestre.append('materia_item', {
            'materia_name': self.name
        })
        semestre.save()  
        frappe.db.commit()

