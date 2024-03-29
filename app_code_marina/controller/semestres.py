import frappe


def get_permission_query_conditions(doc):
 
    user = frappe.get_doc("User", frappe.session.user)
    if user.name in ["Administrator",]:
        return ""

    try:
        prof = frappe.get_doc("Employee", {"user_id": user.name}, ["name"])
    except:
        return ""

   
    if not prof:
        return ""

    roles_names = []
    for role in user.roles:
        roles_names.append(role.role)
    
    
    if "Director" in roles_names:
        return ""
