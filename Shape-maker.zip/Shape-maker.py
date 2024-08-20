from turtle import *
__name__ == "__main__"
Version = "Version 5"
print(Version)
print("Exit\nForm\nlistfunc\nspecial\nhelp")
if 1 == 1:
    while True:
            WF = input("")       
            if WF == "-v":
                print(Version)
            elif WF == "Form.circ":
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
            elif WF == "listfunc.[special]":
                 import funcs
                 funcs.listfunc_spec()
            elif WF == "Form.hexa":
                import funcs
                funcs.Form_hexa()
            elif WF == "Form.dode":
                import funcs
                funcs.Form_dode()
            elif WF == "Form.tria":
                import funcs
                funcs.Form_tria()
            elif WF == "Form.squa":
                 import funcs
                 funcs.Form_squa()
            elif WF == "special.special1":
                 import funcs
                 funcs.Form_spec1()
            elif WF == "help" or "?h":
                    import funcs
                    funcs.help()
