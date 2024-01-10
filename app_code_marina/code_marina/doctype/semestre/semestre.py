# Copyright (c) 2024, reymanuel and contributors
# For license information, please see license.txt

import frappe
import random
from frappe.model.document import Document

class Semestre(Document):
    def autoname(self):
        if not self.name:
            self.name = f"SEM-{self.semestre}-{random.randint(0, 1000000)}"