# Copyright (c) 2024, reymanuel and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class Notas(Document):
	def after_insert(self):
		if frappe.db.exists("Notas", {"estudiante": self.estudiante, "materia": self.materia}, cache=True):
			frappe.throw("yes")