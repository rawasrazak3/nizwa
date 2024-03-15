frappe.ui.form.on("Sales Invoice", {
    refresh: (frm) => {
        let previous_invoice_amount = 0
        let total_special_discount = 0
        frm.add_custom_button(__('Apply Special Discount'), function(){
            $.each(frm.doc.custom_invoice_table, function(index, row){
                previous_invoice_amount +=  row.grand_total; 
            });
            total_special_discount = (frm.doc.custom_discount_percentage / 100) * previous_invoice_amount
            console.log(total_special_discount)
            frm.set_value("custom_previous_invoice_amount", previous_invoice_amount)
            frm.clear_table("items")
            let invoice_discount_table = frm.add_child('items');
            $.each(frm.doc.items || [], function(i, v) {
                frappe.model.set_value(v.doctype, v.name, 'item_code', 'Special Discount')
                frappe.model.set_value(v.doctype, v.name, 'qty', 1)
                frappe.model.set_value(v.doctype, v.name, 'uom', 'Nos')
                frappe.model.set_value(v.doctype, v.name, 'price_list_rate',flt(total_special_discount))
            })
            frm.refresh_fields("items");
        });
    },
    custom_fetch_invoices: (frm) => {
        console.log(frm.doc.custom_from_date )
        console.log(frm.doc.custom_to_date )
        if(frm.doc.custom_from_date && frm.doc.custom_to_date){
            get_invoices(frm)
        }
    }
});

function get_invoices(frm){
    frappe.call({
        method: "nizwa.utils.fetch_invoices",
        args: {
            customer : frm.doc.customer,
            from_date : frm.doc.custom_from_date,
            to_date : frm.doc.custom_to_date
        },
        callback: function (r) {
            if(r.message){
                for(let i = 0 ; i < r.message.length; i++)
                {
                    frm.add_child('custom_invoice_table', {
                        sales_invoice : r.message[i].name,
                        grand_total : r.message[i].grand_total,
                    });
                }
                
            }
            frm.refresh_fields("custom_invoice_table");
        }
    });
}
