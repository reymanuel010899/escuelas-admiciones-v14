// Copyright (c) 2024, reymanuel and contributors
// For license information, please see license.txt

frappe.ui.form.on('Estudiantes', {
	// refresh: function(frm) {
	// },
	custom_semestres (frm) {
        frappe.call({
            method: "app_code_marina.code_marina.doctype.estudiantes.estudiantes.crear_matricula",
            args: {
				semestre : frm.doc.custom_semestres
			},
            callback(response) {
				frm.set_value("matricula", response.message)
				frm.refresh_field("matricula")
            }
        })

    }
});
