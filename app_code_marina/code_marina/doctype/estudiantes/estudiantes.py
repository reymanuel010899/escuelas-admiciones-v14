# Copyright (c) 2024, reymanuel and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document

class Estudiantes(Document):
	def after_insert(self):
		self.add_student_school()

	def add_student_school(self):
		escuela = frappe.get_doc('Escuela', self.escuela)
		escuela.append('estudiante_name', {
			'nombre': self.name
		})
		escuela.save()  
		frappe.db.commit()

def generar_matricula_randon(semestre=None):
	return f"{semestre}-{random.randint(0, 100000)}"

@frappe.whitelist()
def crear_matricula(semestre):
	return generar_matricula_randon(semestre)
