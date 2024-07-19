frappe.ui.form.on("Sales Order Item", {
	custom_days: (frm, cdt, cdn) => {
		let item_row = locals[cdt][cdn];
        if(item_row.custom_days != 0 && frm.doc.custom_qty != 0){
            frappe.model.set_value(cdt, cdn, "qty", (item_row.custom_days * item_row.custom_qty));
        }
	},
    custom_qty: (frm, cdt, cdn) => {
		let item_row = locals[cdt][cdn];
        if(item_row.custom_days != 0 && frm.doc.custom_qty != 0){
            frappe.model.set_value(cdt, cdn, "qty", (item_row.custom_days * item_row.custom_qty));
        }
	},
    custom_from_date: (frm, cdt, cdn) => {
        let item_row = locals[cdt][cdn];
        if(item_row.custom_from_date && item_row.custom_to_date){
            let days  = frappe.datetime.get_day_diff(item_row.custom_to_date,  item_row.custom_from_date)
            frappe.model.set_value(cdt, cdn, "custom_days", days);
        }
    },
    custom_to_date: (frm, cdt, cdn) => {
        let item_row = locals[cdt][cdn];
        if(item_row.custom_from_date && item_row.custom_to_date){
            let days  = frappe.datetime.get_day_diff(item_row.custom_to_date,  item_row.custom_from_date)
            frappe.model.set_value(cdt, cdn, "custom_days", days);
        }
    }
});