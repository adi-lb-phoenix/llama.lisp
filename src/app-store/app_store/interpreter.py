import secrets


def _is_list(sexp):
    return isinstance(sexp, list)


def interactive_input(prompt, docs=""):
    print("==> Entering interactive input")
    print(docs)
    inp = input(f"==> {prompt}: ").strip()
    print(f"==> recieved {inp} for {prompt}")
    return inp


standard_lib = {
    "gen-password": lambda: secrets.token_urlsafe(16),
    "interactive-input": interactive_input,
}


def config_lisp(sexp, env=standard_lib):
    if _is_list(sexp):
        if sexp[0] == "let":
            assert len(sexp) == 3
            varialbes = sexp[1]
            body = sexp[2]
            for var_name, var_value in varialbes:
                assert isinstance(var_name, str)
                env[var_name] = config_lisp(var_value, env)

            return config_lisp(body, env)
        elif sexp[0] == "unquote":
            quoted_sexp = sexp[1]
            if _is_list(quoted_sexp):
                # function
                fn_name = quoted_sexp[0]
                args = quoted_sexp[1:]
                return env[fn_name](*args)
            else:
                # variable
                return env[quoted_sexp]
        else:
            return [config_lisp(x, env) for x in sexp]
    else:
        # atom
        return sexp


if __name__ == "__main__":
    import sys
    from parser import parse_sexp

    print(config_lisp(parse_sexp(open(sys.argv[-1]).read())))