// Copyright (c) 2024, reymanuel and contributors
// For license information, please see license.txt

frappe.ui.form.on('Notas', {
	// refresh: function(frm) {

	// }
	nota(frm) {
		frm.set_value("nota_virtual", frm.doc.nota)
		
	}
});
