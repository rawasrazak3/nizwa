# Copyright (c) 2024, rawas and contributors
# For license information, please see license.txt

import frappe
from frappe.model.document import Document

class AssessmentQuestionnaire(Document):
	pass


@frappe.whitelist()
def get_questions(assessment):
	question = frappe.get_doc("Assessment Questionnaire", assessment)

	return question


@frappe.whitelist()
def get_questions_list():
	questions = frappe.db.sql(
		"""
		SELECT
			scs.name
		FROM
			`tabAssessment Questionnaire` scs""",
		{},
		as_dict=1,
	)

	return questions
