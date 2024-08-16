rom turtle import *
__name__ == "__main__"

print("Shape maker v4 pre-release")
print("Exit\nForm\nlistfunc\nhelp")
WF = input("")
if WF == "Form.circ":
    import funcs
    funcs.Form_cric()
elif WF == "Form.octa":
    import funcs
    funcs.Form_octa()
elif WF == "Form.nona":
    import funcs
    funcs.Form_nona()  
elif WF == "Exit":
    print("exiting")
    exit()
elif WF == "listfunc.[Form]":
    import funcs
    funcs.listfunc_form()
elif WF == "Form.hexa":
    import funcs
    funcs.Form_hexa()
elif WF == "Form.dode":
    import funcs
    funcs.Form_dode()
elif WF == "help" or "?h":
    import funcs
    funcs.help()
