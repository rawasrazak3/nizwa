// Copyright (c) 2024, rawas and contributors
// For license information, please see license.txt

// frappe.ui.form.on('CRITICAL SUPPLIER ASSESSMENT', {
// 	onload: function(frm) {
// 		if (frm.doc.__unsaved == 1)	{
// 			loadAllStandings(frm);
// 		}
// 	}
// });

// frappe.ui.form.on("Assessment Questionnaire Table", {

// 	assessment: function(frm, cdt, cdn) {
// 		var d = frappe.get_doc(cdt, cdn);
// 		if (d.assessment) {
// 			return frm.call({
// 				method: "nizwa.nizwa.doctype.assessment_questionnaire.assessment_questionnaire.get_questions",
// 				child: d,
// 				args: {
// 					assessment: d.assessment
// 				}
// 			});
// 		}
// 	}
// });

// var loadAllStandings = function(frm) {
// 	frappe.call({
// 		method: "nizwa.nizwa.doctype.assessment_questionnaire.assessment_questionnaire.get_questions_list",
// 		callback: function(r) {
// 			for (var j = 0; j < frm.doc.assessment_questionnaire.length; j++)
// 			{
// 				if(!frm.doc.assessment_questionnaire[j].hasOwnProperty("assessment")) {
// 					frm.get_field("assessment_questionnaire").grid.grid_rows[j].remove();
// 				}
// 			}
// 			for (var i = 0; i < r.message.length; i++)
// 			{
// 				var new_row = frm.add_child("assessment_questionnaire");
// 				new_row.assessment = r.message[i].name;
// 				frm.script_manager.trigger("assessment", new_row.doctype, new_row.name);
// 			}
// 			refresh_field("assessment_questionnaire");
// 		}
// 	});
// };

frappe.ui.form.on('CRITICAL SUPPLIER ASSESSMENT', {
	onload: function(frm) {
		if (frm.doc.__unsaved == 1) {
			loadAllStandings(frm);
		}
	}
});

frappe.ui.form.on("Assessment Questionnaire Table", {
	assessment: function(frm, cdt, cdn) {
		var d = locals[cdt][cdn];
		if (d.assessment) {
			frappe.call({
				method: "nizwa.nizwa.doctype.assessment_questionnaire.assessment_questionnaire.get_questions",
				args: {
					assessment: d.assessment
				},
				callback: function(r) {
					// Handle the callback response if needed
				}
			});
		}
	}
});

var loadAllStandings = function(frm) {
	frappe.call({
		method: "nizwa.nizwa.doctype.assessment_questionnaire.assessment_questionnaire.get_questions_list",
		callback: function(r) {
			frm.clear_table("assessment_questionnaire"); // Clear existing rows

			$.each(r.message, function(i, question) {
				var new_row = frappe.model.add_child(frm.doc, "Assessment Questionnaire Table", "assessment_questionnaire");
				new_row.assessment = question.name;
			});

			frm.refresh_field("assessment_questionnaire"); // Refresh the child table
		}
	});
};
