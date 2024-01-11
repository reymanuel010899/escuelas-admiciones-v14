// Copyright (c) 2024, reymanuel and contributors
// For license information, please see license.txt

frappe.ui.form.on('Materias', {
    refresh(frm) {
        frm.trigger("set_queries");
    },
    set_queries(frm) {
        frm.set_query("semestre", () => {
            return {
                filters: {
                    "carrera": frm.doc.carrera,
                }
            }
        });
    },


});