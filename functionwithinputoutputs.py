def format_name(f_name,l_name):
  if l_name == "" or l_name == "":
    return "No names inserted"
  formated_f_name = f_name.title()
  formated_l_name = l_name.title()
  return f"{formated_f_name} {formated_l_name}"

f_name2 = str(input("First name "))
l_name2 = str(input("Last name "))
format_name(f_name2,l_name2)

def functitle(title):
  fix = title.title()
  return fix

print functitle(l_name)
