// Copyright (c) 2024, rawas and contributors
// For license information, please see license.txt

frappe.ui.form.on('Salary Certificate', {
	refresh: function(frm) {

	}
});

frappe.ui.form.on('Salary Certificate', {
    employee: function(frm) {
        console.log("Employee selected:", frm.doc.employee);
        
        frappe.call({
            method: 'nizwa.nizwa.doctype.salary_certificate.salary_certificate.get_salary_detail',
            args: {
                employee: frm.doc.employee
            },
            callback: function(r) {
                console.log("Response:", r);
                
                if (r.message) {
                    console.log("Message received:", r.message);
                    
                    frm.clear_table('salary_component');
                    $.each(r.message, function(i, d) {
                        var row = frappe.model.add_child(frm.doc, 'Salary Certificate Table', 'salary_component');
                        row.salary_component = d.salary_component;
                        row.abbr = d.abbr;
                        row.amount = d.amount;
                    });
                    refresh_field('salary_component');
                } else {
                    console.log("No message received.");
                }
            },
            error: function(err) {
                console.log("Error occurred:", err);
            }
        });
    }
});

