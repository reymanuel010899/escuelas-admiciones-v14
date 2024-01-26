# Copyright (c) 2024, reymanuel and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Notas(Document):
	def before_insert(self):
		if frappe.db.exists("Notas", {"estudiante": self.estudiante, "materia": self.materia}):
			frappe.throw(f"ya al estudiante <b>{self.estudiante}</b/> se le publico una nota")
