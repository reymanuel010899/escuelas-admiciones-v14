import frappe


def after_insert(doc, method):
    add_profesor_school(doc)
        


def add_profesor_school(doc):
    escuela = frappe.get_doc('Escuela', doc.custom_escuelas)
    escuela.append('profesores_name', {
        'nombre': doc.name
    })
    escuela.save()  
    frappe.db.commit()
